# Logic Byte Website — Handover

Operational handover for continuing the website build. Pairs with `logicbyte_ai_readme.md`.
**Current focus for the next session: build `custom.html` (Custom Solutions vertical).**

> Reflects state at the end of the semiconductor-page build. Supersedes earlier copies.

---

## 1. Where things stand

- **Locked / done:** `index.html`, `platform.html`, `biomedical.html`, `about.html`, `research.html`, `contact.html`.
- **`biomedical.html` is the canonical design-system template** (head + CSS tokens, nav, mobile drawer, footer, scripts). Build new vertical pages from it.
- **`semiconductor.html` — complete and publication-ready.** Built from the locked template; only meta/title/canonical/OG/Twitter, `nav aria-current`, footer (plain-text email), and the new body content differ. Passes overflow QA 360–1920px; all guardrails intact.
- **Latest semiconductor changes worth knowing:**
  - Signature section now embeds a **looping, animated reference-free anomaly-detection pipeline** (`optiflow-anomaly-pipeline-embed.html`), replacing the old before/after slider. Built from the founder's **real EM data** (713 connectors → 20 flagged → 10 strong; PCA PC1 ≈ 61%, PC2 ≈ 18%).
  - Editorial pass applied: hero "See it in action" → `#assurance`; "hardware-Trojan" named in meta + the hardware-assurance card; signature value-point #5 changed from "Air-gapped & auditable" to **"Triage hundreds to a handful"** (ROI message, ties to the animation); minor precision/redundancy fixes; over-repetition of the air-gapped claim trimmed.
- **`mailto:` removed site-wide** (biomedical + semiconductor) — email is plain text, actions route to `contact.html`.

---

## 2. Build & QA workflow (use this exactly)

**The founder expects a structural proposal before any significant build, then autonomous execution once a direction is approved.** Large docs/pages are reviewed section-by-section; the founder often makes final tweaks in their own tools and re-uploads.

- **All large HTML/copy edits via Python assertion-guarded replacement scripts.** Each replacement asserts the exact-match count before/after, so a one-character drift fails loudly rather than silently corrupting the file. Pattern:
  ```python
  def rep(old,new,n=1,label=""):
      assert s.count(old)==n, f"[{label}] expected {n}, found {s.count(old)}"
      return s.replace(old,new)
  ```
- **QA every page with Playwright/Chromium**, run against local `file://` with `--no-sandbox`:
  - Horizontal-overflow sweep at **360, 390, 414, 768, 1024, 1280, 1440, 1920** (assert `scrollWidth ≤ clientWidth`).
  - **2× DPR element screenshots** of each section for visual review.
  - For embeds: scroll the iframe into view, wait for it to lazy-load + post height, assert the iframe got an explicit height and the loader is hidden.
- **Deliverables via `present_files`** — never commit to GitHub directly. The founder commits.

---

## 3. The iframe height contract (how embeds size themselves)

Embeds are lazy-loaded and self-size via `postMessage`. To add an embed to a page:

**Markup (in the section):**
```html
<div class="demo-loading" id="ld-NAME"><div class="spinner"></div><span>Preparing live demo&hellip;</span></div>
<iframe class="demo-frame" id="demo-NAME" data-src="EMBED-FILE.html" title="…" loading="lazy" scrolling="no"></iframe>
```
**Register in the page's foot script `frameMap`:**
```js
var frameMap = {
  'optiflow-workflow-from-image-embed.html' : {el:document.getElementById('demo-wfi'),     loader:document.getElementById('ld-wfi')},
  'optiflow-anomaly-pipeline-embed.html'    : {el:document.getElementById('demo-anomaly'), loader:document.getElementById('ld-anomaly')}
  // add new embeds here, keyed by filename
};
```
**Mechanism (already in every page):**
- An `IntersectionObserver` (rootMargin `400px`) sets `iframe.src = data-src` when near-viewport.
- The embed posts `parent.postMessage({optiflowEmbedHeight: H}, '*')` on load / resize / `ResizeObserver`.
- The page handler matches by `contentWindow`, sets `iframe.style.height`, `aspectRatio:'auto'`, and hides the loader. It accepts `optiflowEmbedHeight` | `optiflowWindowHeight` | `height`.

---

## 4. The anomaly-pipeline embed (`optiflow-anomaly-pipeline-embed.html`)

Self-contained, looping, dependency-free (Google Fonts only). Seven cross-faded stages with a status pill, a live metrics readout, and a 7-node stepper:

`Image → Detect → Segment → Characterise (Features) → Gate → Trace back → Review`

- **Detect/Segment** screen-blend recoloured overlays over the greyscale SEM (connectors light up teal, then per-instance colour).
- **Characterise** shows a connector crop → CNN motif → feature-matrix heatmap (**713 × 334**).
- **Gate** is a brand-styled PCA scatter (teal cloud, gold dashed gate ellipse, orange suspects, red strong) rendered from the real matrix.
- **Trace back** pops the 20 boxes onto the SEM (coords inlined in the file), then zooms into a curated cluster.
- **Review** is a collage of the 10 strong-suspect crops.
- Responsive (stacks ≤ 680px), respects `prefers-reduced-motion`, posts its own height.
- **Ships with six assets in the same directory:** `ap-sem.jpg`, `ap-detected.png`, `ap-instances.png`, `ap-scatter.png`, `ap-matrix.png`, `ap-collage.jpg`.

**Regenerating the assets** (if the source data changes): the founder holds the originals — `1__SEM_original.jpg`, `2__connectorsDetected.png`, `3__individualConnectors_IDed.png`, `4__feature_matrix.xlsx`, `6__suspectConnectors.jpg` (`5__Anomaly_gating.svg` is *not* used; the scatter is re-rendered from the matrix for brand control). The generator: optimises the SEM; recolours detect/instance masks for screen-blend; runs PCA → 2D and draws the gated scatter; renders the matrix heatmap; extracts the 20 box coordinates from the suspects image and crops the strong-suspect collage from the full-resolution SEM.

---

## 5. Playbook — building `custom.html`

**Goal:** the Custom Solutions vertical — bespoke pipelines for *any* domain. It is an equal third vertical, not a lesser one; project confidence and breadth (we can take on imaging problems outside bio/semicon).

**Steps:**
1. **Copy `biomedical.html` (or `semiconductor.html`) verbatim** and change *only*, via assertion-guarded edits:
   - `<meta name="description">`, `<title>`, `<link rel="canonical">`, `og:*`, `twitter:*` → Custom Solutions.
   - `nav aria-current="page"` and drawer `aria-current` → the `custom.html` links (already present in the dropdown/drawer of every page).
   - Footer email already plain text — leave as is (no `mailto:`).
   - Replace the body sections.
2. **Section skeleton to mirror** (same components, custom-framed copy):
   - **Hero** — broad promise ("Any imaging problem, your pipeline" style).
   - **Proof bar** — same public-safe proof points.
   - **A problem/gap section** — why generic tools fail bespoke imaging; why a custom-but-auditable approach wins.
   - **Who we serve / what we take on** — the breadth: domains and modalities beyond bio/semicon (e.g. materials, agriculture, food, geology, NDT, art/heritage, remote sensing — pick credible ones), plus an explicit "bring us your problem" card.
   - **Signature / showcase** — the custom differentiator: co-developed pipelines, models trained on the client's own data, delivered as an auditable OptiFlow workflow. Reuse the workflow-from-image embed here.
   - **Capabilities** — the same domain-agnostic toolkit framing.
   - **Integrity** — identical provenance / air-gapped / exportable-method story.
   - **From research to production** — credibility (the same research record + ETH production proof).
   - **How we work** — the Explore → Deploy → Expand → Embed flow + value chips.
   - **CTA + footer.**
3. **Wire the workflow-from-image embed to `?mode=both`** on the custom page (custom spans bio + semicon), registered in `frameMap` exactly as in §3.
4. **QA** per §2 (overflow sweep + section screenshots; embed loads and sizes).
5. **Keep all guardrails** (British English, no pricing, no `mailto:`, no fabricated metrics, three verticals equal, ETH Zürich umlaut, etc.).

**Copy voice:** short punchy headlines, declarative and confident, no overselling, no invitational hedging. Lead with what we *do*, name the client's terms of art, make value-for-money and "your data, your machines" explicit.

---

## 6. Open items (whole site)
- `custom.html` (this next).
- Google Search Console: `www → non-www` redirect (`vercel.json`); swap `href="index.html"` → `href="/"` site-wide.
- Decide on the sub-10px micro-label fonts (`.rsr-label`, `.tag-new`, `.ba-tag`) — bump site-wide or leave.
- Separate strategic doc requested earlier: biosecurity / bio-defence market angle (not a website task).

## 7. Key external relationships (context only — never on site)
NTU: Dr. Liu Qing (NiCE, trial), Hong Siang (day-to-day), Prof. Gan Chee Lip (CHA, future). MIT Semiconductor: Yensan Yong (not yet confirmed — keep off public materials). Investor/mentor: Ali Hasnain (BLOCK71, via Fahad Kidwai). Founder operates publicly as Dr. Doorgesh Sharma Jokhun, PhD; also Lead AI Engineer (Computer Vision) at Borries.
