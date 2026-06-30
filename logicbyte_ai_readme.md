# Logic Byte — Website (`logicbyte_ai`)

Marketing site for **Logic Byte Pte. Ltd.** (Singapore deep-tech, incorporated 2023). Flagship product **OptiFlow** — a modular, domain-aware, no-code visual workflow builder for image analytics. Engine for virtual staining: **CytoByte** (biomedical).

- **Live:** https://logicbyte.ai
- **Stack:** Static HTML/CSS/JS — no framework, no build step. Deployed on **Vercel** from this **GitHub** repo. DNS on **Namecheap**. Indexing via **Google Search Console**.
- **Three equal verticals:** Biomedical & Life Sciences · Semiconductor & Industrial Imaging · Custom Solutions. *Treat them as equals everywhere.*

> This README reflects the site state at the end of the semiconductor-page build (latest session). It supersedes earlier copies.

---

## Repository layout

### Pages
| File | Status | Notes |
|---|---|---|
| `index.html` | ✅ Locked | Home / verticals hub |
| `platform.html` | ✅ Locked | Full OptiFlow platform |
| `biomedical.html` | ✅ Locked | **Design-system reference template** (1,211 lines). `mailto:` removed (latest session). |
| `semiconductor.html` | ✅ **Complete & publication-ready** | Deep-specialisation page. Animated reference-free anomaly-detection embed in the signature section. |
| `custom.html` | ⏳ **To build next** | Bespoke / any-domain vertical |
| `about.html` | ✅ | Incorporation year corrected to **2023** |
| `research.html` | ✅ | Research record |
| `contact.html` | ✅ | All CTAs route here (`?intent=hello` variant for "say hello") |

### Demo embeds (loaded as lazy iframes)
| File | Used by | Modes |
|---|---|---|
| `optiflow-workflow-from-image-embed.html` | integrity sections | `?mode=bio` \| `?mode=semicon` \| `?mode=both` |
| `optiflow-anomaly-pipeline-embed.html` | **semiconductor** signature | — (self-contained, loops) |
| `optiflow-pipeline-demo.html` | (legacy/other) | — |
| `optiflow-product-window.html` | (legacy/other) | — |
| `optiflow-build-workflow.html` | (legacy/other) | — |

### Assets
- **Brand:** `favicon.svg`, pixel-grid logo mark (inline SVG in nav/footer/drawer), `arch_teal.png` (index mission graphic — must ship with `index.html`).
- **CytoByte microscopy (biomedical):** `cytobyte-dic.png`, `cytobyte-virtual-nuclei.png`, `cytobyte-ar-overlay.png`.
- **Anomaly-pipeline embed (semiconductor) — ship all six alongside the embed:**
  `ap-sem.jpg`, `ap-detected.png`, `ap-instances.png`, `ap-scatter.png`, `ap-matrix.png`, `ap-collage.jpg`.
  *(Derived from the founder's real EM pipeline data; see Handover for regeneration.)*

---

## Design system (tokens shared across pages)

```
Navy        #0B1628   navy-2 #0E1B30   navy-3 #101F38   panel #10203A
Teal        #1DB89A   teal-bright #22D3AC   teal-soft rgba(29,184,154,.12)
Gold        #D4AF37
Orange      #F5A623   Red #EF3B2D
Text        #E8EDF4   muted #92A2B8   muted-2 #6E7F96
Radius      14–18px   min font 10px (0.625rem)
```
**Fonts (Google Fonts):** Syne (display weights), Outfit (UI/headings), DM Mono (mono/labels), DM Sans (body).

**Shared structure on every page:** sticky nav + mobile drawer, hero (grid-bg + glow), spec/proof bar, reveal-on-scroll observer, before/after slider component (`.ba`), lazy-iframe + `postMessage` height contract, footer.

---

## Copy & brand guardrails (non-negotiable)

- **British English** throughout.
- **"ETH Zürich"** — always with the umlaut.
- **No fabricated metrics.** No invented %, ×, or accuracy figures.
- **No pricing anywhere on the site** (pricing is internal/verbal only).
- **No version numbers** — use **"New" / "Expanded"** tags instead.
- **No `mailto:` links** anywhere — email shown as plain text; actions route to `contact.html`.
- **Windows-only** — no macOS claims.
- **No "co-pilot"** (Microsoft association); **no "pseudo-DAPI"** → use **"virtual nuclear stain" / "virtual staining"**.
- **CytoByte** is the engine brand (no "CBV" acronym).
- Canonical vertical name: **"Semiconductor & Industrial Imaging."**
- Positioning term used consistently: **"domain-aware."** Prefer **"auditable."** Use **"texture analysis"** (not "texture quantification").
- **Three verticals treated as equal.**
- Minimum font size **10px (0.625rem)**.

### Proof points
- **Public-safe (site-approved):** In production at **ETH Zürich** · Ongoing trials at **NTU** · **20+** peer-reviewed publications · Featured by **CNA & The Straits Times**.
- **Internal-only — never on the site:** NiCE, CHA, Prof. Gan Chee Lip, Borries, MIT Semiconductor, and all pricing/revenue.

---

## Deploy

1. Commit to GitHub → Vercel auto-deploys.
2. New embeds + their assets must sit in the repo root alongside the HTML pages.
3. **Claude never commits directly** — deliverables are handed over as files for the founder to commit.

### Known site-wide tasks (open)
- **Google Search Console indexing:** add `www → non-www` redirect via `vercel.json`; replace every `href="index.html"` with `href="/"` site-wide.
- **Micro-label fonts:** three inherited classes sit marginally < 10px (`.rsr-label` 9.9px, `.tag-new` 9.6px, `.ba-tag` 9.3px). Kept verbatim from the locked design system for cross-page consistency — decide whether to bump site-wide.

---

## Living docs
- `logicbyte_ai_readme.md` — this file.
- `LogicByte_Website_Handover.md` — operational handover (build workflow, embed contract, custom-page playbook, open items).
