# %%


# %%
import tifffile
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import tensorflow as tf

# %%
ori = tifffile.imread("1. SEM_original.tif")
compo = tifffile.imread("3. connectorsDetected_individualID.tif")

# %%
indi_compo = []
target_size = (128, 128)
for i in range(1, compo.max() + 1):
    bounding_box = cv.boundingRect((compo == i).astype(np.uint8))
    component = ori[bounding_box[1] : bounding_box[1] + bounding_box[3], bounding_box[0] : bounding_box[0] + bounding_box[2]]
    delta_shape = (target_size[0] - component.shape[0], target_size[1] - component.shape[1])
    top, bottom = delta_shape[0] // 2, delta_shape[0] - (delta_shape[0] // 2)
    left, right = delta_shape[1] // 2, delta_shape[1] - (delta_shape[1] // 2)
    component = cv.copyMakeBorder(component, top, bottom, left, right, cv.BORDER_CONSTANT, value=0)
    indi_compo.append(component)


# %%

mdl = tf.keras.applications.EfficientNetV2L(
    include_top=False,
    weights="imagenet",
    input_tensor=None,
    input_shape=(128, 128, 3),
    name="efficientnetv2-l",
)
preprocess = tf.keras.applications.efficientnet_v2.preprocess_input

inputs = np.array(indi_compo)
inputs = np.expand_dims(inputs, axis=-1)
inputs = np.repeat(inputs, 3, axis=-1)
inputs = preprocess(inputs)

outputs = mdl.predict(inputs)

# %%
out = outputs#[:,1:3,1:3,:]
avg = np.mean(out, axis=(1, 2))
max = np.max(out, axis=(1, 2)) 
avg_max_ = np.concatenate((avg, max), axis=1)

sd = np.std(avg,axis=0)
selected_features = np.concatenate((sd>0.04, sd>0.04), axis=0)

avg_max = avg_max_[:,selected_features]  # Keep only features with std > 0.1

# %%
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Standardize the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(avg_max.reshape(outputs.shape[0], -1))


# Compute just PC1 for horizontal separation
pca = PCA(n_components=128)
pca_transformed = pca.fit_transform(features_scaled)
pc1 = pca_transformed[:, 0]
pc2 = pca_transformed[:, 1]


# Train on the full 8192-dimensional space
iso_forest = IsolationForest(contamination=0.001, random_state=42)
iso_forest.fit(features_scaled)

# Get anomaly scores (lower scores = more anomalous)
# We invert it so higher value = more anomalous
anomaly_scores = -iso_forest.score_samples(features_scaled)



# %%
# Plotting code for the score-based graph
plt.figure(figsize=(5, 4))
plt.scatter(pc1, anomaly_scores, c=anomaly_scores, cmap='viridis', edgecolors='w', s=30)
# plt.colorbar(label='Anomaly Score Intensity')
plt.xlabel('Global Structure variations')
plt.ylabel('Isolation Forest Anomaly Score (High = Defect)')
plt.title('Unsupervised Anomaly Detection')
plt.grid(True, linestyle='--', alpha=0.5)
plt.plot([pc1.min(), pc1.max()], [0.55, 0.55], 'r--')
plt.plot([-30, -30], [anomaly_scores.min(), anomaly_scores.max()], 'r--')
plt.plot([30, 30], [anomaly_scores.min(), anomaly_scores.max()], 'r--')


strong_suspects = np.where(((pc1 < -30) | (pc1 > 30)) & (anomaly_scores > 0.55))[0]
suspects = np.where((pc1 < -30) | (pc1 > 30) | (anomaly_scores > 0.55))[0]
suspects = np.setdiff1d(suspects, strong_suspects)

plt.scatter(pc1[suspects], anomaly_scores[suspects], c='orange', edgecolors='w', s=40, label='Suspects')
plt.scatter(pc1[strong_suspects], anomaly_scores[strong_suspects], c='red', edgecolors='w', s=40, label='Strong Suspects')
plt.legend()

plt.savefig("anomaly.svg", transparent=True)

plt.show()

# %%
# Identify suspects and strong suspects in 3ch ori image
ori_img = ori.copy()
ori_img = cv.cvtColor(ori_img, cv.COLOR_GRAY2BGR)  # Convert to BGR for colored rectangles
gap=5
for suspect in suspects:
    bounding_box = cv.boundingRect((compo == (suspect + 1)).astype(np.uint8))
    cv.rectangle(
        ori_img, (bounding_box[0]-gap, bounding_box[1]-gap), (bounding_box[0] + bounding_box[2]+gap, bounding_box[1] + bounding_box[3]+gap), 
        (255, 165, 0), 4)  # Orange for suspects

for strong_suspect in strong_suspects:
    bounding_box = cv.boundingRect((compo == (strong_suspect + 1)).astype(np.uint8))
    cv.rectangle(
        ori_img, (bounding_box[0]-gap, bounding_box[1]-gap), (bounding_box[0] + bounding_box[2]+gap, bounding_box[1] + bounding_box[3]+gap), 
        (255, 0, 0), 4)  # Red for strong suspects

# %%
# plt.imshow(ori_img)
# plt.title('Detected Suspects and Strong Suspects')
# plt.axis('off')
# plt.show()

# %%
# tifffile.imwrite("A_trojan_suspects.tif", ori_img)

# %%
import pandas as pd
# 2. Convert to a Pandas DataFrame
df = pd.DataFrame(features_scaled, columns=[f'Feature_{i}' for i in range(features_scaled.shape[1])])

# 3. Save to Excel (index=False removes the row numbers)
df.to_excel("features.xlsx", index=False, header=False)


# %%
# 2. Convert to a Pandas DataFrame
df = pd.DataFrame(np.stack([pc1,anomaly_scores], axis=-1), columns=['PC1', 'IsolationForestAnomalyScore'])

# 3. Save to Excel (index=False removes the row numbers)
df.to_excel("PC1_vs_IsolationForestAnomalyScore.xlsx", index=False, header=True)


# %%




