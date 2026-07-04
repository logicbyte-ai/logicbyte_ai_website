# Logic Byte — Website (`logicbyte_ai`)

Marketing site for **Logic Byte Pte. Ltd.** (Singapore deep-tech, incorporated 2023). Flagship product **OptiFlow** — a modular, domain-aware, no-code visual workflow builder for image analytics. Engine for virtual staining: **CytoByte** (biomedical).

- **Live:** https://logicbyte.ai
- **Stack:** Static HTML/CSS/JS — no framework, no build step. Deployed on **Vercel** from this **GitHub** repo. DNS on **Namecheap**. Indexing via **Google Search Console**.
- **Three equal verticals:** Biomedical & Life Sciences · Semiconductor & Industrial Imaging · Custom Solutions. *Treat them as equals everywhere.*

> Reflects site state at end of **research pages rebuild + about.html founder bio update**. All nine pages are now on the canonical design system. `LogicByte_Website_Handover.md` has been retired — its operational content is merged here.

---

## Repository layout

### Pages

| File | Status | Notes |
|---|---|---|
| `index.html` | ✅ Locked | Home / verticals hub. Canonical design system. `mailto:` removed (footer email plain text). |
| `platform.html` | ✅ Locked | Full OptiFlow platform. Canonical design system. `mailto:` removed; `pseudo-DAPI` removed. |
| `biomedical.html` | ✅ Locked | **Design-system reference template.** Build/refresh every other page from this. |
| `semiconductor.html` | ✅ Publication-ready | Animated reference-free anomaly-detection pipeline embed in signature section. |
| `custom.html` | ✅ Publication-ready | Any-domain vertical. See "custom.html — final state". |
| `about.html` | ✅ Publication-ready | Credibility anchor. Rebuilt on canonical system + full editorial pass. See "about.html — final state". Ships with `mission_arch.png` + founder photo. |
| `contact.html` | ✅ Publication-ready | Conversion endpoint. Formspree back-end. `?intent=` routing intact. See "contact.html — final state". |
| `research.html` | ✅ Publication-ready | **Rebuilt onto the canonical design system this session.** Credibility / proof page — proof-axis framing (not domain-axis). See "research.html — final state". |
| `research-output.html` | ✅ Publication-ready | **Rebuilt onto the canonical design system this session.** Full bibliographic record — filterable, source-linked. See "research-output.html — final state". **Retains `pseudo-DAPI` in one manuscript-in-preparation title only — do not alter.** |

All nine pages are now on the canonical design system. No pages remain on the older system.

### Demo embeds (loaded as lazy iframes)

| File | Used by | Modes |
|---|---|---|
| `optiflow-workflow-from-image-embed.html` | `biomedical`, `semiconductor`, `custom` | `?mode=bio` \| `?mode=semicon` \| `?mode=both` |
| `optiflow-anomaly-pipeline-embed.html` | `semiconductor` signature | — (self-contained, loops) |
| `optiflow-pipeline-demo.html` | legacy | — |
| `optiflow-product-window.html` | legacy | — |
| `optiflow-build-workflow.html` | legacy | — |

`about.html`, `research.html`, `research-output.html` use **no iframe embeds** — their foot scripts are trimmed to nav-scroll + drawer + reveal observer only.

### Assets

- **Brand:** `favicon.svg`, pixel-grid logo mark (inline SVG in nav/footer/drawer).
- **Mission graphic:** `mission_arch.png` — ships with `index.html` and `about.html`.
- **Founder photo:** `DSC_0167__6_in_x_8_in__square_resized.jpg` — ships with `about.html`. Square, 1000×1000, ~41 KB.
- **CytoByte microscopy:** `cytobyte-dic.png`, `cytobyte-virtual-nuclei.png`, `cytobyte-ar-overlay.png`.
- **Anomaly-pipeline embed — ship all six alongside the embed HTML:**
  `ap-sem.jpg`, `ap-detected.png`, `ap-instances.png`, `ap-scatter.png`, `ap-matrix.png`, `ap-collage.jpg`.

---

## Build & QA workflow

**Proposal before build:** present a structural proposal and get approval before any significant build. Large pages are reviewed section-by-section.

**All HTML/copy edits via assertion-guarded Python:**
```python
def rep(s, old, new, label, n=1):
    assert s.count(old) == n, f"[{label}] expected {n}, found {s.count(old)}"
    return s.replace(old, new)
```
After edits: re-grep for the old string to confirm it's gone, then re-run the guardrail sweep.

**QA every page with Playwright/Chromium** (`/opt/pw-browsers`, `--no-sandbox --disable-setuid-sandbox`):
- Horizontal-overflow sweep at **360, 390, 414, 768, 1024, 1280, 1440, 1920** — assert `scrollWidth ≤ clientWidth`. Zero overflow is a hard requirement.
- Per-section 2× DPR screenshots for visual review. Full-page 2× shots exceed the view limit — screenshot per-section or downscale first.
- If screenshots render blank: verify via pixel sampling (sample against navy `#101F38`).
- For embeds: scroll into view, wait for lazy-load + postMessage height, assert iframe got an explicit height and the loader is hidden.

**Deliverables via `present_files`** — Claude never commits to GitHub directly. Re-present only changed files.

---

## The iframe height contract

Embeds are lazy-loaded and self-size via `postMessage`. To add an embed:

**Markup:**
```html
<div class="demo-loading" id="ld-NAME"><div class="spinner"></div><span>Preparing live demo&hellip;</span></div>
<iframe class="demo-frame" id="demo-NAME" data-src="EMBED-FILE.html" title="…" loading="lazy" scrolling="no"></iframe>
```

**Register in the foot script `frameMap`:**
```js
var frameMap = {
  'optiflow-workflow-from-image-embed.html': {el:document.getElementById('demo-wfi'), loader:document.getElementById('ld-wfi')},
  'optiflow-anomaly-pipeline-embed.html':    {el:document.getElementById('demo-anomaly'), loader:document.getElementById('ld-anomaly')}
};
```

**Mechanism:** an `IntersectionObserver` (rootMargin `400px`) sets `iframe.src = data-src` when near-viewport. The embed posts `{optiflowEmbedHeight: H}` on load/resize. The handler matches by `contentWindow` (query string irrelevant — `?mode=both` works), sets `iframe.style.height`, `aspectRatio:'auto'`, hides the loader. Accepts `optiflowEmbedHeight` | `optiflowWindowHeight` | `height`.

---

## The anomaly-pipeline embed

Self-contained, looping, dependency-free. Seven cross-faded stages: `Image → Detect → Segment → Characterise → Gate → Trace back → Review`. Responsive (stacks ≤680px), respects `prefers-reduced-motion`, posts its own height.

**Ships with six assets in the same directory:** `ap-sem.jpg`, `ap-detected.png`, `ap-instances.png`, `ap-scatter.png`, `ap-matrix.png`, `ap-collage.jpg`.

**Regenerating assets** (if source data changes): founder holds originals — `1__SEM_original.jpg`, `2__connectorsDetected.png`, `3__individualConnectors_IDed.png`, `4__feature_matrix.xlsx`, `6__suspectConnectors.jpg`. The generator optimises the SEM, recolours detect/instance masks, runs PCA → 2D scatter (re-rendered from the matrix for brand control), renders the heatmap, extracts 20 box coordinates, crops the strong-suspect collage.

---

## research.html — final state

**Rebuilt onto the canonical design system.** Purpose: convert academic rigour into commercial confidence for any reader — commercial buyer, investor, collaborator, or competitor. Proof-axis framing (not domain-axis); bio/semicon given equal weight.

**Section flow:**

1. **Hero** — eyebrow: "Research & Recognition". H1: "Grounded in peer-reviewed research. / *Hardened in production.*" Sub: domain-independent framing ("wherever an image holds an answer, the same rigour applies"). CTAs: **Book a Demo** / **See the full record** (→ `research-output.html`).
2. **Proof bar** — canonical 4 points.
3. **A decade of evidence** (by the numbers) — `20+` publications · `1,200+` citations · `10+` years · `15+` imaging modalities. Framed as evidence, not vanity.
4. **What the research proves** — 4 domain-agnostic capability cards (the translation layer — the heart of the page): *Domain-informed models beat generic ones* · *Answers without labels or markers* · *Find the anomaly with no template* · *Accuracy that still runs at line speed*. Each states the result in buyer-legible terms with the published proof underneath.
5. **Two kinds of proof** — two equal tracks: *Validated in peer review* (4 curated publication cards, teal accent) + *Hardened in production* (4 deployed-system cards, gold accent). Bio and semiconductor given equal visual weight. "Non-destructive testing" removed — delayering is destructive; track B card reads "Reference-free wafer defect detection" only.
6. **Recognition** — 3 flagship press items only (CNA documentary 2019, Straits Times 2021, LabelFlow/AI Stories 2022). Full list on the record page.
7. **Bridge to the full record** — confident panel: "This is the highlight reel." → `research-output.html`.
8. **CTA** — "See whether it applies to your images." + Book a Demo / Talk to us first + 4-proof strip.

**Key editorial decisions:**
- Proof-axis over domain-axis: replaces the old bio/semicon column split which read bio-first.
- Domain-agnostic translation layer (§4) is new — makes the page work for any field.
- Citation count: `1,200+` (Scholar: 1,242 all-time; conservative, permanently true).
- `"state-of-the-art"` banned → expressed through concrete results.
- Eyebrow iterated: "Research & Evidence" → "Research & Proof" → **"Research & Recognition"** (final).
- QA: zero overflow 360→1920; reveal observer and all responsive breakpoints verified.

---

## research-output.html — final state

**Rebuilt onto the canonical design system.** Purpose: the complete, verifiable bibliographic record for academics, diligence reviewers, and investors.

**Section flow:**

1. **Hero** — eyebrow: "The full record". H1: "The complete / *research record.*" CTAs: **Book a Demo** / **Back to research overview**.
2. **Proof bar** — canonical 4 points.
3. **Peer-reviewed publications** — 15 papers listed (all with DOI links, plus one in-preparation manuscript) with working **theme filter** (All / AI & machine learning / Nuclear mechanics / Cell mechanics / Label-free imaging / In preparation). Filterable by tag, JS-powered, no reload.
4. **Collaborations** — 10 items split: Industry & commercial (C1–C4, including ETH Zürich deployment) + Academic research (C5–C10). Industrial/semiconductor projects listed without institutional attribution where confidentiality applies.
5. **Conference participation** — 6 international conferences (Singapore and Europe, 2015–2019).
6. **Media & press** — 10 items in full (CNA, Straits Times, NUS News, Newswise, CGTN, LabelFlow/AI Stories, L'express, TNE Magazine, Lianhe Zaobao, TopFM).
7. **Book chapter** — Elsevier *Mechanobiology in Health and Disease*, 2018.
8. **CTA** — "Put this track record to work on your images." + Book a Demo / Back to research overview.

**DOI audit (completed this session) — 3 errors found and corrected:**

| Pub | Error | Corrected to |
|---|---|---|
| Jiang et al., *Advanced Science* 2023 | Wrong DOI suffix `202301963` + wrong subdomain | `advanced.onlinelibrary.wiley.com/doi/full/10.1002/advs.202201663` |
| Jokhun et al., *Biophysical Journal* 2018 (actin/telomeres) | Wrong PII `30978-2` | `S0006-3495(18)30983-4` |
| Radhakrishnan et al., *Biophysical Journal* 2017 (nuclear positioning) | Wrong PII `30348-4` | `S0006-3495(17)30344-2` |

Also corrected in the previous session: Venkatachalapathy et al. 2021 was wrongly labelled *Communications Biology* — correct journal is **Scientific Reports 11, 23041**, DOI `10.1038/s41598-021-02441-6`.

All remaining 12 publication URLs confirmed correct against source.

**`pseudo-DAPI` retained** in the manuscript-in-preparation title ("Augmented reality microscopy: label-free pseudo-DAPI nuclear staining from DIC images…") — this is a proper name, not body copy. Do not alter.

Cross-page overlap eliminated: full Collaborations and Media lists live only on this page; `research.html` shows curated highlights only.

---

## about.html — final state

Rebuilt on the biomedical skeleton (canonical head/tokens/nav/drawer/footer/scripts), full editorial pass. Section flow:

1. **Hero** — "Born in a research lab. / *Proven in production.* / Built for any field that runs on images."
2. **Proof bar** — canonical 4 points.
3. **Why we exist** — productisation thesis: "Your expertise is the scarce resource." + 3-item from→to shift row.
4. **Mission & Vision** (`id="vision"` — home links here) — `mission_arch.png` + mission quote + gold tagline; vision "Eliminate the busywork. / *Amplify the expert.*" + 3 agentic chips.
5. **The journey** — vertical timeline (2019 / 2021 / 2023 / Today — gold node).
6. **What sets us apart** — gold ig-panel, 2×2: Domain-aware · Auditable by design · Yours, and local · We build what doesn't exist.
7. **Who we're for** — 3 equal vertical cards.
8. **The founder** — "From fundamental research to productised enterprise deployment." Photo + **Dr. Doorgesh Sharma Jokhun**. See below.
9. **CTA** — "Bring us your images." + 4-proof strip.

**Founder section — final bio (reflects actual career trajectory):**

- **Career sequence:** PhD at NUS (computational and biomedical imaging) → postdoc at NUS → moved into industry in semiconductor image analytics → founded Logic Byte. Bio reflects this sequential trajectory — the transition from research to semiconductor production is what gives OptiFlow its unusual breadth.
- **Para 1:** "Doorgesh completed his PhD and postdoctoral research at NUS in computational and biomedical imaging — spanning autonomous microscope control, biosensor CNN development, in-silico (virtual) nuclear staining and large-scale single-cell analysis — resulting in **more than twenty peer-reviewed publications**, cited more than 1,200 times…"
- **Para 2:** "He then moved into industry, working directly in **high-precision semiconductor image analytics** — where measurement accuracy, throughput and production reliability are non-negotiable. That trajectory — from fundamental research and biomedical imaging through to semiconductor production — is rare…"
- **Credential chips (10):** PhD · NUS · 20+ Publications · 1,200+ Citations · Computer Vision · Deep Learning · Biomedical Imaging · Autonomous Microscopy · Virtual Staining · Semiconductor Inspection · Signal Processing.
- **Links:** email (plain text) · LinkedIn · Google Scholar · Digital Card.

**Founder photo treatment:** `object-fit:cover`, `object-position:50% top`, absolute-fill inside a `minmax(280px,360px)` column. `align-self:start; min-height:450px`. Lower-edge bleed via `::after` pseudo-element. Mobile (≤900px): stacks full-width, capped at 460px, `aspect-ratio:4/5`. `<img>` intrinsics: `width="1000" height="1000"`.

**Optional, high-value:** ETH Zürich attributed testimonial — never fabricated; slot between proof bar and "What sets us apart" when available.

---

## custom.html — final state

Rebuilt on biomedical skeleton. Section flow:

1. **Hero** — "Your imaging challenge. / Our starting point."
2. **Proof bar** — one chip: "From microscopy to satellite imagery."
3. **Build-versus-buy gap** — 3 cards.
4. **Fields we work across** — data-types modbar + 9 domain cards (3×3) + catch-all band. Nine: Aerial/drone/remote-sensing · Earth-observation/space · Defence/security/sovereign · Robotics/autonomy/ADAS · Materials/metallurgy · Construction/built-environment · Marine/subsea/environmental · Food/agriculture/natural-products · **Energy/mining/resources**. (Clinical removed; Energy/resources added.)
5. **How we build** — gold-accented 4-step flow + ETH Zürich proof badge.
6. **Capabilities** — domain-agnostic toolkit.
7. **Integrity** — 3 pillars + `?mode=both` embed.
8. **From research to production** — 3 proofs, leads with reference-free defect result.
9. **Ways to engage** — 3 engagement models (de-priced).
10. **CTA**.

---

## contact.html — final state

Conversion endpoint — every CTA on the site routes here (`?intent=demo|project|hello|other`).

**Structure:** hero → proof bar → form + rail → footer. No separate closing CTA (the page is the CTA).

- **Hero:** "Let's talk about *what your images can tell you.*" Welcomes all verticals + investors/collaborators.
- **Form:** intent chips (pre-filled by `?intent=`), single-column fields: Name* / Work email* / Company / Field or interest (dropdown: Biomedical, Semiconductor, Materials, Pharma, Energy/Mining, Defence, "Another imaging domain", "Investor/partner/press") / Subject* / Message* + dataset hint. Invisible honeypot (`_gotcha`).
- **Rail:** "A person reads every message" (not "the founder" — avoids spam/expectation issues); 1-2-3 next steps; `hello@logicbyte.ai` plain text + LinkedIn.
- **Back-end:** Formspree `f/mzdyjayk`. `?intent=` routing preserved exactly. `aria-invalid` validation; success panel on submit.

---

## Design system (tokens shared across all pages)

```
Navy        #0B1628   navy-2 #0E1B30   navy-3 #101F38   panel #10203A   panel-2 #13243F
Teal        #1DB89A   teal-bright #22D3AC   teal-soft rgba(29,184,154,.12)
Gold        #D4AF37
Text        #E8EDF4   muted #92A2B8   muted-2 #6E7F96
Border      rgba(255,255,255,.10)   border-2 rgba(255,255,255,.07)
Radius      14–18px   min font 10px (0.625rem)
```

**Fonts (Google Fonts):** Syne 600/700/800 (wordmark/display) · Outfit 400/500/600/700 (UI/headings) · DM Mono 400/500 (labels/mono) · DM Sans 300–600 (body).

**Shared structure on all canonical pages:** sticky nav + `has-menu` dropdown + mobile drawer (`aria-expanded`), hero (`hero-grid-bg` + glow), spec/proof bar (`.specbar`), reveal-on-scroll (`IntersectionObserver`, threshold 0.12), footer with `footer-cols`. `about`, `research`, `research-output` omit the iframe/slider machinery.

---

## Copy & brand guardrails

- **British English** throughout.
- **"ETH Zürich"** — always with the umlaut (HTML entity `Z&uuml;rich` or literal `Zürich`).
- **No fabricated metrics.** Real published figures are fine (e.g. APL 2021: 95% accuracy, <35 min).
- **No pricing anywhere on the site.** Verbal only.
- **No version numbers** — use "New" / "Expanded" tags.
- **No `mailto:` links** — email as plain text only; actions route to `contact.html`.
- **Windows-only** — no macOS claims.
- **No "co-pilot"** (Microsoft association).
- **No "state-of-the-art"** → "the latest advances in AI and computer vision."
- **No "science"** in body copy where audience includes engineers/technicians.
- **No "pseudo-DAPI"** in copy → "virtual nuclear stain" / "virtual staining". **Exception: manuscript titles only** — one instance in `research-output.html`, intentional, do not alter.
- **No "non-destructive testing" / "NDT"** for semiconductor work where delayering is required — it is destructive.
- **CytoByte** — engine brand (no "CBV" acronym).
- **"domain-aware"** — canonical positioning term.
- **"Semiconductor & Industrial Imaging"** — canonical vertical name.
- **Three verticals treated as equal** in all copy and layout.
- **Minimum font size 10px (0.625rem)** site-wide.
- **No facial recognition / emotion measurement** as named sectors.

### Public-safe proof points
In production at **ETH Zürich** · Ongoing trials at **NTU** · **20+** peer-reviewed publications · Featured by **CNA & The Straits Times**

### Internal-only — never on the site
NiCE · CHA · Prof. Gan Chee Lip · Borries · MIT Semiconductor · all pricing / revenue figures

---

## Deploy

1. Commit to GitHub → Vercel auto-deploys from repo root.
2. All embed assets must sit in the repo root alongside the HTML. `about.html` requires `mission_arch.png` + `DSC_0167__6_in_x_8_in__square_resized.jpg`. Semiconductor embed requires all six `ap-*` assets.
3. **Claude never commits directly** — deliverables handed over as files for the founder to commit.

---

## Open items

- **ETH Zürich testimonial** — high-value addition to `about.html` when a real attributed quote is available.
- **Micro-label fonts** — a few inherited labels (`.rsr-label`, `.tag-new`, `.ba-tag`) on the older canonical pages sit marginally below 10px. Decide whether to bump site-wide.
- **Reconstruct the `unsupervisedAnomalyDetection` animation** — Python source in `sample_data/unsupervisedAnomalyDetection/single_part_ana.py`.
