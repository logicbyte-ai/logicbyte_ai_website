# Logic Byte Website — Handover Brief

*Upload this file at the start of a new Claude conversation to resume work on the site. Last updated: 16 Jun 2026 — **`biomedical.html` built & delivered**. Recommended next page: **`semiconductor.html`** (build in a new conversation; the full template is locked — see `LogicByte_Website_Handover.md` §7.3b).*

---

## Project overview

**Company:** Logic Byte Pte. Ltd. (Singapore, inc. 2023)  
**Founder (public-facing):** Dr. Doorgesh Sharma Jokhun, PhD (NUS) · Lead AI Engineer (Computer Vision), Borries Pte. Ltd.  
**Personal links:** LinkedIn: linkedin.com/in/dsjokhun | Google Scholar: Sa4nFlYAAAAJ | Blinq: blinq.me/uSAjvpnbgGvk?bs=db | d.s.jokhun@logicbyte.ai | hello@logicbyte.ai  
**Company LinkedIn:** linkedin.com/company/logicbyte-ai  
**Site:** logicbyte.ai

**Product:** OptiFlow — modular, modality-agnostic, domain-aware, no-code visual workflow builder for image analytics. Targets domain experts who need reproducible, auditable pipelines without a dedicated programming team.

**Key module:** CytoByte — label-free in-silico virtual nuclear staining from DIC or phase contrast (no dyes, no fixation, non-sacrificial). Output called "virtual nuclei" / "virtual nuclear stain" — **never "pseudo-DAPI"** (generates unwanted DAPI comparisons). The process is "virtual staining" vs "chemical (dye-based) staining". Deployed commercially at ETH Zürich. Academic manuscript in preparation.

**Primary verticals:** Biomedical & Life Sciences · Semiconductor & Industrial Imaging · Custom Solutions (three equal peers — none dominates).

**Deployment:** Static HTML → Vercel at `logicbyte.ai` (Namecheap domain/DNS, GitHub repository). No build step. Deploy by pushing all files to the GitHub repo root; Vercel picks up automatically.

---

## Files in the project

### Pages — all must sit in the root

| File | Purpose |
|---|---|
| `index.html` | Homepage — Hero → proof bar → Problem → See it in action → Platform (snapshot) → Verticals → Proven & Trusted → How we work → Vision → Mission/CTA |
| `platform.html` | **The platform / product home — ✅ BUILT.** Hero → spec bar → architecture → workflow builder (bespoke fork-and-merge DAG figure, not an iframe) → module library → integrity by design (+ workflow-from-image demo, left-aligned) → deployment & integration → how-we-work (brief) → CTA with proof anchor. Now a second reference page. Full as-built record in `LogicByte_Website_Handover.md` §7.1. |
| `about.html` | Company story + Founder section with photo, email, LinkedIn, Scholar, Blinq |
| `biomedical.html` | **✅ BUILT (16 Jun 2026).** Biomedical & Life Sciences — 11-section rebuild on the platform.html design system. Hero → proof bar → analysis gap → who we serve (5 sub-sectors + custom card) → label-free signature (CytoByte slider) → capabilities → integrity/reproducibility + workflow-from-image demo → grounded in research → how we work → CTA → footer. See `LogicByte_Website_Handover.md` §7.3b for full as-built record. |
| `semiconductor.html` | Semiconductor & Industrial Imaging — 3 segments, SEM/STEM proof, traceability callout, sticky right rail |
| `custom.html` | Custom Solutions — 3 engagement types, capabilities, sticky right rail |
| `research.html` | Research overview — domain columns, selected collaborations, press coverage, sticky right rail |
| `research-output.html` | Full scientific record — C1–C10 collaborations, P1–P6 conferences, M1–M10 media, 16 publications, book chapter, sticky right rail |
| `contact.html` | Contact — intent cards (Book a Demo / Say Hello), form with subject + domain fields. `?intent=hello` query param adjusts page context. |

### Demo embeds — also in root, loaded as iframes from index.html

| File | Role in index.html |
|---|---|
| `optiflow-window-embed.html` | Hero right column — static workflow builder visual. Has internal `fit()` + `transform:scale` that renders at 1060px and scales to the iframe width. CSS `aspect-ratio` matches the scaled height so the parent needs no JS sizing. |
| `optiflow-pipeline-demo-embed.html` | "See it in action" right column — animated pipeline demo, cycles Biomedical ↔ Semiconductor. Fixed title "OptiFlow — Pipeline in Action". Biomedical/Semiconductor toggle tabs at bottom. |
| `optiflow-workflow-from-image-embed.html` | "Drop in a result, get the workflow back" demo. Wired into `platform.html` (Integrity section) and `biomedical.html` (Integrity section, `?mode=bio`). **Updated 16 Jun 2026:** (a) accepts `?mode=bio\|semicon\|both` — biomedical uses `?mode=bio`; semiconductor should use `?mode=semicon`; platform uses no param (both scenes). (b) Respects `prefers-reduced-motion`: renders a static completed state rather than animating. |

**Retired (do not deploy):** `optiflow-build-workflow.html`

### Supporting assets — in root

| File | Purpose |
|---|---|
| `cytobyte-dic.png` | 512×512 label-free DIC microscopy image — base layer of the CytoByte before/after slider on `biomedical.html`. Public-safe; no patient/client-confidential data. |
| `cytobyte-virtual-nuclei.png` | 512×512 CytoByte virtual nuclear stain output of the same field (white nuclei on black). Top layer of the slider; DIC vs this pairing is the dramatic contrast used. |
| `cytobyte-ar-overlay.png` | 512×512 live cyan AR overlay on the DIC feed — same field, shows the real-time AR view of the virtual stain on the microscope. Used as a small inline thumbnail (88×88, float-right) next to the "Real-time virtual staining" value point on `biomedical.html`. |
| `favicon.svg` | Gold pixel-grid mark on navy, 4 black / 4 white inner squares |
| `logo.svg` | Standalone logo (not used in pages — logo is inline SVG in each nav/footer) |
| `sitemap.xml` | XML sitemap for search engine indexing |
| `robots.txt` | Permits all crawlers, references sitemap |
| `DSC_0167__6_in_x_8_in__square_resized.jpg` | Founder photo (white background headshot) |
| `hero_m_bio.jpg` | Mobile hero composite — Biomedical before/after (848×420, loaded via JS `matchMedia`) |
| `hero_m_semi.jpg` | Mobile hero composite — Semiconductor before/after (848×420, loaded via JS `matchMedia`) |
| `mission_arch.png` | Mission section "arch" graphic (1100×906 RGBA, pngquant'd ≈308 KB) — **transparent background**, plain `<img>` (no `<picture>` — WebP saves only 15 KB, not worth the complexity). Composites seamlessly onto the navy section. Generated from `missionStatement.pptx`. **Must ship in the repo root.** Supersedes `arch_teal.png` (retired). |

---

## Design system

**Fonts (Google Fonts — loaded at runtime):**

| Font | Used for |
|---|---|
| Syne | Wordmark and nav links |
| Outfit | Display headings on secondary pages (h2, h3) |
| DM Mono | Homepage hero h1, eyebrows, taglines |
| DM Sans | Body text throughout |

*Note: Google Fonts do not load in Playwright/bash environments. System font fallbacks render with correct layout and brand colours — acceptable for QA screenshots.*

**Colours:**

| Name | Hex | Use |
|---|---|---|
| Navy | `#0B1628` | Background |
| Teal | `#1DB89A` | Primary accent, CTA buttons |
| Gold | `#D4AF37` | Wordmark, logo mark |

**Logo:** Inline SVG geometric pixel-grid mark embedded in every `<nav>` and `<footer>`. 4 black inner squares, 4 white (`#fefefe`) inner squares — binary pattern. Not an external image reference.

**Minimum font size:** 10px (0.625rem) everywhere, no exceptions.

**Responsive layout (index.html — rebuilt):** Hero and "See it in action" use a **fluid flex layout** (no fixed column breakpoint): the text column shrinks faster than the demo (`flex:0 1.6 610px` vs `flex:0 1 810px`), the inter-column gap caps at ~83px and floors at 32px, and the demo window **shrinks monotonically — no size jumps**. Both stack to a **single column at ≤1000px** (fired just before the hero eyebrow "AI-Powered Image Analytics" (288px) would wrap). At the switch, `flex:none` is set on the columns so the width-axis `flex-basis` is **not** read as a height (this was the cause of large dead vertical space); the window/demo is **held at its pre-switch width** (560px hero / 531px demo), **left-aligned**, and squeezes down as the viewport narrows. **Content capped at 1500px** (raised from 1600 to keep the hero gap tight; align secondary pages on rebuild). The hero headline font (`--h1: clamp(1.7rem, calc(3.8vw - 1rem), 2.9rem)`) shrinks on a steep curve to hold the **3-line** headline down to ~1100px (4 lines only in the narrow 1001–1075px band); single-column restores a larger `--h1`. Finer mobile tuning at ≤640px.

**Secondary pages (with sticky rail):** `.page-shell` grid (`1fr var(--col-nav)`) capped at `max-width: 1600px; margin: auto` so the entire grid — content and rail — centres together on large monitors. Rail hides at ≤820px.

---

## Copy guardrails — non-negotiable

- **British English** throughout — colour, normalisation, modality, behaviour, artefact, etc.
- **"ETH Zürich"** — umlaut always required. Never "ETH Zurich".
- **No fabricated metrics** — no placeholder stats (e.g. "99.9% accuracy", "10× faster") without a verifiable source. Remove them; do not replace with different numbers.
- **No "research-grade"** — unprofessional; prohibited.
- **No "co-pilot"** — too Microsoft-associated; prohibited.
- **Pricing is internal only** — no specific figures on the site or in decks. Consistent with competitor norms in scientific imaging software.
- **No OptiFlow version numbers on the site** (e.g. "v3.2.1") — rapid releases would date the site. Use "New"/"Expanded" for recency, never a number.
- **Desktop app is Windows-only — macOS is NOT supported.** Never claim macOS.
- **"license" (verb) vs "licence" (noun)** — British English distinguishes them; mind it.
- **"Auditable" preferred over "reproducible" alone** — reinforces the traceability story directly.
- **OptiFlow is a badge, not a heading** — styled inline (`.optiflow-badge`), never used as an H1 or H2.
- **Real images only** — no synthetic SVG imagery in public-facing demo assets.
- **Three verticals are equal peers** — Biomedical & Life Sciences, Semiconductor & Industrial Imaging, Custom Solutions. None dominates or leads.
- **Vertical name confirmed:** "Semiconductor & Industrial Imaging" — used consistently on the site and LinkedIn.
- **"Not automation for its own sake — intelligence in service of expertise"** — the preferred framing. Avoid language that implies replacement of the domain expert.
- **NTU is now public-safe as a proof point** — usable as "Ongoing trials at NTU" (founder-approved, 15 Jun 2026). **Borries, MIT Semiconductor, NTU CHA, and Prof. Gan Chee Lip remain internal only.** Texture analysis is a tested capability shipping before launch — OK to show.
- **Heading pattern:** section headings are two short fragments in sentence case, the second fragment set in teal (`<em>`); **eyebrows** are DM Mono, uppercase, letter-spaced, prefixed by a short rule.
- **"Pseudo-DAPI" is banned** — use "virtual nuclear stain" / "virtual nuclei" for the output; "virtual staining" for the process (vs "chemical (dye-based) staining"). CytoByte is the engine brand name. No "CBV" acronym.
- **Tone:** declarative and confident, not invitational. Short punchy headlines. Semi-formal for known contacts.

---

## iframe demo architecture

All three demo embeds use a **postMessage height protocol** to size their parent iframes. This is required because `file://` iframes are cross-origin (origin "null"), which blocks the parent from reading `contentWindow.document` via JS. postMessage works in both local `file://` testing and on the deployed same-origin site.

Each embed runs:
```js
function rh() {
  var wrap = document.querySelector('.wrap');
  var h = wrap ? Math.ceil(wrap.getBoundingClientRect().bottom) + 6 : document.body.scrollHeight;
  parent.postMessage({ optiflowEmbedHeight: h, optiflowEmbedWidth: window.innerWidth }, '*');
}
// Called on: load, resize, ResizeObserver, and at [200, 600, 1200, 2000, 3000, 4500, 6500, 9000]ms
```

`index.html` listens and sizes the matching iframe grow-only (resets on width change):
```js
window.addEventListener('message', function(e) { ... });
```

**Hero window exception:** Self-sizes via internal `fit()` + CSS `aspect-ratio`. No postMessage needed.

---

## Screenshot / QA workflow

```bash
# Playwright against local file:/// paths
python3 script.py  # uses playwright.sync_api, --no-sandbox flag
# Output files → /mnt/user-data/outputs/
```

Claude-in-Chrome `save_to_disk` captures return an ID but are not accessible from the bash filesystem. Use Playwright for downloadable QA screenshots.

Audit after changes: check for horizontal overflow at 1280px and 1920px, no fonts below 10px, no "ETH Zurich" (without umlaut).

---

## Current status (June 2026)

**Live at:** logicbyte.ai (Vercel)

### Completed website work
- **`biomedical.html` built, QA'd (zero overflow 360–1920px) & delivered** (16 Jun 2026). Full as-built record in `LogicByte_Website_Handover.md` §7.3b.
- **`platform.html` built, QA'd (zero overflow 360–1920px) & delivered** (15 Jun 2026). Full as-built record in `LogicByte_Website_Handover.md` §7.1.
- **Homepage fully rebuilt** (multi-session). New narrative flow: Hero → proof bar → Problem → See it in action → Platform (snapshot) → Verticals → Proven & Trusted → How we work → Vision → Mission/CTA.
- Hero & "See it in action" rebuilt as **fluid, jump-free** responsive layouts (window shrinks monotonically; single-column hold at the 1000px switch; no dead vertical space). Verified no horizontal overflow 375–1920px.
- Homepage copy refreshed throughout:
  - **Problem** section (eyebrow "The problem"): four loss-framed cards mapping 1:1 to the platform pillars — *Experts stuck in the weeds · Results that can't be defended · Everything waits on one person · Generic AI breaks on domain images.*
  - **See it in action** → eyebrow "OptiFlow in action"; output "auditable and reproducible by anyone with access, on any machine".
  - **Platform** → eyebrow "The architecture"; lead notes it is "a snapshot of what's inside"; prominent "Explore the full platform" CTA after the lead; pillars = No-code workflow builder · Domain-aware AI · Built for handoff · Integrity by design + "The library. Use only what you need."
  - **Verticals** heading → "Deep expertise. Built for any field." Semiconductor card capabilities updated to **hardware assurance / IC-trojan detection / texture analysis / reference comparison** (NiCE/CHA-aligned; MIT material removed).
  - **Proven & trusted** heading → "Grounded in research. Hardened in production." — section **moved to directly after the verticals** (trust precedes the commercial/how-we-work section).
  - **How we work** → "Talk to us" contact CTA added after the value strip.
  - **Vision** reframed to avoid any "replacing the expert" reading → "Today, you build it. Tomorrow, it builds itself." (OptiFlow automates the *building*; the expert is freed for higher-level domain work).
  - Proof bar item → "Imaging modality-agnostic".
  - **Mission section** rebuilt: the "OUR MISSION" eyebrow is now a **top-left section header** (teal rule prefix), consistent with every other section — previously it was buried inside the right text column. Below it, a two-column row: **arch graphic left · mission quote + tagline right** (vertically centred), then the **full-width closing CTA banner**. The graphic is `mission_arch.png` (plain `<img>`) — the wireframe arch from `missionStatement.pptx` with teal "Domain Experts" / gold "Imaging Insights" labels, gold pixel-grid logo mark + "Logic Byte", white arch labels. The slide background was exactly `#0B1628` (brand navy), so it was **knocked out to a true transparent alpha** (soft luminance key) — this removed the hard black box that made the old `arch_teal.png` look like a pasted-in screenshot. **Width fix:** the `.mission .wrap{max-width:1080px}` cap was removed so the section aligns to the page's 1500px frame like every other section (it previously floated narrow and centred on wide monitors); the row is capped at 1180px and left-aligned, the CTA spans full width — all sharing the page's left margin. Stacks to a single column ≤1000px with **all items left-aligned** (`.mission-row{align-items:flex-start}` in the breakpoint). **Tagline sizing:** `.mission-statement{max-width:552px}` is the exact measured natural single-line width of the tagline in DM Mono at 18.4px (49 chars). `white-space:nowrap` on `.mission-tagline` holds it on one line at ≥1250px viewport (where ≥552px of flex space is available); `@media(max-width:1249px)` removes `nowrap` so the tagline wraps gracefully when squeezed. The paragraph (`.mission-quote`) has no own `max-width` and fills the statement container, so both texts share the same right edge. Verified no horizontal overflow 375–1920px.
  - **Vision** lead refined to the reduce/streamline → eliminate framing ("Today, OptiFlow lets domain experts build professional workflows that reduce and streamline manual, image-related work. Tomorrow, it builds those workflows autonomously — eliminating that work entirely, so experts focus fully on their domain expertise and the value only they can add.").
- Retained: workflow-from-image demo in the Platform area, postMessage iframe sizing, ETH Zürich umlaut, no fabricated metrics.
- **Homepage is complete and locked.** Full-page review (June 2026) confirmed every section earns its place; no content cut. Section vertical spacing tightened (`--sec: clamp(4rem,8vw,6rem)`, down from `clamp(4.5rem,9vw,7.5rem)`) — page height ~7,700px at 1440px wide (was ~8,100px). Nav is `position:fixed`, so the persistent "Book a Demo" CTA + escape hatch are always visible. No in-page scroll-nav added (linear narrative, sticky top nav covers the need).

### Pending
- ~~Build `platform.html`~~ ✅ **done** (15 Jun 2026).
- ~~Build `biomedical.html`~~ ✅ **done** (16 Jun 2026).
- **Recommended next: `semiconductor.html`** — build in a new conversation; the template is fully locked. Wire the demo to `?mode=semicon`. Then `custom.html`.
- **Merge `research.html` + `research-output.html`** into a single Research page (IA decision locked).
- **Rebuild** `about.html` (add `#vision` section), `contact.html`.
- Update homepage meta description; push all updated files to GitHub / Vercel.

## Active commercial engagements (brief)

| Contact | Context | Status |
|---|---|---|
| **Dr. Liu Qing** (Director, NiCE, NTU) | One-month complimentary trial. Focus: denoising → expand module by module. Day-to-day contact: Hong Siang. | Trial commenced 02 Jun 2026. NDA to follow post-trial. |
| **Prof. Gan Chee Lip** (CHA Programme Director, NTU) | Primary decision-maker for a larger NTU contract. Deliberately excluded from current proposal — relationship not yet established. | Future target. |
| **Yensan Yong** (Director of Vision, MIT Semiconductor) | Two-phase workshop + deployment proposal in progress. | ETH Zürich leads traction messaging until MIT engagement confirmed. |
| **Ali Hasnain** (serial entrepreneur, BLOCK71 mentor) | Angel investor pitch deck delivered, framed as open conversation. | Follow-up pending. |

**IP strategy with academic institutions:** Push for Model 3 co-ownership (Logic Byte holds unilateral commercialisation rights, pays 10–15% revenue share). Fall back to Model 1 with long exclusivity + right of first refusal if NTUitive insists.

**Pricing (internal only — never on site or slides):**
- Essential Platform (E1) perpetual: USD 20,000
- Hardware Assurance Suite: USD 40,000
- Year 1 total (NTU): USD 60,000 · Year 2+ maintenance: USD 15,000/year
