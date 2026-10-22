# Profile Notes — confirmed facts

These are confirmed directly by Kartik and **take precedence over older documents** in this
repository (including `MANIFEST.md` and the README). If something here conflicts with an
older file, this file wins — and the older file should be corrected.

---

## Contact

- **Email:** kartik.h6822@gmail.com
- **LinkedIn:** https://www.linkedin.com/in/kartik-h6
- **GitHub:** https://github.com/kartik-h6
- **Portfolio:** https://kartik-h6.github.io/Portfolio/
- **WhatsApp:** +91 91415 42270 — **this is the only number published on the portfolio.**

A second, business number exists (+91 94807 27214) and is used on the Digital Setup
site for business enquiries. It is **deliberately not on the portfolio**: anyone
reaching out through this site comes through the single personal line.

---

## Locations

- **Koppal, Karnataka** — residence.
- **Anantapur, Andhra Pradesh** — RIPER campus, where the M.Pharm is pursued.

---

## Education

- **M.Pharm (Pharmacy Practice)** — Raghavendra Institute of Pharmaceutical Education and
  Research (RIPER), Anantapur (JNTUA), **Oct 2026 – present**.
  - **RIPER is an autonomous campus.** It designs and examines its own curriculum rather than
    following an affiliating university's syllabus. Kartik raised this specifically as a
    recruiter-facing point: it is a distinction among Indian pharmacy colleges and matters when
    someone is assessing the academic record. Keep it attached to the M.Pharm entry wherever
    academics are presented.
- **B.Pharm** — Priyadarshini College of Pharmacy, Koratagere (RGUHS), 2021 – 2025, CGPA 7.2 / 10.
- **Pre-University (PCMB)** — Satyam International School & PU College, Ballari, 2018 – 2020, 81.45%.

---

## Name

Written **KARTIK H** — capitalised, and with no punctuation (no full stop after the H).

---

## Certifications

**Seven certifications**, plus the B.Pharm degree certificate (which is an academic award,
not a certification — keep it separate in any count):

1. AI in Pharma: Transforming Life Sciences Through Technology — LSSSDC · Skill India · NSQF Level 5
2. Generative AI Mastermind — Outskill
3. Google AI Essentials — Google / Coursera
4. Google Prompting Essentials — Google / Coursera
5. Use AI as a Creative or Expert Partner — Google / Coursera
6. Good Clinical Practice — NIDA Clinical Trials Network
7. Junior Medical Writing Intern — YuvaIntern (certificate of experience)

---

## Other confirmed points

- **Mentoring:** delivered lectures and academic mentoring for junior students across several
  departments, both offline and online, as academic curriculum support.
- **S.M.I.L.E.** is a visual-communication asset from his medical-writing work — a
  preventive-health framework (Sleep, Move, Immunity-boosting foods, Love, Exposure to
  sunlight). It is not a pharmacology tool.
- **The site lives at `https://kartik-h6.github.io/Portfolio/`.** An earlier note in this file
  said `https://portfolio.techstudyhubcore.in`; that is superseded.
- **The repository was briefly renamed to `kartik-h6` (Oct 2026) and then renamed back to
  `Portfolio`.** Worth recording why it is not trivial: on GitHub Pages the repository name
  *is* the URL path, so the rename silently invalidated 58 absolute references — every
  `canonical` and `og:*` tag, the JSON-LD, `sitemap.xml`, `robots.txt`, the PWA manifest's
  `start_url`/`scope`, the README badges, the site origin in `assets/js/main.js`, and the
  signature appended to every contact message in `assets/js/contact.js`. All were updated and
  then reverted. Relative links were never affected, which is why the pages kept rendering
  and the breakage was invisible. **Any future rename means re-checking every absolute URL** —
  `grep -rn 'github.io/' .` is the fast way to find them.
- **The domain root is a redirect, not a second site.** `https://kartik-h6.github.io/` is
  served by its own repository, `kartik-h6/kartik-h6.github.io` (created 22 Oct 2026), which
  holds nothing but a redirect page, `.nojekyll` and a README. It sends visitors to
  `https://kartik-h6.github.io/Portfolio/`.
  - The scaffold that used to own the root — placeholder pages under clean paths (`/about/`,
    `/projects/`, `/pharmacy/`, `/sslc/`, `/cgpacalculator/`) — was **deleted**, and the
    redirect repo replaced it. Nothing of the scaffold survives.
  - A repository named `<user>.github.io` is the only one that can serve the domain root, so
    this is the only way to keep the root from being a dead end without mirroring every asset.
- **If the site is ever moved to the domain root**, the change is mechanical: copy every file
  from this repo into `kartik-h6.github.io`, then replace
  `https://kartik-h6.github.io/Portfolio/` with `https://kartik-h6.github.io/` in the 9 page
  heads and `/Portfolio/` with `/` in `manifest.json`, `sitemap.xml` and `robots.txt`. The
  binary assets (portrait, OG image, WebPs, PDFs, DOCX) cannot be moved through the API and
  would need a manual upload — which is why a redirect is the arrangement for now.
- **The portfolio is the only site carrying a contact number.** Digital Setup has its own
  business line; the portfolio routes everything through the single personal number.
