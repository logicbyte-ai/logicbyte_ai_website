# Logic Byte Website — Handover Brief
*Upload this file at the start of a new Claude conversation to resume work on the site.*

---

## Project overview

**Company:** Logic Byte Pte. Ltd. (Singapore, inc. 2022)
**Founder:** Doorgesh Sharma Jokhun, PhD (NUS)
**Current role:** Lead AI Engineer (Computer Vision) at Borries Pte. Ltd.
**Personal links:** LinkedIn: linkedin.com/in/dsjokhun | Google Scholar: Sa4nFlYAAAAJ | Blinq: blinq.me/uSAjvpnbgGvk?bs=db | Founder email: d.s.jokhun@logicbyte.ai | General: hello@logicbyte.ai
**Company LinkedIn:** linkedin.com/company/logicbyte-ai

**Product:** OptiFlow — modular, domain-aware and AI-native image analytics platform for deploying customizable workflows at scale.
**CytoByte** — label-free DIC→pseudo-DAPI in-silico staining module within OptiFlow. Deployed commercially at ETH Zurich. Academic manuscript in preparation.

**Deployment:** Static HTML → Vercel at `logicbyte.ai` (Namecheap domain). Deploy by dropping all files into the Vercel project root. No build step required.

---

## Files in the project

| File | Purpose |
|---|---|
| `index.html` | Homepage — hero, platform features, 3 vertical cards, modules selector, pricing note, CTA band |
| `about.html` | Company story + Founder section with photo, email, LinkedIn, Scholar, Blinq |
| `biomedical.html` | Biomedical & Life Sciences vertical — 4 segments with pain points + modules + pricing note |
| `semiconductor.html` | Semiconductor & Industrial vertical — 3 segments, SEM/STEM proof point, pricing note |
| `custom.html` | Custom Solutions vertical — 3 engagement types, capabilities section, per-engagement pricing |
| `research.html` | Research overview — domain columns, selected collaborations, press coverage |
| `research-output.html` | Full scientific record — C1–C10 collaborations, P1–P6 conferences, M1–M10 media, 16 publications, B1 book chapter |
| `contact.html` | Contact page — Start a conversation card, intent cards, form with subject + domain fields, direct contact links |
| `favicon.svg` | Favicon — gold pixel-grid mark on navy background, 4 black / 4 white inner squares |
| `sitemap.xml` | XML sitemap listing all 8 pages for search engine indexing |
| `robots.txt` | Permits all crawlers, references sitemap URL |
| `DSC_0167__6_in_x_8_in__square_resized.jpg` | Founder photo (white background headshot) |
| `logo.svg` | Standalone logo SVG (not used in pages — logo is inline SVG in each nav) |

All files must sit in the same root directory when deployed.

---

## Design system

**Fonts (loaded via Google Fonts):**
- Syne — wordmark and nav
- Outfit — display headings (h1, h2, h3)
- DM Mono — homepage h1
- DM Sans — body text

**Colors:**
- Navy: `#0B1628` (background)
- Teal: `#1DB89A` (primary accent)
- Gold: `#d4af37` (wordmark, logo)

**Logo:** Inline SVG geometric gold pixel-grid mark, embedded in every `<nav>` and `<footer>`. 4 black inner squares, 4 white (`#fefefe`) inner squares — binary pattern. Not an external image reference.

**Nav structure (every page):**
- Left: logo mark + "Logic Byte" in gold Syne
- Centre: Platform · Solutions · Modules · Research · About · Contact
- Right: "Say Hello" (ghost pill → `mailto:hello@logicbyte.ai`) + "Book a Demo" (teal pill → `contact.html`)
- Mobile (≤820px): hamburger button opens full-screen drawer with expandable Solutions and Research sub-menus, pre-opened and active state set per page

**Footer structure (every page):**
- Left: logo + tagline
- Centre links: Biomedical & Life Sciences · Semiconductor & Industrial · Custom Solutions
- Bottom row: © 2026 Logic Byte Pte. Ltd. · Singapore | hello@logicbyte.ai · LinkedIn

**OptiFlow badge:** Inline teal typographic element in body copy using `.optiflow-badge` CSS class. Not a button, not a link.

---

## Key constraints — to be preserved in future edits

- **Logic Byte** = the company. **OptiFlow** = the product. Never conflated.
- OptiFlow appears as an inline badge in copy, not as a standalone heading or button.
- **The verticals are peers with no hierarchy:** Biomedical & Life Sciences · Semiconductor & Industrial · Custom Solutions.
- Personal links (LinkedIn, Google Scholar, Blinq, founder email `d.s.jokhun@logicbyte.ai`) appear **only** on `about.html` (founder section) and `contact.html` (direct links panel). Not on any other page.
- Company LinkedIn (`linkedin.com/company/logicbyte-ai`) appears in the footer of every page and in the `contact.html` direct links panel.
- `research-output.html` is Logic Byte's independently maintained full scientific record. Not presented as a personal publication list or linked to the founder's Google Scholar profile.
- Collaborations on `research-output.html` are split: **C1–C4** (Industry & Commercial) and **C5–C10** (Academic Research).
- NDA constraint: NTU must not appear anywhere in Logic Byte materials. Borries is not named on the website.
- **`--gold` CSS variable** must be `#d4af37` on every page.
- **Logo inner rects:** always `#000` (black) and `#fefefe` (white) — never `#9BA0B8`. 4 black, 4 white.

---

## Mobile optimisation

All 8 pages are mobile-optimised at ≤820px:
- **Hamburger drawer** with expandable Solutions and Research groups. Left side of each group row = navigable link. Right side = chevron toggle only.
- **Sticky jump bar** (horizontal scrollable pills) on biomedical, semiconductor, custom, research, research-output — sits at `top: 68px`. Activates and auto-scrolls to current section via scroll spy shared with the right-side navigator.
- **Footer** stacks to single column. Bottom row stacks vertically.
- Active state in drawer is pre-set per page (correct group opened, current page highlighted in teal).

---

## SEO & meta

Every page has:
- `<meta name="description">` — unique per page
- `<meta property="og:*">` and `<meta name="twitter:*">` — Open Graph and Twitter Card tags
- `<link rel="canonical">` — pointing to `https://logicbyte.ai/[page]`
- `<link rel="icon" href="favicon.svg">` — favicon

`sitemap.xml` and `robots.txt` are in the project root.

---

## Contact form

- **Backend:** Formspree (`https://formspree.io/f/mzdyjayk`) — live and tested end-to-end.
- **Form fields:** Name (required) · Company/Institution · Email (required) · Domain (dropdown) · Subject (required) · Message (required)
- **Email threading:** `_subject` field sets the Formspree email subject line. Team reply goes directly to the customer. Customer replies come directly to `hello@logicbyte.ai`. Formspree is not involved after initial delivery.
- **Intent cards:** Book a Demo / Discuss a Project / Say Hello — pre-fills message placeholder
- **"Start a conversation" card:** Prominent CTA in hero-right column with "Send us a message" button scrolling to form
- **Direct links panel:** `hello@logicbyte.ai` · `d.s.jokhun@logicbyte.ai` · LinkedIn (company page)
- **Free tier:** 50 submissions/month. No auto-reply to submitter — success message explains the thread model.

---

## Pricing signals

Surfaced in three places:
1. `index.html` — between modules section and CTA band
2. `biomedical.html` / `semiconductor.html` — beneath CTA buttons in closing band
3. `custom.html` — per-engagement pricing beneath each engagement block

All link to `contact.html` for enquiries.

---

## Buyer types and vertical strategy

1. **Biomedical / Life Sciences** — existing vertical, deployed customer (ETH Zurich / CytoByte)
2. **Semiconductor & Industrial** — existing vertical. Proof point: "Deployed on commercial SEM and STEM instruments in production environments."
3. **Growth verticals** — Defence, Materials Science, Agriculture, Pharma, etc. Custom Solutions page designed for these buyers with capabilities section and explicit "net-new capability development" positioning.

---

## Competitors (for context)

MVTec HALCON · Imaris · ZEISS ZEN · Dragonfly (ORS/Comet) · Thermo Fisher Avizo

---

## Media coverage (verified URLs)

- CNA: https://www.channelnewsasia.com/watch/becoming-human/unnatural-genius-1514711
- Straits Times: https://www.straitstimes.com/singapore/researchers-use-ai-to-identify-the-ph-of-cancer-cells
- CGTN: https://news.cgtn.com/news/2021-04-13/Singapore-researchers-using-AI-to-identify-cancer-cells-by-acidity--ZqRmTp4ZuU/index.html
- L'Express (Mauritius): https://www.lexpress.mu/node/392065
- NUS News: https://news.nus.edu.sg/nus-researchers-harness-ai-to-identify-cancer-cells-by-their-acidity/
- LabelFlow / AI Stories (YouTube): https://www.youtube.com/watch?v=QzctAUSFriU

---

## What still needs doing

1. **Formspree upgrade (optional)** — free tier is 50 submissions/month, no auto-reply to submitter. First paid tier unlocks auto-confirmation emails.
2. **Vercel deployment** — add A record + CNAME in Namecheap pointing to Vercel. All files go in project root including `favicon.svg`, `sitemap.xml`, `robots.txt`, and `DSC_0167__6_in_x_8_in__square_resized.jpg`.
3. **Google Search Console** — after deployment, submit `https://logicbyte.ai/sitemap.xml` to accelerate indexing.
4. **Future content** — as new deployments accumulate, semiconductor and custom pages would benefit from additional named or anonymised proof points alongside ETH Zurich.

---

*Last updated: April 2026. All 8 HTML pages, favicon.svg, sitemap.xml, robots.txt, and founder photo are ready for Vercel deployment.*
