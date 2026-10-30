"""Rebuild Kartik_H_CRS_Resume_2026.pdf so it matches the facts confirmed in PROFILE-NOTES.md.

Corrections applied vs the previous PDF:
  * contact number: business line -> personal line (+91 91415 42270)
  * retired domain techstudyhubcore.in -> portfolio URL
  * conference descriptor: "national-level" -> named event, no unverified qualifier
  * dissertation: stated as a five-student group project with his contribution
  * M.Pharm start date Aug 2026 -> Oct 2026
  * TechStudyHubCore: "Apr 2026 - Present" -> archived
  * portfolio build stack: Tailwind/Netlify/Cloudflare -> hand-written HTML/CSS/JS on GitHub Pages
  * added the two internships and the remaining five certifications
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                KeepTogether, PageBreak)

NAVY = colors.HexColor("#1F3864")
GREY = colors.HexColor("#4A4A4A")
RULE = colors.HexColor("#B4C6E7")
BODY = colors.HexColor("#1A1A1A")

OUT = "assets/files/Kartik_H_CRS_Resume_2026.pdf"

name = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=19, leading=22,
                      textColor=NAVY, spaceAfter=2)
tagline = ParagraphStyle("tagline", fontName="Helvetica", fontSize=8.6, leading=11,
                         textColor=GREY, spaceAfter=1)
contact = ParagraphStyle("contact", fontName="Helvetica", fontSize=8.4, leading=11,
                         textColor=BODY)
h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=9.4, leading=12,
                    textColor=NAVY, spaceBefore=7, spaceAfter=3)
role = ParagraphStyle("role", fontName="Helvetica-Bold", fontSize=9, leading=11.5, textColor=BODY)
meta = ParagraphStyle("meta", fontName="Helvetica-Oblique", fontSize=8.2, leading=10.5, textColor=GREY)
body = ParagraphStyle("body", fontName="Helvetica", fontSize=8.4, leading=11, textColor=BODY,
                      spaceAfter=1.5)
bullet = ParagraphStyle("bullet", parent=body, leftIndent=9, bulletIndent=1, spaceAfter=1.2)


def rule():
    return Table([[""]], colWidths=[172 * mm], rowHeights=[1.2],
                 style=TableStyle([("LINEABOVE", (0, 0), (-1, -1), 0.8, RULE),
                                   ("TOPPADDING", (0, 0), (-1, -1), 0),
                                  ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))


def section(title):
    return [Paragraph(title, h2), rule()]


def bl(items):
    return [Paragraph(t, bullet, bulletText="\u2022") for t in items]


S = []

S.append(Paragraph("KARTIK H", name))
S.append(Paragraph("M.Pharm (Pharmacy Practice) Candidate &nbsp;|&nbsp; Clinical Research &nbsp;|&nbsp; "
                   "Evidence Synthesis &nbsp;|&nbsp; Medical Writing", tagline))
S.append(Paragraph("+91 91415 42270 &nbsp;\u2022&nbsp; kartik.h6822@gmail.com &nbsp;\u2022&nbsp; Koppal, "
                   "Karnataka &nbsp;|&nbsp; Open to Remote / On-site / Hybrid", contact))
S.append(Paragraph("linkedin.com/in/kartik-h6 &nbsp;\u2022&nbsp; kartik-h6.github.io/Portfolio/", contact))
S.append(Spacer(1, 4))

# ---- summary
S += section("PROFESSIONAL SUMMARY")
S.append(Paragraph(
    "B.Pharm graduate (RGUHS, 2025) pursuing an M.Pharm in Pharmacy Practice at RIPER, Anantapur, with "
    "experience in literature review, evidence synthesis, medical writing, patient-education content and "
    "healthcare communication. Co-authored a comparative telepharmacy literature review and presented a poster "
    "at a pharmacy conference. Certified in AI in Pharma (Skill India / NSQF Level 5), with additional "
    "experience applying AI and digital tools to healthcare education. Seeking entry-level clinical research "
    "opportunities.", body))

# ---- competencies
S += section("CORE COMPETENCIES")
comp = [
    ("Clinical Research Readiness", "Literature review and synthesis, comparative outcome analysis, structured "
                                    "medical writing, evidence appraisal, research documentation"),
    ("Pharmacy Practice and Patient Care", "Patient-counselling content, health simplification, adherence "
                                           "communication, telepharmacy concepts, digital health engagement"),
    ("Medical and Scientific Communication", "Pharmacology writing, research poster presentation, academic "
                                             "content architecture, AI-assisted literature support"),
    ("AI and Research Tools", "Literature searching, evidence synthesis, documentation, data handling, "
                              "scientific writing, research methodology, GCP, regulatory knowledge"),
    ("Technical and Documentation", "Structured content management, process documentation, data annotation "
                                    "readiness, no-code automation"),
    ("Languages (clinical asset)", "Kannada (native), English (professional), Hindi, Telugu, Tamil \u2014 "
                                   "vernacular patient-communication capability"),
]
rows = [[Paragraph(f"<b>{k}</b>", body), Paragraph(v, body)] for k, v in comp]
S.append(Table(rows, colWidths=[46 * mm, 126 * mm],
               style=TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                                 ("LEFTPADDING", (0, 0), (-1, -1), 0),
                                 ("RIGHTPADDING", (0, 0), (-1, -1), 2),
                                 ("TOPPADDING", (0, 0), (-1, -1), 1),
                                 ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5)])))

# ---- education
S += section("EDUCATION")
edu = [
    ("Master of Pharmacy (M.Pharm) \u2014 Pharmacy Practice", "Oct 2026 \u2013 Present",
     "Raghavendra Institute of Pharmaceutical Education and Research (RIPER), Anantapur | JNTUA | autonomous campus",
     "Focus areas aligned with clinical pharmacy, patient-centred care, evidence-based practice and research methodology."),
    ("Bachelor of Pharmacy (B.Pharm)", "2021 \u2013 2025",
     "Priyadarshini College of Pharmacy, Koratagere | RGUHS, Karnataka | CGPA 7.2 / 10", None),
    ("Pre-University \u2014 PCMB", "2018 \u2013 2020",
     "Satyam International School and PU College, Ballari, Karnataka | 81.45%", None),
]
for title, when, place, extra in edu:
    blk = [Table([[Paragraph(f"<b>{title}</b>", role), Paragraph(when, meta)]],
                 colWidths=[128 * mm, 44 * mm],
                 style=TableStyle([("ALIGN", (1, 0), (1, 0), "RIGHT"),
                                   ("LEFTPADDING", (0, 0), (-1, -1), 0),
                                   ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                                   ("TOPPADDING", (0, 0), (-1, -1), 0),
                                   ("BOTTOMPADDING", (0, 0), (-1, -1), 0)])),
           Paragraph(place, meta)]
    if extra:
        blk.append(Paragraph(extra, body))
    blk.append(Spacer(1, 2))
    S.append(KeepTogether(blk))

# ---- research
S += section("RESEARCH AND KEY PROJECTS")
S.append(Paragraph("Telepharmacy Research Project &nbsp;|&nbsp; Comparative Literature Review "
                   "<font size=8 color='#4A4A4A'><i>2025</i></font>", role))
S.append(Paragraph("RGUHS final-year dissertation, submitted as a five-student group project. My contribution "
                   "was the literature search strategy and screening, the evidence synthesis, the write-up and "
                   "the presentation.", meta))
S.append(Paragraph("\u201cPatient Satisfaction and Counseling Effectiveness in Telepharmacy: A Comparative "
                   "Literature Review of Remote vs. Face-to-Face\u201d", body))
S += bl([
    "Conducted a structured comparative analysis of remote versus in-person pharmacy counselling outcomes \u2014 "
    "directly relevant to digital clinical research, telehealth trial design and patient-reported outcomes.",
    "Identified patient-engagement drivers and adherence factors in digital pharmacy settings, and produced "
    "recommendations applicable to clinical service integration.",
    "Applied core clinical-research methods: literature search strategy, critical appraisal, data synthesis, "
    "structured medical writing and evidence-based communication.",
])
S.append(Spacer(1, 2))

S.append(Paragraph("Research and Scientific Communication &nbsp;|&nbsp; PharmaNEST 3.E, Ooty "
                   "<font size=8 color='#4A4A4A'><i>2022</i></font>", role))
S += bl([
    "Presented a poster on nanoparticle drug-delivery systems to a multi-institutional audience, and received "
    "an award recognition among peer presenters.",
    "Demonstrated scientific communication, research documentation and conference-level presentation skills.",
])
S.append(Spacer(1, 2))

S.append(Paragraph("Medical Writing Sample &nbsp;|&nbsp; AI Patient-Education Narrative Review "
                   "<font size=8 color='#4A4A4A'><i>2026</i></font>", role))
S += bl([
    "Narrative review written during a junior medical-writing internship: literature research, evidence "
    "synthesis, topic development and structured healthcare content planning.",
])
S.append(Spacer(1, 2))

S.append(Paragraph("Healthcare Portfolio Website &nbsp;|&nbsp; Independent build "
                   "<font size=8 color='#4A4A4A'><i>2026</i></font>", role))
S += bl([
    "Designed, built and deployed a responsive multi-page portfolio covering pharmacy, research and "
    "digital-health work, in hand-written HTML, CSS and JavaScript hosted on GitHub Pages.",
    "Applied structured content architecture, accessibility and progressive enhancement, with a link-checking "
    "CI gate so that broken internal references fail the build.",
])

# ---- experience (starts a new page so the heading is never orphaned)
S.append(PageBreak())
S += section("EXPERIENCE")
exp = [
    ("Medical Writer \u2014 YuvaIntern (Henry Harvin)", "Jul 2026 \u2013 Aug 2026",
     ["Junior medical-writing internship: medical literature research, evidence synthesis, topic development "
      "and structured healthcare content planning."]),
    ("Internship Trainee \u2014 KS Hospital", "Jan 2026 \u2013 Feb 2026",
     ["Junior pharmacist across purchase, inventory and clinical data management.",
      "Built and maintained a master database of 750+ pharmaceutical products \u2014 generic compositions, brand "
      "names, manufacturers, dosage forms, strengths and routes of administration.",
      "Supported Medication Management and Use (MMU) documentation aligned with NABH 6th Edition standards."]),
    ("Founder and Builder \u2014 TechStudyHubCore", "Apr 2026 \u2013 Oct 2026 \u00b7 archived",
     ["Built, alone, a learning ecosystem for pharmacy, nursing and school-level students, including a "
      "structured B.Pharm architecture, SSLC content and a CGPA/SGPA calculator on the PCI 2026 syllabus.",
      "Designed the S.M.I.L.E. framework, a vernacular health-education visual system prioritising Kannada and "
      "regional-language learners.",
      "Retired the public infrastructure deliberately rather than let it decay; the engineering record is "
      "archived on GitHub."]),
    ("Digital Setup \u2014 freelance", "Ongoing",
     ["Builds local businesses a digital presence they own: landing page, WhatsApp contact, Google and maps "
      "presence, and the local-search basics that make a business findable."]),
    ("Academic mentoring and lectures \u2014 junior students", "Ongoing",
     ["Delivered lectures and mentoring sessions for junior students across several departments, in person and "
      "online, as academic curriculum support."]),
]
for title, when, items in exp:
    blk = [Table([[Paragraph(f"<b>{title}</b>", role), Paragraph(when, meta)]],
                 colWidths=[128 * mm, 44 * mm],
                 style=TableStyle([("ALIGN", (1, 0), (1, 0), "RIGHT"),
                                   ("LEFTPADDING", (0, 0), (-1, -1), 0),
                                   ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                                   ("TOPPADDING", (0, 0), (-1, -1), 0),
                                   ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))]
    blk += bl(items)
    blk.append(Spacer(1, 2.5))
    S.append(KeepTogether(blk))

# ---- certifications
S += section("CERTIFICATIONS")
S += bl([
    "AI in Pharma: Transforming Life Sciences Through Technology \u2014 LSSSDC, Skill India, NSQF Level 5, "
    "recognised by NCVET \u00b7 Mar 2026",
    "Generative AI Mastermind \u2014 Outskill \u00b7 Dec 2025",
    "Good Clinical Practice \u2014 NIDA Clinical Trials Network",
    "Google AI Essentials \u2014 Google / Coursera",
    "Google Prompting Essentials \u2014 Google / Coursera",
    "Use AI as a Creative or Expert Partner \u2014 Google / Coursera",
    "Junior Medical Writing Intern \u2014 YuvaIntern (certificate of experience)",
])

S.append(Spacer(1, 5))
S.append(rule())
S.append(Paragraph("Available immediately &nbsp;\u2022&nbsp; Open to Clinical Research / Pharmacy Practice / "
                   "Medical Writing roles &nbsp;\u2022&nbsp; References on request", meta))

doc = SimpleDocTemplate(OUT, pagesize=A4,
                        leftMargin=19 * mm, rightMargin=19 * mm,
                        topMargin=15 * mm, bottomMargin=14 * mm,
                        title="KARTIK H \u2014 Resume 2026", author="KARTIK H",
                        subject="M.Pharm (Pharmacy Practice) candidate \u2014 clinical research, evidence "
                                "synthesis, medical writing")
doc.build(S)
print("built", OUT)
