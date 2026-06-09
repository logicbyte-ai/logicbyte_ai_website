# Logic Byte Website — Handover Brief

*Upload this file at the start of a new Claude conversation to resume work on the site.*

---

## Project overview

**Company:** Logic Byte Pte. Ltd. (Singapore, inc. 2023)  
**Founder (public-facing):** Dr. Doorgesh Sharma Jokhun, PhD (NUS) · Lead AI Engineer (Computer Vision), Borries Pte. Ltd.  
**Personal links:** LinkedIn: linkedin.com/in/dsjokhun | Google Scholar: Sa4nFlYAAAAJ | Blinq: blinq.me/uSAjvpnbgGvk?bs=db | d.s.jokhun@logicbyte.ai | hello@logicbyte.ai  
**Company LinkedIn:** linkedin.com/company/logicbyte-ai  
**Site:** logicbyte.ai

**Product:** OptiFlow — modular, modality-agnostic, domain-aware, no-code visual workflow builder for image analytics. Targets domain experts who need reproducible, auditable pipelines without a dedicated programming team.

**Key module:** CytoByte — label-free DIC→pseudo-DAPI in-silico staining. Deployed commercially at ETH Zürich. Academic manuscript in preparation.

**Primary verticals:** Biomedical & Life Sciences · Semiconductor & Industrial Imaging · Custom Solutions (three equal peers — none dominates).

**Deployment:** Static HTML → Vercel at `logicbyte.ai` (Namecheap domain/DNS, GitHub repository). No build step. Deploy by pushing all files to the GitHub repo root; Vercel picks up automatically.

---

## Files in the project

### Pages — all must sit in the root

| File | Purpose |
|---|---|
| `index.html` | Homepage — hero, See it in action, Platform section, verticals strip, modules selector, CTA band |
| `about.html` | Company story + Founder section with photo, email, LinkedIn, Scholar, Blinq |
| `biomedical.html` | Biomedical & Life Sciences — 4 segments, modules, traceability callout, sticky right rail |
| `semiconductor.html` | Semiconductor & Industrial Imaging — 3 segments, SEM/STEM proof, traceability callout, sticky right rail |
| `custom.html` | Custom Solutions — 3 engagement types, capabilities, sticky right rail |
| `research.html` | Research overview — domain columns, selected collaborations, press coverage, sticky right rail |
| `research-output.html` | Full scientific record — C1–C10 collaborations, P1–P6 conferences, M1–M10 media, 16 publications, book chapter, sticky right rail |
| `contact.html` | Contact — intent cards (Book a Demo / Say Hello), form with subject + domain fields. `?intent=hello` query param adjusts page context. |

### Demo embeds — also in root, loaded as iframes from index.html

| File | Role in index.html |
|---|---|
| `optiflow-window-embed.html` | Hero right column — auto-cycling workflow builder visual (Biomedical ↔ Semiconductor). Canonical desktop frame is 1060px wide, scaled down from the top-left via `transform:scale(...)` only when the iframe is narrower. Posts its current measured height back to the parent on load and resize. Source panel is 190px wide. Window body height is 640px. |
| `optiflow-pipeline-demo-embed.html` | "See it in action" right column — animated pipeline demo, cycles Biomedical ↔ Semiconductor. Fixed title "OptiFlow — Pipeline in Action". Biomedical/Semiconductor toggle tabs at bottom. Canonical desktop frame is 880px wide, scaled down from the top-left only when needed to fit iframe width. |
| `optiflow-workflow-from-image-embed.html` | Platform section right column (sticky) — "drop in a result, get the workflow back" demo, cycles Biomedical ↔ Semiconductor. Canonical desktop frame is 880px wide, scaled down from the top-left only when needed to fit iframe width. |

**Retired (do not deploy):** `optiflow-build-workflow.html`

### Supporting assets — in root

| File | Purpose |
|---|---|
| `favicon.svg` | Gold pixel-grid mark on navy, 4 black / 4 white inner squares |
| `logo.svg` | Standalone logo (not used in pages — logo is inline SVG in each nav/footer) |
| `sitemap.xml` | XML sitemap for search engine indexing |
| `robots.txt` | Permits all crawlers, references sitemap |
| `DSC_0167__6_in_x_8_in__square_resized.jpg` | Founder photo (white background headshot) |
| ~~`hero_m_bio.jpg`~~ | Removed — mobile before/after carousel retired; live hero iframe used instead. |
| ~~`hero_m_semi.jpg`~~ | Removed — see above. |

---

## Design system

**Fonts (Google Fonts — loaded at runtime):**

| Font | Used for |
|---|---|
| Syne | Wordmark and nav links |
| Outfit | Display headings on secondary pages (h2, h3) |
| DM Mono | Homepage h1 ("See more. / Discover faster. / Scale with confidence.") |
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

**Responsive breakpoints (index.html):** Side-by-side layouts collapse to stacked at ≤900px. Mobile layout at ≤600px. Content capped at 1600px centred on viewports wider than ~1660px. Additional padding-reduction breakpoints at ≤1400px and ≤1200px progressively shrink horizontal padding to maximise graphic size on 13"–14" screens. At ≤1400px the hero showcase is also capped to a 680px frame so the product window does not dominate smaller desktop layouts.

**Mobile behaviour (≤900px):** All three homepage demo iframes stack below their text content (flex column). The hero section shows the live `optiflow-window-embed.html` iframe scaled down via the embed's own `fit()`. The before/after image carousel (`.hero-mobile`) and its associated image files (`hero_m_bio.jpg`, `hero_m_semi.jpg`) have been removed. The embed files themselves have no internal responsive media queries — all size adaptation is handled by the `transform:scale()` approach.

**Secondary pages (with sticky rail):** `.page-shell` grid (`1fr var(--col-nav)`) capped at `max-width: 1600px; margin: auto` so the entire grid — content and rail — centres together on large monitors. Rail hides at ≤820px.

---

## Copy guardrails — non-negotiable

- **British English** throughout — colour, normalisation, modality, behaviour, artefact, etc.
- **"ETH Zürich"** — umlaut always required. Never "ETH Zurich".
- **No fabricated metrics** — no placeholder stats (e.g. "99.9% accuracy", "10× faster") without a verifiable source. Remove them; do not replace with different numbers.
- **No "research-grade"** — unprofessional; prohibited.
- **No "co-pilot"** — too Microsoft-associated; prohibited.
- **Pricing is internal only** — no specific figures on the site or in decks. Consistent with competitor norms in scientific imaging software.
- **"Auditable" preferred over "reproducible" alone** — reinforces the traceability story directly.
- **OptiFlow is a badge, not a heading** — styled inline (`.optiflow-badge`), never used as an H1 or H2.
- **Real images only** — no synthetic SVG imagery in public-facing demo assets.
- **Three verticals are equal peers** — Biomedical & Life Sciences, Semiconductor & Industrial Imaging, Custom Solutions. None dominates or leads.
- **Vertical name confirmed:** "Semiconductor & Industrial Imaging" — used consistently on the site and LinkedIn.
- **"Not automation for its own sake — intelligence in service of expertise"** — the preferred framing. Avoid language that implies replacement of the domain expert.
- **NTU and Borries are internal only** — never mentioned in public-facing copy.
- **Tone:** declarative and confident, not invitational. Short punchy headlines. Semi-formal for known contacts.

---

## iframe demo architecture

All three demo embeds now use a **unified width-first postMessage sizing contract**. This is required because `file://` iframes are cross-origin (origin "null"), which blocks the parent from reading `contentWindow.document` directly. postMessage works in both local `file://` testing and on the deployed same-origin site.

**Parent page (`index.html`):**

- The homepage owns the outer frame widths: hero capped at 1060px, pipeline and workflow demos capped at 880px, all centred in their columns.
- The homepage also reserves close-to-final placeholder space before the embeds load: hero `1060 / 684`, pipeline `880 / 723`, workflow `880 / 672`.
- `applyEmbedMeasurement(source, height, width)` listens for postMessage events and applies the **latest reported height** directly to the matching iframe, rather than keeping a grow-only max-height cache.
- The hero iframe mask radius on the homepage is intentionally smaller (`8px`) than the inner product window radius so the green bottom corners remain visible on 13-inch-class desktop layouts.

**Hero window (`optiflow-window-embed.html`):**

- Wraps the UI in a 1060px `.scaler` with `transform-origin: top left`.
- `fit()` calculates `scale = min(window.innerWidth / 1060, 1)`, applies `transform:scale(...)` only when needed, then sets both `body` and `html` height to the scaled height.
- Posts `{ optiflowEmbedHeight, optiflowEmbedWidth, optiflowWindowHeight }` so the parent can size the iframe through the shared handler while remaining backward-compatible with the hero-specific field.
- A leftover narrow-screen `body` padding rule was removed in June 2026 after it was found to create top/left gutter and right/bottom clipping inside the iframe at smaller desktop widths.

**Pipeline demo (`optiflow-pipeline-demo-embed.html`):**

- Wraps the UI in `#pd-scaler` at a natural width of 880px with `transform-origin: top left`.
- Uses width-only downscaling: `scale = min(availW / 880, 1)`.
- On load, waits 420ms before the first fit so the animated strip has populated and the reported height is stable.
- The operation-card strip is pinned to a stable loaded height of `106px`, with scrollbar space reserved from the beginning, so adding the fifth card does not change the overall window height.
- The scaler padding is slightly top-light / bottom-heavy (`2px` top, `8px` bottom) to remove the tiny top gutter and keep the preview visually centred.
- Footer controls are nudged inward slightly for breathing room: transport buttons offset from the left edge, domain tabs offset from the right edge.
- Posts `{ optiflowEmbedHeight, optiflowEmbedWidth }` on load, resize, and ResizeObserver updates.
- **No internal media queries.** A `@media(max-width:640px)` block that previously collapsed the layout on narrow iframe viewports was removed (June 2026); `transform:scale()` handles all size adaptation.

**Workflow-from-image demo (`optiflow-workflow-from-image-embed.html`):**

- Uses an 880px `.wrap` with `transform-origin: top left`.
- Uses width-only downscaling: `scale = min(availW / 880, 1)`.
- Sets `body` and `html` height from the current scaled height, then posts `{ optiflowEmbedHeight, optiflowEmbedWidth }`.
- **No internal media queries.** A `@media(max-width:640px)` block that switched `.top` to `flex-direction:column` (collapsing the two-column image+workflow layout) was removed (June 2026).

**Practical rule:** the embeds preserve a canonical desktop frame and only scale down when space is tighter. The parent page does not stretch them to fill arbitrarily wide columns on large monitors.

---

## Screenshot / QA workflow

```bash
# Playwright against local file:/// paths
python3 script.py  # uses playwright.sync_api, --no-sandbox flag
# Output files → /mnt/user-data/outputs/
```

Claude-in-Chrome `save_to_disk` captures return an ID but are not accessible from the bash filesystem. Use Playwright for downloadable QA screenshots.

Audit after changes: check for horizontal overflow at 1280px and 1920px, no fonts below 10px, no "ETH Zurich" (without umlaut), and no internal gutter/clipping mismatch on the three homepage demo iframes.

---

## Deployment

Vercel auto-deploys from the `main` branch of the GitHub repo. Pushing to `main` is the only step needed to go live — no build command, no manual Vercel trigger.

### One-time setup (WSL / new machine)

```bash
# Allow git to operate on the Windows-mounted drive path
git config --global --add safe.directory '/mnt/i/My Drive/logicbyte_ai'
```

### Stage, commit, and push

```bash
cd "/mnt/i/My Drive/logicbyte_ai"

# Stage all site files (pages, embeds, assets, readme)
# Do NOT add: IssueTracker.xlsx, desktop.ini, sample_data/,
#             optiflow-pipeline-demo.html, optiflow-product-window.html,
#             optiflow-workflow-from-image.html  (dev/standalone versions, not deployed)
git add index.html about.html biomedical.html semiconductor.html \
        custom.html research.html research-output.html contact.html \
        optiflow-window-embed.html optiflow-pipeline-demo-embed.html \
        optiflow-workflow-from-image-embed.html \
        logicbyte_ai_readme.md logicbyte_readme.md \
        favicon.svg logo.svg sitemap.xml robots.txt \
        DSC_0167__6_in_x_8_in__square_resized.jpg

git rm hero_m_bio.jpg hero_m_semi.jpg

git commit -m "Improve mobile/tablet experience: show scaled iframes below text on ≤900px screens"

git push origin main
```

Vercel will detect the push and deploy within ~30–60 seconds. Check live at **logicbyte.ai**.

### Verify the deploy

1. Open logicbyte.ai on a phone or DevTools mobile emulator (≈390px wide).
2. Hero section: live OptiFlow window iframe should appear below the headline — not the before/after carousel.
3. "See it in action": pipeline demo should show the full animated desktop layout, scaled down.
4. "Platform" section: workflow-from-image demo should show image + workflow side-by-side (two columns), scaled down.
5. On desktop (>900px): confirm no visible change from previous layout.

---

## Current status (June 2026)

**Live at:** logicbyte.ai (Vercel)

### Completed website work
- Full multi-session overhaul: layout, copy, responsive polish
- Homepage: side-by-side hero / See it in action / Platform sections (text left, demo/window right)
- Workflow-from-image demo moved from biomedical.html → Platform section (domain-agnostic proof point)
- Unified postMessage iframe sizing for all three demo embeds including hero window
- Content capped at 1600px centred, site-wide (incl. `.page-shell` grid on detail pages)
- Seventh feature card added: "Reproducible & auditable by design"
- Traceability callout added to biomedical and semiconductor pages
- ETH Zürich umlaut corrected site-wide; "research-grade" removed; fabricated hero metrics removed
- Inc. year corrected to 2023 in about.html
- **Hero product window (`optiflow-window-embed.html`)**: rebuilt with real bio + semicon images, auto-cycling domains, source panel 190px, window height 640px, `.phdr` fixed-height for line alignment, reduced card spacing, batch button label simplified to "Batch"
- **Pipeline demo (`optiflow-pipeline-demo-embed.html`)**: op cards widened to 200px with 3-line layout (Op#|IN|OUT / title / group), pvhead condensed to single line "Op title · description", legacy note paragraph removed, left text updated; canonical 880px desktop frame now scales down from the top-left only when space is tighter
- **Pipeline demo polish**: op-strip height fixed at 106px so the scrollbar appearing at the 5th card no longer changes window height; preview shifted up slightly via scaler padding rebalance; footer controls nudged inward for edge breathing room
- **Responsive hero**: padding-reduction breakpoints at ≤1400px and ≤1200px so graphics scale maximally on 13"–14" laptops; hero showcase additionally capped to 680px at ≤1400px before the mobile hero takeover at ≤900px
- **Homepage demo framing**: hero/pipeline/workflow wrappers now use canonical desktop frame widths (1060 / 880 / 880), with tuned placeholder aspect ratios and current-measurement iframe height updates instead of grow-only max-height behaviour
- **Hero iframe scaling**: fixed overflow-propagation bug (html overflow + window.innerWidth), removed stale narrow-screen body padding inside the hero embed, kept hero iframe height driven entirely by postMessage, and reduced the homepage hero mask radius to keep the inner green corners visible on 13" screens
- **Mobile demo experience (June 2026)**: on ≤900px screens, all three homepage iframes now appear as scaled-down versions of the desktop layout, stacked below their text content. Hero section now shows the live `optiflow-window-embed.html` iframe (`.hero-mobile` hidden); pipeline and workflow iframes already stacked correctly. Removed `@media(max-width:640px)` blocks from `optiflow-pipeline-demo-embed.html` and `optiflow-workflow-from-image-embed.html` that were triggering on the iframe's own narrow viewport and collapsing the internal layouts before the `transform:scale()` ran.

### Pending
- Update homepage meta description (current one frames Logic Byte too narrowly)
- `optiflow-build-workflow.html` retirement decision pending (likely retire)

---

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
