#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generator barevnych HTML pracovnich listu pro pripravu na prijimacky - MA5"""
import base64, os, sys
sys.path.insert(0, '/home/claude')
from hints_data import HINTS_PL01,HINTS_PL02,HINTS_PL03,HINTS_PL04,HINTS_PL05,HINTS_PL06,HINTS_PL07,HINTS_PL08,HINTS_PL09,QUIZ_PL01,QUIZ_PL02,QUIZ_PL03,QUIZ_PL04,QUIZ_PL05,QUIZ_PL06,QUIZ_PL07,QUIZ_PL08,QUIZ_PL09

OUTDIR = os.path.join(os.path.dirname(__file__) or ".", "docs", "pages")
IMGDIR = "/tmp/cropped"

def img64(name):
    p = f"{IMGDIR}/{name}.jpeg"
    if not os.path.exists(p): return ""
    with open(p,"rb") as f: d = f.read()
    return "data:image/jpeg;base64," + base64.b64encode(d).decode()

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Segoe UI', Arial, sans-serif; font-size: 15px;
       color: #222; background: #f5f5f5; padding: 16px; }

/* --- PAGE WRAPPER --- */
.page { background: white; max-width: 1024px; margin: 0 auto;
        padding: 32px; border-radius: 12px;
        box-shadow: 0 2px 12px rgba(0,0,0,.15); }

/* --- COVER BANNER --- */
.cover { color: white; border-radius: 14px; padding: 26px 28px 22px;
         margin-bottom: 22px; }
.cover .num { font-size: 13px; opacity: .85; margin-bottom: 4px; font-weight: 600;
              letter-spacing: 1px; text-transform: uppercase; }
.cover h1 { font-size: 30px; font-weight: 800; margin-bottom: 6px; }
.cover .sub { font-size: 15px; opacity: .9; margin-bottom: 10px; }
.cover .pts { display: inline-block; background: rgba(255,255,255,.25);
              border-radius: 20px; padding: 5px 16px; font-size: 13px; font-weight: 700; }

/* ── BLACKPINK — cover & member card ── */
.cover { border-bottom: 3px solid #ff0076; position: relative; overflow: hidden; }
.cover::after { content: ''; position: absolute; top: -60px; right: -60px;
  width: 220px; height: 220px;
  background: radial-gradient(circle, #ff007855 0%, transparent 70%);
  pointer-events: none; }

.member-card {
  display: flex; align-items: center; gap: 14px;
  background: rgba(0,0,0,.25); border: 1px solid rgba(255,0,118,.4);
  border-radius: 12px; padding: 14px 18px; margin-top: 16px;
}
.member-avatar {
  width: 60px; height: 60px; border-radius: 50%;
  border: 2.5px solid #ff0076;
  display: flex; align-items: center; justify-content: center;
  font-size: 28px; background: rgba(0,0,0,.3); flex-shrink: 0;
  box-shadow: 0 0 14px #ff007666;
}
.member-info .member-name {
  font-size: 17px; font-weight: 800;
  letter-spacing: .5px; text-shadow: 0 0 10px #ff007888;
}
.member-info .member-role {
  font-size: 12px; color: rgba(255,255,255,.7);
  text-transform: uppercase; letter-spacing: 1px; margin-top: 2px;
}
.member-info .member-quote {
  font-size: 13px; color: rgba(255,255,255,.9);
  margin-top: 6px; font-style: italic; line-height: 1.5;
}

.bp-back { display: inline-flex; align-items: center; gap: 8px;
  margin-bottom: 8px; color: #666; text-decoration: none;
  font-size: 13px; font-weight: 600;
  padding: 5px 13px; border: 1px solid #ddd;
  border-radius: 20px; transition: all .2s; background: white; }
.bp-back:hover { background: #ff0076; color: white; border-color: #ff0076; }

/* --- HINTS SECTION --- */
.hints-section { background: #fafafa; border-radius: 12px;
                 border: 2px solid #e0e0e0; padding: 20px; margin-bottom: 26px; }
.hints-title { font-size: 15px; font-weight: 800; letter-spacing: .5px;
               text-transform: uppercase; margin-bottom: 16px; display: flex;
               align-items: center; gap: 8px; }
.hint-blocks { display: flex; flex-direction: column; gap: 16px; }
.hint-block { border-radius: 10px; padding: 14px 16px; border-left: 5px solid; }
.hint-block h3 { font-size: 15px; font-weight: 800; margin-bottom: 12px;
                 display: flex; align-items: center; gap: 8px;
                 padding-bottom: 10px; border-bottom: 2px solid rgba(0,0,0,.1); }
.hint-block p, .hint-block li { font-size: 14px; line-height: 1.75; color: #333; }
.hint-block ul { padding-left: 0; list-style: none; }
.hint-block ul li { padding: 5px 0 5px 20px; position: relative; }
.hint-block ul li::before { content: "•"; position: absolute; left: 4px;
                             color: #888; font-size: 16px; line-height: 1.5; }
.hint-block ol { padding-left: 0; list-style: none; counter-reset: hint-steps; }
.hint-block ol li { padding: 7px 0 7px 36px; position: relative;
                    counter-increment: hint-steps; border-bottom: 1px solid rgba(0,0,0,.05); }
.hint-block ol li:last-child { border-bottom: none; }
.hint-block ol li::before { content: counter(hint-steps);
                             position: absolute; left: 0; top: 7px;
                             width: 24px; height: 24px; border-radius: 50%;
                             background: rgba(0,0,0,.12); color: #333;
                             font-size: 12px; font-weight: 800;
                             display: flex; align-items: center; justify-content: center; }
.hint-block .formula { background: rgba(0,0,0,.07); border-radius: 6px;
                       padding: 6px 10px; font-family: monospace; font-size: 14px;
                       margin: 6px 0; display: block; }
.hint-block .ex { background: rgba(255,255,255,.85); border-radius: 8px;
                  padding: 12px 14px; margin-top: 10px; font-size: 14px;
                  border: 1px solid rgba(0,0,0,.12); }
.hint-block .ex .lbl { font-weight: 800; font-size: 12px; text-transform: uppercase;
                       letter-spacing: .5px; opacity: .7; margin-bottom: 6px; }

/* Fill-in box — replaces □ */
.fillin { display: inline-flex; align-items: center; justify-content: center;
          min-width: 52px; height: 28px; background: #fffde7;
          border: 2.5px dashed #f9a825; border-radius: 6px;
          font-size: 13px; font-weight: 700; color: #e65100;
          padding: 0 8px; margin: 0 3px; vertical-align: middle;
          letter-spacing: .5px; }

/* Hint diagram container */
.hint-diagram { margin: 12px 0; text-align: center; }
.hint-diagram svg { max-width: 100%; height: auto; }
.hint-diagram .diagram-caption { font-size: 12px; color: #888;
                                  font-style: italic; margin-top: 6px; }

/* Hint result highlight */
.hint-result { display: inline-block; background: rgba(0,0,0,.08);
               border-radius: 6px; padding: 4px 12px; font-weight: 800;
               font-size: 15px; margin: 4px 0; }

/* Hint table — cleaner */
.hint-block { overflow-x: auto; }
.hint-block table.htable { width: 100%; border-collapse: collapse; margin: 10px 0; font-size: 14px; }
.hint-block table.htable th { padding: 9px 12px; text-align: center; font-size: 13px; font-weight: 700; }
.hint-block table.htable td { padding: 8px 12px; text-align: center; border: 1px solid rgba(0,0,0,.1); }
.hint-block table.htable .fill { background: #fffde7; font-style: italic; color: #e65100; }

/* Hint step-box — for multi-step calculations */
.hint-calc { background: rgba(0,0,0,.05); border-radius: 8px;
             padding: 10px 14px; margin: 8px 0; font-family: monospace;
             font-size: 14px; line-height: 2; }
.hint-calc .step-arrow { color: #999; margin: 0 8px; }
.hint-calc b { color: #1a1a1a; }

/* --- DIVIDER --- */
.divider { text-align: center; margin: 24px 0 20px; position: relative; }
.divider::before { content:''; position:absolute; top:50%; left:0; right:0;
                   height:2px; background:#e0e0e0; }
.divider span { position: relative; background: white; padding: 0 14px;
                font-weight: 800; font-size: 14px; letter-spacing: .5px;
                text-transform: uppercase; color: #888; }

/* --- EXAMPLE CARDS --- */
.example { border-radius: 12px; margin-bottom: 22px; overflow: hidden;
           border: 2px solid #e0e0e0; }
.ex-header { padding: 12px 18px; display: flex; justify-content: space-between;
             align-items: center; }
.ex-header .ex-num { font-size: 13px; font-weight: 800; letter-spacing: .5px;
                     text-transform: uppercase; }
.ex-header .ex-source { font-size: 11px; opacity: .85; font-style: italic; }
.ex-badge { display: inline-flex; align-items: center; gap: 5px; padding: 4px 12px;
            border-radius: 20px; font-size: 12px; font-weight: 700; }

.ex-body { padding: 16px 18px; }

/* Zadani */
.zadani { background: #f8f9fa; border-radius: 8px; padding: 14px 16px;
          margin-bottom: 14px; border-left: 5px solid #999; font-size: 14px;
          line-height: 1.7; }
.zadani strong { display: block; font-size: 12px; text-transform: uppercase;
                 letter-spacing: .5px; color: #888; margin-bottom: 6px; }

/* Exam image */
.exam-img { margin: 16px 0; }
.exam-img img { width: 100%; max-width: 100%; display: block; margin: 0 auto;
                border-radius: 8px; border: 1px solid #ddd;
                box-shadow: 0 2px 8px rgba(0,0,0,.12); }
.exam-img .img-cap { font-size: 11px; color: #888; margin-top: 6px; font-style: italic; text-align:center; }

/* SOLVED example steps */
.steps { display: flex; flex-direction: column; gap: 10px; margin-bottom: 14px; }
.step { display: flex; gap: 12px; align-items: flex-start; }
.step-num { width: 28px; height: 28px; border-radius: 50%; display: flex;
            align-items: center; justify-content: center; font-weight: 800;
            font-size: 13px; flex-shrink: 0; color: white; }
.step-content { flex: 1; padding: 8px 12px; border-radius: 8px;
                font-size: 14px; line-height: 1.6; }
.step-content .step-label { font-size: 11px; font-weight: 700; text-transform: uppercase;
                             letter-spacing: .4px; opacity: .7; margin-bottom: 4px; }
.step-content .calc { font-family: monospace; background: rgba(0,0,0,.06);
                      border-radius: 5px; padding: 4px 8px; display: inline-block;
                      margin: 3px 0; font-size: 14px; }

.result-box { border-radius: 10px; padding: 12px 16px; display: flex;
              align-items: center; gap: 10px; font-weight: 700; font-size: 15px; }
.result-box .r-icon { font-size: 22px; }

/* HINT example */
.hint-card { border-radius: 8px; padding: 12px 14px; margin-bottom: 12px; }
.hint-card h4 { font-size: 13px; font-weight: 700; text-transform: uppercase;
                letter-spacing: .5px; margin-bottom: 8px; display: flex;
                align-items: center; gap: 6px; }
.hint-card p { font-size: 14px; line-height: 1.65; }
.hint-step { display: flex; align-items: flex-start; gap: 8px; margin: 7px 0; }
.hint-arrow { font-size: 16px; color: #999; flex-shrink: 0; margin-top: 2px; }
.hint-text { font-size: 14px; line-height: 1.6; }
.hint-blank { display: inline-block; border-bottom: 2px solid #bbb;
              min-width: 70px; height: 22px; vertical-align: bottom; }

/* Answer box */
.answer-box { background: #fffde7; border-radius: 10px; padding: 14px 16px;
              border: 2px dashed #f9a825; margin-top: 12px; }
.answer-box .a-label { font-size: 12px; font-weight: 700; text-transform: uppercase;
                       letter-spacing: .5px; color: #795548; margin-bottom: 8px; }
.answer-line { border-bottom: 2px solid #ddd; height: 28px; margin: 6px 0; }

/* Scratch space */
.scratch { background: #fafafa; border-radius: 8px; padding: 10px;
           margin: 10px 0; border: 1px dashed #ccc; }
.scratch .s-label { font-size: 11px; color: #bbb; margin-bottom: 6px; }
.scratch-line { border-bottom: 1px solid #eee; height: 26px; margin: 4px 0; }

/* Solo example */
.solo-badge { background: #e8f5e9; color: #1b5e20; }

/* Tip box */
.tip-box { border-radius: 10px; padding: 12px 16px; margin-top: 14px;
           border-left: 5px solid; display: flex; gap: 10px; align-items: flex-start; }
.tip-box .tip-icon { font-size: 20px; flex-shrink: 0; }
.tip-box p { font-size: 13px; line-height: 1.6; }

/* Visual calc demo */
.calc-demo { background: #f3f4f6; border-radius: 10px; padding: 14px 16px;
             margin: 10px 0; font-family: monospace; font-size: 14px; line-height: 2; }
.calc-demo .hl { font-weight: 800; }
.calc-demo .arrow { color: #999; }
.calc-demo .note { font-family: sans-serif; font-size: 12px; color: #666;
                   background: white; border-radius: 4px; padding: 2px 6px;
                   margin-left: 6px; font-style: italic; }

/* Comparison visual */
.comp-visual { display: grid; gap: 8px; margin: 10px 0; }
.comp-bar { display: flex; align-items: center; gap: 10px; font-size: 13px; }
.comp-bar .label { min-width: 140px; font-weight: 600; }
.bar-track { flex: 1; background: #e0e0e0; border-radius: 4px; height: 22px;
             overflow: hidden; position: relative; }
.bar-fill { height: 100%; border-radius: 4px; display: flex; align-items: center;
            padding-left: 8px; color: white; font-size: 12px; font-weight: 700; }

/* Table in examples */
.ex-table { width: 100%; border-collapse: collapse; margin: 10px 0; font-size: 14px; }
.ex-table th { padding: 8px 10px; text-align: center; font-size: 13px; }
.ex-table td { padding: 8px 10px; text-align: center; border: 1px solid #e0e0e0; }
.ex-table .fill { background: #fffde7; min-width: 50px; }


/* --- QUIZ SECTION --- */
.quiz-section { background: #f0f4ff; border-radius: 12px; border: 2px solid #c5cae9;
                padding: 20px; margin-bottom: 26px; }
.quiz-title { font-size: 15px; font-weight: 800; letter-spacing: .5px; text-transform: uppercase;
              margin-bottom: 16px; color: #283593; display: flex; align-items: center; gap: 8px; }
.quiz-q { background: white; border-radius: 10px; padding: 14px 16px; margin-bottom: 14px;
          border-left: 5px solid #3949ab; }
.quiz-chart { margin: 8px 0 4px; background: #f8faff; border-radius: 8px;
              padding: 8px 12px; border: 1px solid #dde; overflow-x: auto; }
.quiz-q .q-num { font-size: 12px; font-weight: 700; text-transform: uppercase; color: #5c6bc0;
                 letter-spacing: .5px; margin-bottom: 6px; }
.quiz-q .q-text { font-size: 15px; font-weight: 600; color: #1a237e; margin-bottom: 10px;
                   line-height: 1.5; }
.quiz-options { display: flex; flex-direction: column; gap: 6px; }
.quiz-opt { display: flex; align-items: flex-start; gap: 10px; padding: 8px 12px;
            border-radius: 8px; background: #f8f9fa; border: 1.5px solid #e0e0e0;
            font-size: 14px; cursor: default; }
.quiz-opt .opt-letter { font-weight: 800; color: #5c6bc0; min-width: 22px; flex-shrink: 0; }
.quiz-answer { margin-top: 10px; padding: 10px 14px; border-radius: 8px;
               background: #e8f5e9; border-left: 4px solid #43a047;
               font-size: 13px; line-height: 1.6; color: #1b5e20; display: none; }
.quiz-answer .ans-label { font-weight: 700; font-size: 12px; text-transform: uppercase;
                           letter-spacing: .5px; margin-bottom: 4px; }
.quiz-answer .ans-correct { font-size: 14px; font-weight: 700; margin-bottom: 4px; }


/* --- ANSWER KEY SECTION --- */
.quiz-answers-section { border-radius: 12px; border: 2px solid #3949ab;
                        padding: 20px; margin-top: 14px; margin-bottom: 8px;
                        background: #f8f9ff; }

.quiz-answers-title { font-size: 15px; font-weight: 800; letter-spacing: .5px;
                      text-transform: uppercase; margin-bottom: 14px; }
.ans-row-correct { font-size: 14px; font-weight: 700; margin-bottom: 4px; }
.ans-row-exp { font-size: 13px; line-height: 1.6; color: #333; }

@media print {
  body { background: white; padding: 0; font-size: 13px; }
  .page { box-shadow: none; border-radius: 0; max-width: 100%; padding: 14px 20px; }
  .example { break-inside: avoid; page-break-inside: avoid; }
  .hints-section { break-inside: avoid; }
  .hint-blocks { flex-direction: column; }
  .exam-img { break-inside: avoid; }
  .exam-img img { max-width: 100%; width: 100%; }
  .steps { break-inside: avoid; }
  .quiz-section { break-inside: avoid; }
  .quiz-answers-section { break-inside: avoid; }

}
"""

def make_html(title, sub, num, color_dark, color_mid, color_light, color_text, body):
    return f"""<!DOCTYPE html>
<html lang="cs">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>PL{num:02d} &mdash; {title}</title>
<style>{CSS}</style>
</head>
<body>

<div class="page">
{body}
</div>
</body>
</html>"""

# BLACKPINK members assigned to each PL
BP_MEMBERS = {
    1: {"name": "JISOO",  "emoji": "🌸", "color": "#ff80c0",
        "role": "Průvodkyně geometrií",
        "quote": "Přesnost je základ krásy — i při rýsování kružítkem! Každý krok má svůj řád. Fighting! 💪"},
    2: {"name": "LISA",   "emoji": "💛", "color": "#ffd700",
        "role": "Průvodkyně prostorem",
        "quote": "Prostorová představivost je jako tanec — musíš vidět celý pohyb najednou. You can do it! 🎵"},
    3: {"name": "ROSÉ",   "emoji": "🌹", "color": "#ff80c0",
        "role": "Průvodkyně vzory",
        "quote": "Vzory jsou všude okolo nás — jako melodie v písničce. Najdi rytmus posloupnosti! 🎶"},
    4: {"name": "JENNIE", "emoji": "💎", "color": "#c084fc",
        "role": "Průvodkyně grafy",
        "quote": "Každý graf vypráví příběh. Přečti ho pozorně — čísla nikdy nelžou! 📊"},
    5: {"name": "JENNIE", "emoji": "💎", "color": "#c084fc",
        "role": "Průvodkyně podmínkami",
        "quote": "Podmínky jsou jako pravidla ve skupině — musí platit všechny najednou. Systematicky! 💎"},
    6: {"name": "ROSÉ",   "emoji": "🌹", "color": "#ff80c0",
        "role": "Průvodkyně plochou",
        "quote": "Obvod jde po okraji, obsah se skrývá uvnitř — nezaměňuj je! Já v tebe věřím 🌹"},
    7: {"name": "LISA",   "emoji": "💛", "color": "#ffd700",
        "role": "Průvodkyně výrazy",
        "quote": "Závorky mění vše — jako beat drop v písničce. Dodržuj pořadí a výsledek přijde! 🎤"},
    8: {"name": "JISOO",  "emoji": "🌸", "color": "#ff80c0",
        "role": "Průvodkyně jednotkami",
        "quote": "Převody jednotek jsou jako překlad z korejštiny — vždy zkontroluj slovník! 🌸"},
    9: {"name": "JENNIE", "emoji": "💎", "color": "#ffd700",
        "role": "Průvodkyně poměry",
        "quote": "Poměry jsou jako mix tracků — každý díl musí sedět přesně. Nepočítej od oka! 💎"},
}

def cover(num, title, sub, pts, c_dark, c_mid, pdf_name=""):
    pdf_btn = ""
    if pdf_name:
        pdf_btn = f'''<a href="../pdfs/{pdf_name}" download style="display:inline-flex;align-items:center;gap:8px;margin-top:14px;background:rgba(255,255,255,.15);color:white;padding:9px 20px;border-radius:8px;text-decoration:none;font-size:14px;font-weight:600;border:1.5px solid rgba(255,0,118,.5);transition:background .2s">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 15V3m0 12l-4-4m4 4l4-4M2 17l.621 2.485A2 2 0 0 0 4.561 21h14.878a2 2 0 0 0 1.94-1.515L22 17"/></svg>
      Stáhnout PDF k tisku
    </a>'''
    m = BP_MEMBERS.get(num, BP_MEMBERS[1])
    member_html = f'''<div class="member-card">
  <div class="member-avatar">{m["emoji"]}</div>
  <div class="member-info">
    <div class="member-name" style="color:{m["color"]}">{m["name"]}</div>
    <div class="member-role">{m["role"]}</div>
    <div class="member-quote">„{m["quote"]}"</div>
  </div>
</div>'''
    back_btn = '<a href="../index.html" class="bp-back">← zpět na přehled</a>'
    return f"""<div style="margin-bottom:8px">{back_btn}</div>
<div class="cover" style="background:linear-gradient(135deg,{c_dark}ee,{c_mid}cc,#1a0010)">
  <div style="font-size:11px;opacity:.7;letter-spacing:2px;text-transform:uppercase;font-weight:700;margin-bottom:6px">🖤 BLACKPINK × Matematika 5 🩷</div>
  <div class="num">📄 Pracovní list {num:02d}</div>
  <h1>{title}</h1>
  <div class="sub">{sub}</div>
  <div class="pts">⭐ Max. {pts} bodů v testu</div>
  {pdf_btn}
  {member_html}
</div>"""

def hints_start(c_dark):
    return f"""<div class="hints-section">
<div class="hints-title" style="color:{c_dark}">💡 Pravidla a tipy &mdash; přečti si před každým řešením!</div>
<div class="hint-blocks">"""

def hints_end():
    return """</div></div>"""


def build_quiz(questions, c_dark="#283593"):
    """Generates only the questions (no answers inline)."""
    html = f'''<div class="quiz-section">
<div class="quiz-title" style="color:{c_dark}">🧩 Procvičení základních principů — zakroužkuj správnou odpověď</div>'''
    for i, q in enumerate(questions, 1):
        html += f'''<div class="quiz-q">
<div class="q-num">Otázka {i}</div>
<div class="q-text">{q["otazka"]}</div>
<div class="quiz-options">'''
        for opt in q["moznosti"]:
            html += f'''<div class="quiz-opt"><span class="opt-letter">{opt[0]}</span><span>{opt[3:]}</span></div>'''
        html += '''</div></div>'''
    html += "</div>"
    return html


def _strip_charts(html):
    import re as _re
    return _re.sub(r'<div class="quiz-chart">.*?</div>', '', html, flags=_re.DOTALL)

def build_quiz_answers(questions, c_dark="#283593"):
    """Collapsible answer rows — click to reveal."""
    html = f'''<div class="quiz-answers-section" style="border-color:{c_dark}">
<div class="quiz-answers-title" style="color:{c_dark}">✅ Odpovědi ke kvízu — klikni pro zobrazení</div>'''
    for i, q in enumerate(questions, 1):
        q_text = _strip_charts(q["otazka"])
        # Short label: strip HTML tags for toggle label
        import re as _re2
        label = _re2.sub(r'<[^>]+>', '', q_text).strip()[:70]
        if len(_re2.sub(r'<[^>]+>', '', q_text).strip()) > 70:
            label += "…"
        aid = f"a{i}_{abs(hash(q['otazka']))%99999}"
        html += f'''<div class="quiz-ans-row">
<div class="ans-toggle" onclick="tA('{aid}')" id="tg_{aid}">
  <span class="toggle-icon">▶</span>
  <span class="toggle-label">Otázka {i} — {label}</span>
</div>
<div class="ans-body" id="{aid}">
  <div class="ans-row-correct" style="color:{c_dark};font-size:15px;font-weight:700;margin-bottom:6px">
    ✅ Správná odpověď: {q["spravna"]}
  </div>
  <div class="ans-row-exp">{q["vysvetleni"]}</div>
</div></div>'''
    html += '''</div>
<script>
function tA(id){
  var b=document.getElementById(id);
  var t=document.getElementById("tg_"+id);
  b.classList.toggle("open");
  t.classList.toggle("open");
}
</script>'''
    return html



def build_hints(blocks):
    parts = []
    for (icon, title, content, bg, border) in blocks:
        parts.append(hblock(icon, title, content, bg, border))
    return "".join(parts)

def hblock(icon, title, content, bg, border):
    return f"""<div class="hint-block" style="background:{bg};border-color:{border}">
<h3>{icon} {title}</h3>
{content}
</div>"""

def ex_header(num, title, source, badge_bg, badge_color, badge_text, badge_icon):
    return f"""<div class="ex-header" style="background:{badge_bg}22">
  <div>
    <div class="ex-num" style="color:{badge_color}">{badge_icon} Příklad {num}</div>
    <div style="font-size:14px;font-weight:700;color:#222;margin-top:2px">{title}</div>
  </div>
  <div>
    <div class="ex-badge" style="background:{badge_bg};color:{badge_color}">{badge_text}</div>
    <div class="ex-source" style="margin-top:4px;text-align:right">{source}</div>
  </div>
</div>"""

def zadani(text, border_color="#999"):
    lines = text.strip().split('\n')
    parts = []
    for l in lines:
        l = l.strip()
        if not l:
            continue
        parts.append(l if l.startswith('<') else f'<p>{l}</p>')
    html = '\n'.join(parts)
    return f"""<div class="zadani" style="border-color:{border_color}">
<strong>📋 Zadání:</strong>
{html}
</div>"""

def exam_img(name, caption="Obrázek ze zadání"):
    src = img64(name)
    if not src: return ""
    return f"""<div class="exam-img">
<img src="{src}" alt="{caption}">
<div class="img-cap">🖼 {caption}</div>
</div>"""

def step(n, label, content, num_bg, step_bg):
    return f"""<div class="step">
  <div class="step-num" style="background:{num_bg}">{n}</div>
  <div class="step-content" style="background:{step_bg}">
    <div class="step-label">{label}</div>
    {content}
  </div>
</div>"""

def result(icon, text, bg, color):
    return f"""<div class="result-box" style="background:{bg};color:{color}">
<span class="r-icon">{icon}</span>
<span>{text}</span>
</div>"""

def hint_card(icon, title, content, bg, color):
    return f"""<div class="hint-card" style="background:{bg};border:1px solid {color}33">
<h4 style="color:{color}">{icon} {title}</h4>
{content}
</div>"""

def answer_box(label="Moje odpověď:", lines=2):
    lns = '\n'.join('<div class="answer-line"></div>' for _ in range(lines))
    return f"""<div class="answer-box">
<div class="a-label">✏️ {label}</div>
{lns}
</div>"""

def scratch(n=5):
    lns = '\n'.join('<div class="scratch-line"></div>' for _ in range(n))
    return f"""<div class="scratch">
<div class="s-label">📝 Místo pro výpočet:</div>
{lns}
</div>"""

def tip(icon, text, bg, border):
    return f"""<div class="tip-box" style="background:{bg};border-color:{border}">
<span class="tip-icon">{icon}</span>
<p>{text}</p>
</div>"""

def divider(text):
    return f"""<div class="divider"><span>✏️ {text}</span></div>"""

# ══════════════════════════════════════════════════════════════════════
# PL09 &mdash; POMĚRY A ZLOMKY
# ══════════════════════════════════════════════════════════════════════
def pl09():
    CD="#B7770D"; CM="#D4AC0D"; CL="#FEF9E7"
    body = cover(9,"Poměry a zlomky","Přímá úměrnost, části celku, záludná slova v zadání","2&ndash;4",CD,CM, "PL09_Pomery_a_zlomky.pdf")

    body += hints_start(CD)
    body += build_hints(HINTS_PL09)
    body += hints_end()

    body += build_quiz(QUIZ_PL09, CD)
    body += build_quiz_answers(QUIZ_PL09, CD)

    body += divider("PŘÍKLADY K PROCVIČENÍ")

    # EXAMPLE 1 — SOLVED
    body += '<div class="example" style="border-color:#D4AC0D">'
    body += ex_header(1,"Kola s různými průměry","2025 &middot; 1. řádný termín","#FEF9E7","#B7770D","✅ Vzorový příklad","✅")
    body += '<div class="ex-body">'
    body += zadani("Mirkovo kolo se otočilo 30× a tátovo 25× — ujeli stejnou vzdálenost.\n3.1 Kolikrát se otočilo Mirkovo kolo, pokud se tátovo otočilo 30×?\n3.2 Tátovo vykonalo o 30 otáček méně než Mirkovo. Kolikrát se otočilo Mirkovo?","#D4AC0D")
    body += '<div class="steps">'
    body += step(1,"Zjistím poměr (z první informace)","Mirkovo : Tátovo = 30 : 25 = <span class='calc'>6 : 5</span><br>→ Mirkovo se otočí vždy 6/5× více než tátovo.","#B7770D","#fffbf0")
    body += step(2,"3.1 — Tátovo = 30, hledám Mirkovo","Mirkovo = 30 × 6 ÷ 5 = <span class='calc'>36 otáček</span><br>Nebo křížem: 30 × 30 = 25 × ? → ? = 900 ÷ 25 = 36","#D4AC0D","#fffbf0")
    body += step(3,"3.2 — Rozdíl = 30, hledám Mirkovo","Každou skupinu: Mirkovo = 6 dílů, Tátovo = 5 dílů → rozdíl = 1 díl<br>1 díl = 30 → Mirkovo = 6 × 30 = <span class='calc'>180 otáček</span>","#B7770D","#fffbf0")
    body += '</div>'
    body += result("✅","3.1: Mirkovo = 36 otáček &nbsp;|&nbsp; 3.2: Mirkovo = 180 otáček","#FEF9E7","#B7770D")
    body += '</div></div>'

    # EXAMPLE 2 — WITH HINTS
    body += '<div class="example" style="border-color:#D4AC0D">'
    body += ex_header(2,"Rozdělení peněz na části","2025 &middot; 1. řádný termín","#fffbf0","#B7770D","💡 S nápovědou","💡")
    body += '<div class="ex-body">'
    body += zadani("Maminka rozdělila peníze mezi tři děti.\nJaně dala pětinu celkové částky.\nIvo dostal dvakrát více peněz než Jana.\nZbylých 240 korun dala Evě.\nKolik korun celkem maminka rozdělila?","#D4AC0D")
    body += hint_card("🧮","Postup — vyplň mezery:","""
<div class="hint-step"><span class="hint-arrow">1.</span><span class="hint-text">Jana = celkem ÷ 5 = <span class="hint-blank"></span> Kč</span></div>
<div class="hint-step"><span class="hint-arrow">2.</span><span class="hint-text">Ivo = 2 × Jana = <span class="hint-blank"></span> Kč</span></div>
<div class="hint-step"><span class="hint-arrow">3.</span><span class="hint-text">Jana + Ivo = <span class="hint-blank"></span>/5 celkové částky</span></div>
<div class="hint-step"><span class="hint-arrow">4.</span><span class="hint-text">Eva = celkem − Jana − Ivo = <span class="hint-blank"></span>/5 celkové = 240 Kč</span></div>
<div class="hint-step"><span class="hint-arrow">5.</span><span class="hint-text">Celkem = 240 × 5 ÷ <span class="hint-blank"></span> = <span class="hint-blank"></span> Kč</span></div>""","#fffbf0","#D4AC0D")
    body += answer_box("Celková částka = _____ Kč")
    body += '</div></div>'

    # EXAMPLES 3–5 — SOLO
    solos = [
        ("3","Velká a malá kulička","2025 &middot; 1. řádný termín",
         "Velká kulička váží 30 g a malá kulička váží 20 g.\nAnička položila na prázdnou váhu určitý počet velkých kuliček a dvojnásobný počet malých kuliček.\nVáha ukázala celkovou hmotnost 560 g.\n4.1 Určete počet všech kuliček (malých i velkých) položených na váze.\n4.2 Určete v gramech celkovou hmotnost všech malých kuliček."),
        ("4","Závodníci na lyžích","2021 &middot; 1. řádný termín",
         "Závod absolvovalo 6 závodníků. První vyběhl v 9:20, další vybíhali v půlminutových intervalech.\nZávodník A skončil v 10:04:30, závodník B v 10:02:00.\nKterý závodník byl rychlejší a o kolik sekund?"),
        ("5","Farmář s kravami","2025 &middot; 1. řádný termín",
         "Farmář měl 7 krav, každá nadojila 15 l mléka denně.\nFarmář 5 prodal, přikoupil nové krávy (každá 20 l/den).\nCelkové množství za 2 dny původních 7 krav = množství za 1 den nynějších.\nKolik krav farmář přikoupil?"),
    ]
    for num, title, src, zad in solos:
        body += f'<div class="example" style="border-color:#ddd">'
        body += ex_header(num, title, src, "#e8f5e9","#1E8449","🖊 Vyřeš sám/sama","🖊")
        body += '<div class="ex-body">'
        body += zadani(zad)
        body += scratch(7)
        body += answer_box()
        body += '</div></div>'

    body += tip("💡","Poměr vždy zapiš jako tabulku (A | B) a doplňuj do ní. Křížové násobení ověř zpětným dosazením!","#fffbf0","#D4AC0D")

    return body

# ══════════════════════════════════════════════════════════════════════
# PL07 &mdash; VÝRAZY A ZÁVORKY (pišeme jako první - kratší, dobrý test)
# ══════════════════════════════════════════════════════════════════════
def pl07():
    CD="#C0392B"; CM="#E74C3C"; CL="#FDEDEC"
    body = cover(7,"Výrazy a závorky","Pořadí operací, hledání neznámého čísla, závorky","3&ndash;4",CD,CM, "PL07_Vyrazy_a_zavorky.pdf")

    body += hints_start(CD)
    body += build_hints(HINTS_PL07)
    body += hints_end()

    body += build_quiz(QUIZ_PL07, "#148F77")
    body += build_quiz_answers(QUIZ_PL07, "#148F77")

    body += divider("PŘÍKLADY K PROCVIČENÍ")

    # EXAMPLE 1 &mdash; FULLY SOLVED
    body += '<div class="example" style="border-color:#E74C3C">'
    body += ex_header(1,"Vypočti výraz krok za krokem","2025 &middot; 1. řádný termín","#FDEDEC","#C0392B","✅ Vzorový příklad &mdash; vše vyřešeno","✅")
    body += '<div class="ex-body">'
    body += zadani("Doplň číslo do rámečku, aby platila rovnost:\n1.1 &nbsp; &#9633; &divide; 11 = (5 + 5 &middot; 20) &minus; 101","#E74C3C")
    body += '<div class="steps">'
    body += step(1,"Nejdřív závorka &mdash; počítám uvnitř","Násobení je před sčítáním: <span class='calc'>5 &middot; 20 = 100</span><br>Pak: <span class='calc'>5 + 100 = 105</span>","#E74C3C","#fff0ef")
    body += step(2,"Pak odčítám","<span class='calc'>105 &minus; 101 = 4</span><br>Pravá strana = <b>4</b>","#C0392B","#fff0ef")
    body += step(3,"Hledám &#9633; pozpátku","Vím, že &#9633; &divide; 11 = 4<br>Pozpátku: 4 &times; 11 = <span class='calc' style='font-size:16px;font-weight:800'>44</span>","#922B21","#fff0ef")
    body += step(4,"Ověřím dosazenĺm","<span class='calc'>44 &divide; 11 = 4</span> a <span class='calc'>(5 + 5&middot;20) &minus; 101 = 4</span> &#10003;","#922B21","#fff0ef")
    body += '</div>'
    body += result("✅","Odpověď: &#9633; = 44","#FDEDEC","#922B21")
    body += '</div></div>'

    # EXAMPLE 2 &mdash; WITH HINTS
    body += '<div class="example" style="border-color:#E74C3C">'
    body += ex_header(2,"Doplň číslo do rámečku","2025 &middot; 1. řádný termín","#fff0ef","#C0392B","💡 S nápovědou","💡")
    body += '<div class="ex-body">'
    body += zadani("1.2 &nbsp; (188 &minus; 152) &divide; (1 + &#9633;) = 4 + 20 &divide; 4","#E74C3C")
    body += hint_card("➡️","Postup &mdash; vyplň mezery:","""
<div class="hint-step"><span class="hint-arrow">1.</span><span class="hint-text">Pravá strana: nejdřív dělení: 20 &divide; 4 = <span class="hint-blank"></span>, pak: 4 + <span class="hint-blank"></span> = <span class="hint-blank"></span></span></div>
<div class="hint-step"><span class="hint-arrow">2.</span><span class="hint-text">Levá strana: závorka: 188 &minus; 152 = <span class="hint-blank"></span></span></div>
<div class="hint-step"><span class="hint-arrow">3.</span><span class="hint-text">Teď: <span class="hint-blank"></span> &divide; (1 + &#9633;) = <span class="hint-blank"></span> &rarr; (1 + &#9633;) = <span class="hint-blank"></span> &divide; <span class="hint-blank"></span> = <span class="hint-blank"></span></span></div>
<div class="hint-step"><span class="hint-arrow">4.</span><span class="hint-text">Tedy &#9633; = <span class="hint-blank"></span> &minus; 1 = <span class="hint-blank"></span></span></div>""","#fff5f5","#E74C3C")
    body += answer_box("&#9633; = _____ (ověř dosazením!)")
    body += '</div></div>'

    # EXAMPLE 3 &mdash; WITH HINTS
    body += '<div class="example" style="border-color:#E74C3C">'
    body += ex_header(3,"Hledej neznámé číslo pozpátku","2025 &middot; 2. řádný termín","#fff0ef","#C0392B","💡 S nápovědou","💡")
    body += '<div class="ex-body">'
    body += zadani("Neznámé číslo vydělím 7, přičtu 3 a výsledek zdvojnásobím &mdash; dostanu 20. Jaké je neznámé číslo?","#E74C3C")
    body += hint_card("⬅️","Jdi pozpátku od výsledku 20:","""
<div class="calc-demo">
  Výsledek: <span class="hl">20</span><br>
  &divide; 2 (opak zdvojnásobení): 20 &divide; 2 = <span class="hint-blank" style="display:inline-block;width:40px;border-bottom:2px solid #ccc"></span><br>
  &minus; 3 (opak přičtení 3): &nbsp;&nbsp;<span class="hint-blank" style="display:inline-block;width:40px;border-bottom:2px solid #ccc"></span> &minus; 3 = <span class="hint-blank" style="display:inline-block;width:40px;border-bottom:2px solid #ccc"></span><br>
  &times; 7 (opak dělení 7): &nbsp;&nbsp;&nbsp;&nbsp;<span class="hint-blank" style="display:inline-block;width:40px;border-bottom:2px solid #ccc"></span> &times; 7 = <span class="hint-blank" style="display:inline-block;width:40px;border-bottom:2px solid #ccc"></span> ← to je neznámé číslo!
</div>""","#fff5f5","#C0392B")
    body += answer_box("Neznámé číslo = _____")
    body += '</div></div>'

    # EXAMPLES 4,5,6 &mdash; SOLO
    solos = [
        ("4","Vypočti výrazy","2023 &middot; 1. řádný termín",
         "1.1 &nbsp; 5 &middot; 120 + (700 &minus; 6 &middot; 25) &divide; (10 &minus; 7 + 2) = ?\n1.2 &nbsp; (5 + 5 &middot; 29) &minus; 4 &middot; (176 &divide; 8 &minus; 8 &middot; 2) = ?",
         "vyrazy_23r1_1_2"),
        ("5","Slovní úloha &mdash; součet a rozdíl","2025 &middot; 2. řádný termín",
         "1.1 Součet dvou čísel je 109 a jejich rozdíl je 13. Jaká jsou obě čísla?\n1.2 Neznámé číslo zvětšené o svou POLOVINU se rovná 198. Jaké je číslo?\n1.3 Součet dvou neznámých čísel je 109 a jejich rozdíl je 13. Urči obě čísla.",
         "vyrazy_25r2_1_2"),
        ("6","Vypočti","2024 &middot; 2. náhradní termín",
         "2.1 &nbsp; (510 &divide; 34) &minus; (8 + 56 &divide; 8) = ?\n2.2 &nbsp; 10 &middot; 100 &minus; (100 &minus; 6 &middot; 14) &divide; 2 = ?\n2.3 &nbsp; 72 &divide; 4 + 8 &minus; 10 &divide; 1 + 1 = ?",
         "vyrazy_24n2_1_2"),
    ]
    for num, title, src, zad, img_name in solos:
        body += f'<div class="example" style="border-color:#ddd">'
        body += ex_header(num, title, src, "#e8f5e9","#1E8449","🖊 Vyřeš sám/sama","🖊")
        body += '<div class="ex-body">'
        # Obrazky v techto ulohach nejsou nutne - zadani je uplne v textu nize
        body += zadani(zad)
        body += scratch(7)
        body += answer_box()
        body += '</div></div>'

    body += tip("💡","Nezkoušej počítat v hlavě! Piš VŠECHNY mezivýsledky. Jedna malá chyba na začátku = špatná odpověď na konci.","#fff5f5","#E74C3C")

    return body

# ══════════════════════════════════════════════════════════════════════
# PL08 &mdash; JEDNOTKY A PŘEVODY
# ══════════════════════════════════════════════════════════════════════
def pl08():
    CD="#784212"; CM="#A56A2A"; CL="#FAE5D3"
    body = cover(8,"Jednotky a převody","Délky, hmotnost, čas &mdash; jak převádět a počítat","3",CD,CM, "PL08_Jednotky_a_prevody.pdf")

    body += hints_start(CD)
    body += build_hints(HINTS_PL08)
    body += hints_end()

    body += build_quiz(QUIZ_PL08, "#784212")
    body += build_quiz_answers(QUIZ_PL08, "#784212")

    body += divider("PŘÍKLADY K PROCVIČENÍ")

    # SOLVED
    body += '<div class="example" style="border-color:#A56A2A">'
    body += ex_header(1,"Vzdálenost vlaku od lomu k mostu","2025 &middot; 1. náhradní termín","#FAE5D3","#784212","✅ Vzorový příklad","✅")
    body += '<div class="ex-body">'
    body += zadani("Vlak vyjel v poledne a za každých 8 minut ujede 7 km.\nVe 12:20 minul lom, ve 12:36 dojel na most.\nUrčete vzdálenost od lomu k mostu.","#A56A2A")
    body += '<div class="steps">'
    body += step(1,"Zjistím čas cesty od lomu k mostu","Čas = 12:36 &minus; 12:20 = <span class='calc'>16 minut</span>","#A56A2A","#fdf5ec")
    body += step(2,"Porovnám s tempem vlaku","Tempo: za 8 minut = 7 km<br>16 minut = <span class='calc'>2 &times; 8 minut</span>","#784212","#fdf5ec")
    body += step(3,"Vypočtu vzdálenost","Vzdálenost = <span class='calc'>2 &times; 7 km = 14 km</span><br><small>Dvakrát delší čas &rarr; dvakrát větší vzdálenost</small>","#5D3A1A","#fdf5ec")
    body += '</div>'
    body += result("🚂","Odpověď: 14 km","#FAE5D3","#5D3A1A")
    body += '</div></div>'

    # HINT 2
    body += '<div class="example" style="border-color:#A56A2A">'
    body += ex_header(2,"Doplň chybějící jednotku","2025 &middot; 2. řádný termín","#fdf5ec","#784212","💡 S nápovědou","💡")
    body += '<div class="ex-body">'
    body += zadani("2.1 &nbsp; 18 m &minus; 15 dm + &#9633; cm = 20 m\n2.2 &nbsp; 4 &middot; &#9633; g &minus; 3 kg = 1/5 kg\n2.3 &nbsp; 1/4 h + &#9633; s = 20 min","#A56A2A")
    body += hint_card("📏","Postup pro 2.1 &mdash; převeď vše na cm:","""
<div class="ex-table" style="width:100%">
<table class="ex-table">
<tr><th style="background:#784212;color:white">18 m = ?</th><th style="background:#784212;color:white">15 dm = ?</th><th style="background:#784212;color:white">20 m = ?</th></tr>
<tr><td class="fill">_____ cm</td><td class="fill">_____ cm</td><td class="fill">_____ cm</td></tr>
</table>
</div>
<p>Pak: _____ &minus; _____ + &#9633; = _____ &rarr; &#9633; = _____ cm</p>""","#fdf5ec","#A56A2A")
    body += hint_card("⚖️","Postup pro 2.2 &mdash; převeď na gramy:","""
<p>3 kg = _____ g &nbsp;|&nbsp; 1/5 kg = _____ g</p>
<p>Pak: 4 &middot; &#9633; &minus; _____ = _____ &rarr; 4 &middot; &#9633; = _____ &rarr; &#9633; = _____ g</p>""","#fdf5ec","#A56A2A")
    body += hint_card("⏱️","Postup pro 2.3 &mdash; převeď na sekundy:","""
<p>1/4 hodiny = 60 &divide; 4 = _____ minut = _____ sekund</p>
<p>20 minut = _____ sekund</p>
<p>Pak: _____ + &#9633; = _____ &rarr; &#9633; = _____ sekund</p>""","#fdf5ec","#784212")
    body += answer_box("2.1: &#9633; = _____ cm &nbsp;&nbsp; 2.2: &#9633; = _____ g &nbsp;&nbsp; 2.3: &#9633; = _____ s")
    body += '</div></div>'

    # HINT 3
    body += '<div class="example" style="border-color:#A56A2A">'
    body += ex_header(3,"Zlomky hodin a metrů","2024 &middot; 2. náhradní termín","#fdf5ec","#784212","💡 S nápovědou","💡")
    body += '<div class="ex-body">'
    body += zadani("5.1 &nbsp; 1/3 hodiny &minus; 1/6 hodiny = &#9633; sekund\n5.2 &nbsp; 1 metr &minus; 1/4 metru = &#9633; centimetrů + 250 milimetrů","#A56A2A")
    body += hint_card("⏱️","Nápověda pro 5.1:","""
<p>1/3 hodiny = 60 &divide; 3 = _____ min = _____ s</p>
<p>1/6 hodiny = 60 &divide; 6 = _____ min = _____ s</p>
<p>Rozdíl = _____ s &minus; _____ s = _____ s</p>""","#fdf5ec","#784212")
    body += hint_card("📏","Nápověda pro 5.2:","""
<p>Čtvrtina metru = 100 &divide; 4 = 25 cm. Takže: 1 m &minus; 25 cm = 75 cm.</p>
<p>75 cm = 750 mm.</p>
<p>750 mm = &#9633; cm + 250 mm. Odečtu: 750 &minus; 250 = 500 mm. A 500 mm = _____ cm.</p>""","#fdf5ec","#A56A2A")
    body += answer_box("5.1: &#9633; = _____ sekund &nbsp;&nbsp; 5.2: &#9633; = _____ cm")
    body += '</div></div>'

    # SOLO 4,5,6
    solos = [
        ("4","Délka druhé úsečky lomené čáry","2023 &middot; 1. náhradní termín","jedn_23n1_2",
         "Lomená čára se skládá ze dvou úseček.\nCelková délka: 2 m 4 cm 2 mm.\nPrvní úsečka: 52 cm 6 mm.\nVypočti délku druhé úsečky v mm.\n\n💡 Tip: převeď vše na mm, pak odečti."),
        ("5","Plavec v bazénu","2025 &middot; 2. náhradní termín","jedn_25n2_1",
         "Plavec uplave rovnoměrným tempem 2 kilometry za 48 minut.\nZa kolik minut uplave 5 padesátimetrových bazénů?\n\n💡 Tip: 5 bazénů po 50 m = 250 m. Za 48 min = 2 km = 2000 m. Kolik minut na 250 m?"),
        ("6","Čas odchodu z domu","2024 &middot; 1. náhradní termín","jedn_24n1_13",
         "Katka jede do školy na kole. Cesta DO KOPCE (do školy) trvá dvakrát déle než cesta ZE ŠKOLY (z kopce).\nOběma cestami dohromady (tam + zpět) stráví na kole 33 minut.\n\n💡 Postup:\nCesta ze školy = &#9633; minut. Cesta do školy trvá dvakrát déle = 2 &times; &#9633; minut.\nDohromady: &#9633; + 2&times;&#9633; = 3&times;&#9633; = 33 minut Dělíme 3: &#9633; = _____ min (cesta ze školy). Cesta do školy = 2 &times; _____ = _____ min.\n\nVyučování začíná v 8:00. Katka chce být 10 min dříve = v 7:50.\nV kolik hodin nejpozději musí vyjet z domu?"),
    ]
    for num, title, src, img_name, zad in solos:
        body += f'<div class="example" style="border-color:#ddd">'
        body += ex_header(num, title, src, "#e8f5e9","#1E8449","🖊 Vyřeš sám/sama","🖊")
        body += '<div class="ex-body">'
        im = exam_img(img_name,"Zadání z přijímaček")
        if im: body += im
        body += zadani(zad)
        body += scratch(6)
        body += answer_box()
        body += '</div></div>'

    body += ex_header(5,"Zlomky hodin a metrů — doplň do rámečku","2024 &middot; 2. náhradní termín","#fdf5ec","#784212","🖊 Vyřeš sám/sama","🖊")
    body += '<div class="ex-body">'
    body += zadani("""Doplňte do rámečku číslo, aby platila rovnost:
<ol class="task-list">
<li>1/3 hodiny &minus; 1/6 hodiny = &nbsp;&nbsp;&nbsp;□&nbsp;&nbsp;&nbsp; sekund</li>
<li>1 metr &minus; 1/4 metru = &nbsp;&nbsp;&nbsp;□&nbsp;&nbsp;&nbsp; centimetrů + 250 milimetrů</li>
</ol>
<i>Tip: nejdřív vypočítej hodnotu zlomku v základní jednotce (minuty, cm), pak převeď na požadovanou.</i>""")
    body += scratch(5)
    body += answer_box()
    body += '</div></div>'

    body += tip("⏰","Vždy nejdřív převeď VŠE na jednu jednotku, a teprve pak počítej. Smíchané jednotky způsobují chyby!","#fdf5ec","#A56A2A")

    return body

# ══════════════════════════════════════════════════════════════════════
# PL04 &mdash; GRAFY
# ══════════════════════════════════════════════════════════════════════
def pl04():
    CD="#6C3483"; CM="#9B59B6"; CL="#F4ECF7"
    body = cover(4,"Grafy &mdash; pravdivé nebo nepravdivé?","Čti graf přesně, počítej, rozhodni: A nebo N","4",CD,CM, "PL04_Grafy_pravdive_nepravdive.pdf")

    body += hints_start(CD)
    body += build_hints(HINTS_PL04)
    body += hints_end()

    body += build_quiz(QUIZ_PL04, "#6C3483")
    body += build_quiz_answers(QUIZ_PL04, "#6C3483")

    body += divider("PŘÍKLADY K PROCVIČENÍ")

    # SOLVED
    body += '<div class="example" style="border-color:#9B59B6">'
    body += ex_header(1,"Turistický oddíl &mdash; muži a ženy 2015&ndash;2018","2025 &middot; 1. řádný termín","#F4ECF7","#6C3483","✅ Vzorový příklad","✅")
    body += '<div class="ex-body">'
    body += exam_img("grafy_25r1_8","Graf turistického oddílu")
    body += zadani("Rozhodni, zda je každé tvrzení pravdivé (A) nebo nepravdivé (N).\n8.1 Počet mužů v roce 2015 byl o jednu třetinu menší než v roce 2016.\n8.2 Počet členů v roce 2017 byl o jednu devítinu větší než v roce 2016.\n8.3 Počet žen se poprvé snížil oproti předchozímu roku až v roce 2018.","#9B59B6")
    body += '<div class="steps">'
    body += step(1,"Odečtu hodnoty z grafu","Muži 2015 &asymp; 60, muži 2016 &asymp; 90<br>Ženy: 2015 &asymp; 30, 2016 &asymp; 35, 2017 &asymp; 37, 2018 &asymp; 30","#9B59B6","#f9f0ff")
    body += step(2,"Ověřím tvrzení 8.1","O třetinu méně než 90 = 90 &minus; 90&divide;3 = 90 &minus; 30 = <span class='calc'>60</span><br>Graf ukazuje: muži 2015 = 60 &#10003; &rarr; <b>A (Pravdivé)</b>","#6C3483","#f9f0ff")
    body += step(3,"Ověřím tvrzení 8.2","Tvrzení mluví o 'počtu členů' &mdash; to je muži + ženy dohromady.<br>2016: muži 90 + ženy 36 = 126 členů. O devítinu více = 126 + 126&divide;9 = 126 + 14 = 140.<br>2017: muži 90 + ženy 36 = 126 (stejné). 126 &ne; 140 &rarr; <b>N (Nepravdivé)</b>","#6C3483","#f9f0ff")
    body += step(4,"Ověřím tvrzení 8.3","Ženy: 2015&rarr;2016 vzrostly (+5) &#10003;, 2016&rarr;2017 vzrostly (+2) &#10003;, 2017&rarr;2018 klesly (&minus;7) &rarr; POPRVÉ kleslo v 2018 &rarr; <b>A (Pravdivé)</b>","#5B2C8D","#f9f0ff")
    body += '</div>'
    body += result("✅","8.1: A &nbsp;|&nbsp; 8.2: N &nbsp;|&nbsp; 8.3: A","#F4ECF7","#5B2C8D")
    body += '</div></div>'

    # HINT 2
    body += '<div class="example" style="border-color:#9B59B6">'
    body += ex_header(2,"Kasička &mdash; Věra, Pavel, Tomáš","2025 &middot; 2. řádný termín","#f9f0ff","#6C3483","💡 S nápovědou","💡")
    body += '<div class="ex-body">'
    body += exam_img("grafy_25r2_8","Graf počtu 50Kč mincí")
    body += zadani("8.1 Věra vložila v lednu tolik Kč, kolik za zbývající 3 měsíce dohromady.\n8.2 V únoru vložili Pavel s Věrou dohromady 3&times; více Kč než Tomáš.\n8.3 Tomáš vložil v dubnu více než 1/9 všech peněz za 4 měsíce od všech tří.","#9B59B6")
    body += hint_card("📝","Nejprve si zapiš hodnoty z grafu (počty mincí &times; 50 Kč):","""
<table class="ex-table"><tr><th style="background:#6C3483;color:white">Osoba</th><th style="background:#6C3483;color:white">Leden</th><th style="background:#6C3483;color:white">Únor</th><th style="background:#6C3483;color:white">Březen</th><th style="background:#6C3483;color:white">Duben</th></tr>
<tr><td>Věra (mince)</td><td class="fill"></td><td class="fill"></td><td class="fill"></td><td class="fill"></td></tr>
<tr><td>Pavel (mince)</td><td class="fill"></td><td class="fill"></td><td class="fill"></td><td class="fill"></td></tr>
<tr><td>Tomáš (mince)</td><td class="fill"></td><td class="fill"></td><td class="fill"></td><td class="fill"></td></tr>
</table>
<p>Pak pro každé tvrzení vypočti konkrétní čísla a porovnej.</p>""","#f9f0ff","#9B59B6")
    body += answer_box("8.1: ___   8.2: ___   8.3: ___   (A = pravdivé, N = nepravdivé)")
    body += '</div></div>'

    # HINT 3
    body += '<div class="example" style="border-color:#9B59B6">'
    body += ex_header(3,"Rodný dům &mdash; děti a dospělí","2025 &middot; 1. náhradní termín","#f9f0ff","#6C3483","💡 S nápovědou","💡")
    body += '<div class="ex-body">'
    body += exam_img("grafy_25n1_8","Graf návštěvnosti rodného domu")
    body += zadani("8.1 V prvních 3 měsících bylo dospělých 3&times; více než dětí.\n8.2 Dospělých v srpnu bylo o polovinu více než v červnu.\n8.3 Za celou sezonu bylo dětí o 340 méně než dospělých.","#9B59B6")
    body += hint_card("📝","Zapiš si hodnoty a doplň tabulku:","""
<table class="ex-table"><tr><th style="background:#6C3483;color:white">Měsíc</th><th style="background:#6C3483;color:white">Děti</th><th style="background:#6C3483;color:white">Dospělí</th></tr>
<tr><td>Květen</td><td class="fill"></td><td class="fill"></td></tr>
<tr><td>Červen</td><td class="fill"></td><td class="fill"></td></tr>
<tr><td>Červenec</td><td class="fill"></td><td class="fill"></td></tr>
<tr><td>Srpen</td><td class="fill"></td><td class="fill"></td></tr>
<tr><td>Září</td><td class="fill"></td><td class="fill"></td></tr>
<tr><td><b>CELKEM</b></td><td class="fill"></td><td class="fill"></td></tr>
</table>
<p>8.2: o polovinu více než červen = červen + červen&divide;2 = ?</p>""","#f9f0ff","#6C3483")
    body += answer_box("8.1: ___   8.2: ___   8.3: ___")
    body += '</div></div>'

    # SOLO 4,5,6
    solos = [
        ("4","Skautské oddíly &mdash; přiřaď odpovědi","2023 &middot; 1. řádný termín",
         "grafy_23r1_13","Graf udává kg odpadu (papír, plast, kovy) pro oddíly R, S, T.\nPřiřaď ke každé větě správnou část:\nA: o šestinu, B: o pětinu, C: o čtvrtinu, D: o třetinu, E: o polovinu, F: dvakrát\n\n13.1 Oddíl R vytřídil _______ méně papíru než S.  ____\n13.2 Oddíly S a T vytřídily _______ více plastu než R.  ____\n13.3 Všechny oddíly vytřídily _______ více papíru než kovů.  ____"),
        ("5","Brigádník &mdash; sbírání ovoce","2024 &middot; 2. náhradní termín",
         "grafy_24n2_13","Graf znázorňuje, kolik kg jablek, hrušek a hroznového vína Pepa nasbíral každý den týdne.\n\n💡 Postup: Nejdřív si sečti kg každého druhu za celý týden (sečti všechny sloupečky dané barvy).\n\n13.1 Kdyby nasbíral za celý týden o 25 kg více jablek, bylo by to stejně jako hrušek?  A / N\n13.2 Z daných druhů nasbíral za týden nejvíce hroznového vína?  A / N\n13.3 Jedna devítina hroznového vína = jedna šestina hrušek za týden?  A / N\n   (Tip: hroznové víno &divide; 9 = ? &nbsp; hrušky &divide; 6 = ? &nbsp; jsou stejné?)"),
        ("6","Šetření sourozenců","2024 &middot; 1. náhradní termín",
         "grafy_24n1_12","Graf znázorňuje, kolik Kč Sára, Dana a Lukáš každý měsíc ušetřili nebo utratili. Sloupeček nahoru = ušetřeno, dolů = utraceno.\n\n💡 Postup: Pro každého sečti všechny měsíce kdy ušetřil (sloupec nahoru) a všechny kdy utratil (dolů). Pak porovnej.\n\n12.1 Lukáš měl na konci června méně než měl 1. ledna?  A / N\n   (Tip: začínal s 600 Kč. Přidej/odečti každý měsíc.)\n12.2 Sára za první pololetí celkově ušetřila?  A / N\n12.3 Dana utratila více, než ušetřila?  A / N"),
    ]
    for num, title, src, img_name, zad in solos:
        body += f'<div class="example" style="border-color:#ddd">'
        body += ex_header(num, title, src, "#e8f5e9","#1E8449","🖊 Vyřeš sám/sama","🖊")
        body += '<div class="ex-body">'
        if img_name:
            body += exam_img(img_name)
        body += zadani(zad)
        body += scratch(6)
        body += answer_box()
        body += '</div></div>'

    body += tip("🔍","Nezapomeň si vždy napsat čísla z grafu do tabulky &mdash; pak je mnohem snazší počítat. Chyby jsou skoro vždy v chybně odečtené hodnotě!","#f9f0ff","#9B59B6")

    return body

# ══════════════════════════════════════════════════════════════════════
# PL05 &mdash; SOUSTAVY PODMÍNEK
# ══════════════════════════════════════════════════════════════════════
def pl05():
    CD="#1E8449"; CM="#27AE60"; CL="#D5F5E3"
    body = cover(5,"Soustavy podmínek","Slovní úlohy: tabulka, krok za krokem, ověření","3&ndash;5",CD,CM, "PL05_Soustavy_podminek.pdf")

    body += hints_start(CD)
    body += build_hints(HINTS_PL05)
    body += hints_end()

    body += build_quiz(QUIZ_PL05, "#1E8449")
    body += build_quiz_answers(QUIZ_PL05, "#1E8449")

    body += divider("PŘÍKLADY K PROCVIČENÍ")

    # SOLVED
    body += '<div class="example" style="border-color:#27AE60">'
    body += ex_header(1,"Martinovy kuličky","2025 &middot; 2. náhradní termín","#D5F5E3","#1E8449","✅ Vzorový příklad","✅")
    body += '<div class="ex-body">'
    body += zadani("Martin má jednobarevné kuličky. Třetina je žlutých, 12 červených, zbývající modré.\nModrých má o polovinu více než červených.\n3.1 Kolik má Martin všech kuliček?\n3.2 Kolik červených dá kamarádce, aby polovina jeho zbylých kuliček byla modrá?","#27AE60")
    body += '<div class="steps">'
    body += step(1,"Zjistím počet modrých","O polovinu více než červených = červené + polovina červených<br><span class='calc'>12 + 12&divide;2 = 12 + 6 = 18 modrých</span>","#27AE60","#eafaf1")
    body += step(2,"Červené + modré = kolik?","<span class='calc'>12 + 18 = 30 kuliček</span><br>To jsou 2/3 ze všech (žluté jsou třetina = 1/3)","#1E8449","#eafaf1")
    body += step(3,"Zjistím celkový počet","30 kuliček = 2/3 ze všech<br><span class='calc'>30 &divide; 2 &times; 3 = 45 kuliček celkem</span><br>Ověř: žluté = 45&divide;3 = 15, 15+12+18 = 45 &#10003;","#145A32","#eafaf1")
    body += step(4,"Kolik červených dá kamarádce?","Po darování: zbyde 45 &minus; dárek kuliček. Polovina zbylých = modré (18).<br>Zbylých musí být 2&times;18 = 36. Tedy: 45 &minus; 36 = <span class='calc'>9 červených dá</span>","#145A32","#eafaf1")
    body += '</div>'
    body += result("✅","3.1: 45 kuliček &nbsp;|&nbsp; 3.2: 9 červených kuliček","#D5F5E3","#145A32")
    body += '</div></div>'

    # HINT 2
    body += '<div class="example" style="border-color:#27AE60">'
    body += ex_header(2,"Dům se třemi patry","2025 &middot; 1. řádný termín","#eafaf1","#1E8449","💡 S nápovědou","💡")
    body += '<div class="ex-body">'
    body += exam_img("podm_25r1_5","Zadání z přijímaček")
    body += zadani("Dům má 3 patra, bydlí tam 11 dětí. V 1.+2. patře celkem 8 dětí.\nVe 2. patře bydlí jen dívky. V 1.+3. patře: 5 chlapců a 3 dívky.\nZe všech chlapců bydlí mimo 3. patro jen 3 chlapci.\n5.1 Kolik chlapců bydlí ve 2. patře?  5.2 Kolik dětí v 1. patře?  5.3 Kolik dívek celkem?","#27AE60")
    body += hint_card("📋","Vyplni tabulku &mdash; začni od podmínek:","""
<table class="ex-table" style="width:100%">
<tr><th style="background:#1E8449;color:white">Patro</th><th style="background:#1E8449;color:white">Chlapci</th><th style="background:#1E8449;color:white">Dívky</th><th style="background:#1E8449;color:white">Celkem</th></tr>
<tr><td>1.</td><td class="fill"></td><td class="fill"></td><td class="fill"></td></tr>
<tr><td>2.</td><td style="background:#ffe;color:#999">0 (jen dívky!)</td><td class="fill"></td><td class="fill"></td></tr>
<tr><td>3.</td><td class="fill"></td><td class="fill"></td><td class="fill"></td></tr>
<tr><td><b>CELKEM</b></td><td class="fill"></td><td class="fill"></td><td style="font-weight:700">11</td></tr>
</table>
<p style="margin-top:6px;font-size:13px">Nápověda: &bdquo;mimo 3. patro jen 3 chlapci" = v 1.+2. patře dohromady 3 chlapci. Ve 2. patře 0 &rarr; v 1. patře = ?</p>""","#eafaf1","#27AE60")
    body += answer_box("5.1: _____ chlapců &nbsp;&nbsp; 5.2: _____ dětí &nbsp;&nbsp; 5.3: _____ dívek")
    body += '</div></div>'

    # HINT 3
    body += '<div class="example" style="border-color:#27AE60">'
    body += ex_header(3,"Jana a sešity","2023 &middot; 1. řádný termín","#eafaf1","#1E8449","💡 S nápovědou","💡")
    body += '<div class="ex-body">'
    body += exam_img("podm_23r1_4","Zadání z přijímaček")
    body += zadani("4.1 Jana koupila celkem 36 sešitů. Linkovaných 3&times; více než čtverečkovaných. Kolik linkovaných?\n4.2 2 linkované + 2 čtverečkované = 180 Kč. 2 čtverečkované stojí jako 3 linkované. Cena 1 čtverečkovaného?\n4.3 K nákupu 6 kružítek chybělo 160 Kč. Koupila 4 a zbylo 100 Kč. Zaplatila za 4?","#27AE60")
    body += hint_card("➡️","Nápověda pro 4.1:","""
<p>Označ čtverečkované = &#9633;. Linkované = &#9633; + &#9633; + &#9633; (třikrát tolik).</p>
<p>Dohromady: &#9633; + &#9633;+&#9633;+&#9633; = 4 skupiny &#9633; = 36. Takže 1 skupina = _____ a linkovaných = _____</p>""","#eafaf1","#27AE60")
    body += hint_card("➡️","Nápověda pro 4.2 &mdash; krok za krokem:","""
<p>Víme: 2 čtverečkované stojí stejně jako 3 linkované.</p>
<p>V první podmínce jsou 2 linkované + 2 čtverečkované = 180 Kč.</p>
<p>Nahradíme 2 čtverečkované jejich cenou: místo nich napíšeme &bdquo;3 linkované".</p>
<p>Dostaneme: 2 linkované + 3 linkované = 5 linkovaných = 180 Kč. Takže 1 linkovaný = 180 &divide; 5 = _____</p>""","#eafaf1","#1E8449")
    body += answer_box("4.1: _____ linkovaných &nbsp;&nbsp; 4.2: _____ Kč &nbsp;&nbsp; 4.3: _____ Kč")
    body += '</div></div>'

    # SOLO 4,5,6
    solos = [
        ("4","Korálky na šňůrce","2025 &middot; 2. řádný termín",
         "podm_25r1_3_4",
         "Korálky jsou ve 4 skupinách. 1. skupina nejmenší, každá další 4&times; více než předchozí. Ve 3. skupině je 32 korálků.\n3.1 Kolik korálků je celkem na šňůrce?\n3.2 Kolikrát více korálků má 4. skupina než 2. skupina?\n3.3 Na šňůrce se střídají: 4 černé, 1 bílý, 4 černé, 1 bílý... Kolik černých je ve 4. skupině?"),
        ("5","Vědomostní soutěž","2025 &middot; 2. náhradní termín","podm_25n2_4tbl",
         "Vědomostní soutěže se zúčastnilo 10 členů týmu. V každém kole dostali 8, 9 nebo 10 bodů.\nV 1. kole bylo těch co dostali 8 bodů o jednoho méně než těch co dostali 10 bodů.\n\n4.1 Urči součet bodů celého týmu v 1. kole.\n💡 Tip pro 4.1: Zkus různé možnosti do tabulky &mdash; zjistíš něco překvapivého!\n| počet desetkařů | 5 | 4 | 3 |\n| počet osmičkářů | 4 | 3 | 2 |\n| počet devítkářů | 1 | 3 | 5 |\n| Součet bodů      | ? | ? | ? |\n\n4.2 Ve 2. kole: 3 dostali 8 bodů, 5 dostalo 10 bodů. Kolik mohlo dostat 9 bodů? Najdi všechna řešení."),
        ("6","Odměny pro soutěžící","2023 &middot; 1. řádný termín","podm_23r1_6",
         "Na odměny byl připraven určitý obnos. 1. soutěžící dostal polovinu celé částky. 2. soutěžící dostal 300 Kč.\n3. soutěžící dostal zbytek &mdash; přitom 1. soutěžící dostal 3&times; VÍCE než 3. soutěžící.\n6.1 Kolikrát více Kč dostal 2. soutěžící než 3. soutěžící?\n6.2 Kolik Kč bylo celkem připraveno na odměny?"),
    ]
    for num, title, src, img_name, zad in solos:
        body += f'<div class="example" style="border-color:#ddd">'
        body += ex_header(num, title, src, "#e8f5e9","#1E8449","🖊 Vyřeš sám/sama","🖊")
        body += '<div class="ex-body">'
        if img_name:
            body += exam_img(img_name)
        body += zadani(zad)
        body += scratch(7)
        body += answer_box()
        body += '</div></div>'

    body += ex_header(4,"Vědomostní soutěž &mdash; tým a body","2025 &middot; 2. náhradní termín","#eafaf1","#1E8449","🖊 Vyřeš sám/sama","🖊")
    body += '<div class="ex-body">'
    body += zadani("""Vědomostní soutěže se zúčastnil 10členný tým. Ve dvou kolech získali soutěžící 8, 9 nebo 10 bodů. Celkem tým získal 93 bodů v 1. kole a 94 bodů v 2. kole.
<ol class="task-list">
<li>Kolik soutěžících získalo v 1. kole 10 bodů, jestliže 8 bodů získali 4 soutěžící a zbytek 9?</li>
<li>Určete, kolik soutěžících mohlo získat v obou kolech dohromady méně než 18 bodů.</li>
</ol>""")
    body += scratch(7)
    body += answer_box()
    body += '</div></div>'

    body += ex_header(5,"Penzion &mdash; skupiny a pokoje","2025 &middot; 1. náhradní termín","#eafaf1","#1E8449","🖊 Vyřeš sám/sama","🖊")
    body += '<div class="ex-body">'
    body += zadani("""Skupina 18 osob přijela do penzionu na jednu noc. Tabulka udává počty volných pokojů a ceny lůžek. Každý pronajatý pokoj musí být plně obsazen.
<table class="ex-table" style="width:100%;margin:10px 0;table-layout:fixed">
<colgroup><col style="width:42%"><col style="width:29%"><col style="width:29%"></colgroup>
<tr><th style="background:#1E8449;color:white;text-align:left">Typ pokoje</th><th style="background:#1E8449;color:white">Počet volných pokojů</th><th style="background:#1E8449;color:white">Cena za lůžko</th></tr>
<tr><td style="text-align:left">Jednolůžkový</td><td>6</td><td>1 400 Kč</td></tr>
<tr><td style="text-align:left">Dvoulůžkový</td><td>5</td><td>700 Kč</td></tr>
<tr><td style="text-align:left">Třílůžkový</td><td>5</td><td>500 Kč</td></tr>
<tr><td style="text-align:left">Čtyřlůžkový</td><td>2</td><td>300 Kč</td></tr>
</table>
<ol class="task-list">
<li>Kolik pokojů obsadili, jestliže vzali 2 pokoje pro 3 osoby a zbytek skupiny do pokojů pro 4 osoby?</li>
<li>Jaká je nejnižší možná cena za ubytování celé skupiny?</li>
</ol>""")
    body += scratch(7)
    body += answer_box()
    body += '</div></div>'

    body += ex_header(6,"Dvě neznámá čísla &mdash; součet a rozdíl","2025 &middot; 2. řádný termín","#eafaf1","#1E8449","🖊 Vyřeš sám/sama","🖊")
    body += '<div class="ex-body">'
    body += zadani("""<ol class="task-list">
<li>Součet dvou neznámých čísel je 109 a jejich rozdíl je 13. Určete obě neznámá čísla.</li>
<li>Neznámé číslo zvětšené o jednu jeho polovinu se rovná 198. Určete neznámé číslo.</li>
</ol>""")
    body += scratch(6)
    body += answer_box()
    body += '</div></div>'

    body += ex_header(7,"Nákupy za mince — hledej nejmenší počet","2021 &middot; 2. řádný termín","#eafaf1","#1E8449","🖊 Vyřeš sám/sama","🖊")
    body += '<div class="ex-body">'
    body += zadani("""V dětské hře: za 5 mincí = 6 panáčků, za 20 mincí = 9 zvířátek.
<ol class="task-list">
<li>Žofie koupila 12 panáčků a určitý počet zvířátek. Celkem zaplatila 90 mincí. Kolik zvířátek koupila?</li>
<li>Pepa chce koupit stejný počet panáčků jako zvířátek. Jaký je nejmenší počet mincí, které potřebuje?</li>
</ol>""")
    body += scratch(6)
    body += answer_box()
    body += '</div></div>'

    body += tip("✅","Vždy na konci OVĚŘ: dosad výsledky zpátky do KAŽDÉ podmínky v zadání. Sedí vše? Pak máš správně!","#eafaf1","#27AE60")

    return body

# ══════════════════════════════════════════════════════════════════════
# PL06 &mdash; OBVOD A OBSAH
# ══════════════════════════════════════════════════════════════════════
def pl06():
    CD="#515A5A"; CM="#7F8C8D"; CL="#F2F3F4"
    body = cover(6,"Obvod a obsah","Vzorce, složené obrazce, čtvercová síť","3&ndash;5",CD,CM, "PL06_Obvod_a_obsah.pdf")

    body += hints_start(CD)
    body += build_hints(HINTS_PL06)
    body += hints_end()

    body += build_quiz(QUIZ_PL06, "#515A5A")
    body += build_quiz_answers(QUIZ_PL06, "#515A5A")

    body += divider("PŘÍKLADY K PROCVIČENÍ")

    # SOLVED
    body += '<div class="example" style="border-color:#7F8C8D">'
    body += ex_header(1,"Obdélníky ze čtverečků &mdash; obvod 18 cm","2025 &middot; 2. řádný termín","#F2F3F4","#515A5A","✅ Vzorový příklad","✅")
    body += '<div class="ex-body">'
    body += exam_img("obvod_25r2_5","Zadání z přijímaček")
    body += zadani("Lepíme čtverečky se stranou 1 cm. Vytváříme obdélníky s obvodem 18 cm.\n5.1 Nejdelší možná strana?  5.2 Kolik různých obsahů?  5.3 Největší možný obsah?","#7F8C8D")
    body += '<div class="steps">'
    body += step(1,"Zjistím podmínku","Obvod obdélníku = 2 &times; (délka + šířka) = 18 cm<br>Takže: délka + šířka = 18 &divide; 2 = <span class='calc'>9 cm</span>","#7F8C8D","#f5f5f5")
    body += step(2,"Vyjmenuji všechny možnosti","<table class='ex-table' style='width:100%'><tr><th>a</th><th>b</th><th>Obsah</th></tr><tr><td>1</td><td>8</td><td>8 cm&sup2;</td></tr><tr><td>2</td><td>7</td><td>14 cm&sup2;</td></tr><tr><td>3</td><td>6</td><td>18 cm&sup2;</td></tr><tr><td>4</td><td>5</td><td><b>20 cm&sup2;</b></td></tr></table>","#515A5A","#f5f5f5")
    body += step(3,"Odpovím na otázky","5.1: Nejdelší strana = <span class='calc'>8 cm</span><br>5.2: Různé obsahy: 8, 14, 18, 20 &rarr; <span class='calc'>4 různé</span><br>5.3: Největší obsah = <span class='calc'>20 cm&sup2;</span> (obdélník 4&times;5)","#2C3E50","#f5f5f5")
    body += '</div>'
    body += result("✅","5.1: 8 cm &nbsp;|&nbsp; 5.2: 4 různé obsahy &nbsp;|&nbsp; 5.3: 20 cm&sup2;","#F2F3F4","#2C3E50")
    body += '</div></div>'

    # HINT 2
    body += '<div class="example" style="border-color:#7F8C8D">'
    body += ex_header(2,"Šestiúhelník &mdash; domeček","2025 &middot; 1. řádný termín","#f5f5f5","#515A5A","💡 S nápovědou","💡")
    body += '<div class="ex-body">'
    body += exam_img("obvod_25r1_6","Domeček ze zadání")
    body += zadani("Šestiúhelník tvaru domečku má obvod 24 cm.\nSkládá se ze STŘECHY (rovnoběžník ze 3 rovnostranných trojúhelníků) a PŘÍZEMÍ (obdélník).\nOba čtyřúhelníky mají STEJNÝ obvod.\n6.1 Obvod střechy?  6.2 Kratší strana obdélníku (přízemí)?","#7F8C8D")
    body += hint_card("🏠","Klíčové zjištění &mdash; krok za krokem:","""
<p><b>Krok 1:</b> Rovnostranný trojúhelník = všechny 3 strany stejně dlouhé. Říkejme straně &bdquo;jedna délka".</p>
<p><b>Krok 2:</b> Střecha má tvar rovnoběžníku &mdash; 4 strany, každá = &bdquo;jedna délka" &rarr; obvod střechy = 4 &times; délka.</p>
<p><b>Krok 3:</b> Přízemí (obdélník) &mdash; delší strana = &bdquo;jedna délka", kratší strana = kratší. Obvod = 2 &times; délka + 2 &times; kratší.</p>
<p><b>Krok 4:</b> Oba čtyřúhelníky mají STEJNÝ obvod:<br>
4 &times; délka = 2 &times; délka + 2 &times; kratší<br>
Odečteme 2 &times; délka z obou stran: 2 &times; délka = 2 &times; kratší.<br>
Vydělíme 2: <b>kratší = délka</b> (obě délky jsou stejné!)</p>
<p><b>Krok 5:</b> Celkový obvod domečku = 2 šikmé + horní + 2 kratší + spodek = 6 &times; délka = 24 cm.<br>
Takže délka = _____</p>""","#f5f5f5","#7F8C8D")
    body += answer_box("6.1: _____ cm &nbsp;&nbsp; 6.2: _____ cm")
    body += '</div></div>'

    # HINT 3
    body += '<div class="example" style="border-color:#7F8C8D">'
    body += ex_header(3,"Čtyřúhelník ze čtverců","2023 &middot; 1. náhradní termín","#f5f5f5","#515A5A","💡 S nápovědou","💡")
    body += '<div class="ex-body">'
    body += exam_img("obvod_23n1_5_6","Zadání z přijímaček")
    body += zadani("Čtyřúhelník ABCD se skládá ze 7 šedých čtverců a 4 bílých čtverců.\nObvod jednoho šedého čtverce = 48 cm.\n6.1 Obvod jednoho bílého čtverce (cm)?\n6.2 Obvod celého čtyřúhelníku ABCD (cm)?","#7F8C8D")
    body += hint_card("🔷","Postup:","""
<p>Šedý čtverec: obvod = 48 cm &rarr; strana šedého = 48 &divide; 4 = _____ cm</p>
<p>Z obrázku: bílý čtverec má stranu = polovina šedého = _____ cm</p>
<p>Obvod bílého čtverce = 4 &times; _____ = _____ cm</p>
<p>Pro obvod celého tvaru: jdi prstem OKOLO celého tvaru a počítej vnější úseky.</p>""","#f5f5f5","#515A5A")
    body += answer_box("6.1: _____ cm &nbsp;&nbsp; 6.2: _____ cm")
    body += '</div></div>'

    # SOLO 4,5,6
    solos = [
        ("4","Obrazec A a B","2025 &middot; 2. náhradní termín","obvod_25n2_6",
         "Obrazec A: obdélník ze 4 bílých obdélníčků a 4 šedých čtverečků.\nObvod bílé části je o 32 cm VĚTŠÍ než obvod šedé části.\nObrazec B vznikl přeskládáním dílů A.\n6.1 Obvod celého obrazce A?  6.2 O kolik cm se liší obvody A a B?"),
        ("5","Záhon &mdash; rovnostranný trojúhelník","2025 &middot; 2. řádný termín","obvod_25r2_10_11",
         "Záhon má tvar rovnostranného trojúhelníku. Po obvodu záhonu je 39 rostlin ve stejných rozestupech (i v každém vrcholu).\nŽluté rostliny tvoří 6 stejných žlutých rovnostranných trojúhelníků.\nFialové tvoří 3 fialové trojúhelníky &mdash; každý o 1 řadu více než žlutý.\n\n💡 Postup pro úlohu 10:\nObvod záhonu = 39 rostlin. Záhon je rovnostranný &rarr; každá strana má 39&divide;3 + 1 = _____ rostlin.\n(Proč +1? Rohový keř se počítá do dvou stran &mdash; proto ho musíme přičíst zpět.)\nNa každé straně záhonu jsou 2 žluté trojúhelníky vedle sebe &rarr; strana 1 žlutého △ = _____ rostlin.\nKolik rostlin má rovnostranný trojúhelník se stranou n? (n=1: 1, n=2: 3, n=3: 6, n=4: 10 ...)\n\n10. Kolik žlutých rostlin tvoří jeden žlutý trojúhelník? (výběr A&ndash;E)\n11. Kolik fialových rostlin je vysazeno na celém záhoně?"),
        ("6","Čtverec z čtverečků","2024 &middot; 2. náhradní termín","obvod_24n2_8",
         "Ve čtvercové síti je nakreslen obdélník ABCD, který lze rozstříhat na 20 shodných čtverců. Obvod obdélníku = 54 cm.\n\n💡 Postup:\nDélka + šířka = 54 &divide; 2 = 27 cm.\nObdélník = m sloupců &times; n řad čtverců, kde m&times;n = 20.\nDélka = m &times; strana čtverce, šířka = n &times; strana čtverce &rarr; (m+n) &times; strana = 27.\nStrana čtverce musí dělit 27 beze zbytku. Zkus faktory 20:\n  &bull; 1&times;20: m+n=21, strana=27&divide;21 (nevychází celé ✗)\n  &bull; 2&times;10: m+n=12, strana=27&divide;12 (nevychází celé ✗)\n  &bull; 4&times;5:  m+n=9,  strana=27&divide;9=3 cm &#10003;\nDélka=5&times;3=15 cm, šířka=4&times;3=12 cm. Teď odpověz:\n\n8.1 Je obsah obdélníku ABCD 180 cm&sup2;?  A / N\n8.2 Je obvod tmavého obrazce 69 cm?  A / N\n8.3 Je obsah tmavého obrazce 90 cm&sup2;?  A / N"),
    ]
    for num, title, src, img_name, zad in solos:
        body += f'<div class="example" style="border-color:#ddd">'
        body += ex_header(num, title, src, "#e8f5e9","#1E8449","🖊 Vyřeš sám/sama","🖊")
        body += '<div class="ex-body">'
        if img_name:
            body += exam_img(img_name)
        body += zadani(zad)
        body += scratch(6)
        body += answer_box()
        body += '</div></div>'

    body += ex_header(7,"Obdélník z čtverců čtyř velikostí — S, M, L, XL","2022 &middot; 2. řádný termín","#f5f0ff","#7F8C8D","🖊 Vyřeš sám/sama","🖊")
    body += '<div class="ex-body">'
    body += zadani("""Obdélník je rozdělen na 12 čtverců čtyř různých velikostí (S, M, L a XL). Delší strana obdélníku měří 260 cm.
<ol class="task-list">
<li>Jaký je obvod čtverce velikosti L? Nápověda: zkus zjistit stranu nejmenšího čtverce S a od ní odvodit ostatní.</li>
</ol>""")
    body += scratch(6)
    body += answer_box()
    body += '</div></div>'

    body += tip("👆","Při počítání obvodu složeného tvaru VŽDY jdi prstem po okraji &mdash; jen vnější strany se počítají! Vnitřní stěny se nepočítají.","#f5f5f5","#7F8C8D")

    return body

# ══════════════════════════════════════════════════════════════════════
# PL03 &mdash; POSLOUPNOSTI A VZORY
# ══════════════════════════════════════════════════════════════════════

    body += tip("💡","Spočítej vždy první rozdíly! Jsou-li stejné → stálý přírůstek. Různé? Spočítej 2. rozdíly.","#fff8f0","#C87941")

    
def pl03():
    CD="#A04000"; CM="#C87941"; CL="#FDEBD0"
    body = cover(3,"Posloupnosti a vzory","Rady čísel, obrazce, pravidla a N-tý člen","4&ndash;6",CD,CM, "PL03_Posloupnosti_a_vzory.pdf")

    body += hints_start(CD)
    body += build_hints(HINTS_PL03)
    body += hints_end()

    body += build_quiz(QUIZ_PL03, "#C87941")
    body += build_quiz_answers(QUIZ_PL03, "#C87941")

    body += divider("PŘÍKLADY K PROCVIČENÍ")

    # SOLVED
    body += '<div class="example" style="border-color:#C87941">'
    body += ex_header(1,"Cyklista &mdash; klesající vzdálenosti","2023 &middot; 2. náhradní termín","#FDEBD0","#A04000","✅ Vzorový příklad","✅")
    body += '<div class="ex-body">'
    body += zadani("Cyklista za 5 dní ujel celkem 200 km.\nPrvní den ujel nejdelší trasu a každý další den ujel o 6 km méně.\nKolik km ujel první den?","#C87941")
    body += '<div class="steps">'
    body += step(1,"Pojmenuji dny","1. den jede nejdéle. Každý další den ujede o 6 km méně.<br>Označím vzdálenost 1. dne jako <b>&#9633;</b> km.","#C87941","#fff8f0")
    body += step(2,"Zapíšu všechny dny","<div style='overflow-x:auto'><table class='ex-table'><tr><th>Den</th><th>1.</th><th>2.</th><th>3.</th><th>4.</th><th>5.</th></tr><tr><td>km</td><td>&#9633;</td><td>&#9633;&minus;6</td><td>&#9633;&minus;12</td><td>&#9633;&minus;18</td><td>&#9633;&minus;24</td></tr></table></div>","#A04000","#fff8f0")
    body += step(3,"Sečtu a hledám &#9633;","Kdybychom každý den ujeli &#9633; km (stejně jako první den), bylo by to 5 &times; &#9633; km.<br>Ale 2.&ndash;5. den ujeli méně: o 6, 12, 18, 24 km méně = celkem 60 km méně.<br>Takže: 5 &times; &#9633; &minus; 60 = 200 &rarr; 5 &times; &#9633; = <span class='calc'>260</span> &rarr; &#9633; = 260 &divide; 5 = <span class='calc'>52 km</span>","#7E5109","#fff8f0")
    body += step(4,"Ověřím","52 + 46 + 40 + 34 + 28 = <span class='calc'>200 &#10003;</span>","#7E5109","#fff8f0")
    body += '</div>'
    body += result("✅","První den ujel 52 km","#FDEBD0","#7E5109")
    body += '</div></div>'

    # HINT 2
    body += '<div class="example" style="border-color:#C87941">'
    body += ex_header(2,"Šestiúhelníky z trojúhelníků","2025 &middot; 1. náhradní termín","#fff8f0","#A04000","💡 S nápovědou","💡")
    body += '<div class="ex-body">'
    body += exam_img("posl_25n1_14","Zadání z přijímaček")
    body += zadani("1. obrazec: 3 bílé + 3 šedé trojúhelníky = 6 celkem.\nKaždý další přidá 1 pás trojúhelníků dokola.\n14.1 Kolik trojúhelníků celkem obsahuje přidaný pás 4. obrazce?\n14.2 Kolik šedých trojúhelníků je v celém 6. obrazci?\n14.3 Kolikátý obrazec má v posledním pásu 225 šedých trojúhelníků?","#C87941")
    body += hint_card("📊","Vyplň tabulku:","""
<div style="overflow-x:auto">
<table class="ex-table" style="width:100%">
<tr><th style="background:#A04000;color:white">Obrazec</th><th style="background:#A04000;color:white">1.</th><th style="background:#A04000;color:white">2.</th><th style="background:#A04000;color:white">3.</th><th style="background:#A04000;color:white">4.</th><th style="background:#A04000;color:white">5.</th><th style="background:#A04000;color:white">6.</th></tr>
<tr><td>Celkem △</td><td>6</td><td>24</td><td>54</td><td class="fill"></td><td class="fill"></td><td class="fill"></td></tr>
<tr><td>Přidaný pás</td><td>&mdash;</td><td>18</td><td>30</td><td class="fill"></td><td class="fill"></td><td class="fill"></td></tr>
<tr><td>Z toho šedých</td><td>3</td><td>9</td><td>15</td><td class="fill"></td><td class="fill"></td><td class="fill"></td></tr>
</table>
</div>
<p style="margin-top:8px;font-size:13px">Nápověda: počet šedých v pásu roste o 6. Celkový počet šedých = sečti šedé ve všech pasech.</p>""","#fff8f0","#C87941")
    body += answer_box("14.1: _____ △ &nbsp;&nbsp; 14.2: _____ šedých &nbsp;&nbsp; 14.3: _____ obrazec")
    body += '</div></div>'

    # HINT 3
    body += '<div class="example" style="border-color:#C87941">'
    body += ex_header(3,"Základní a rozšířený obrazec","2023 &middot; 1. řádný termín","#fff8f0","#A04000","💡 S nápovědou","💡")
    body += '<div class="ex-body">'
    body += exam_img("posl_23r1_14","Zadání z přijímaček")
    body += zadani("Základní obrazec: výška řad &times; šířka sloupců světlých čtverečků.\nRozšířený: přidáme 1 tmavou řadu nahoře + 1 tmavý sloupec vlevo + 1 vpravo.\nPočet tmavých = (šířka + 2) + 2 &times; výška\n💡 Příklad: základní 2&times;3 &rarr; tmavých = (3+2)+2&times;2 = 5+4 = 9  &#10003;\n14.1 Základní má 5 řad, přidáme 30 tmavých &mdash; kolik sloupců má základní?\n14.2 Rozšířený má 3 řady a stejný počet tmavých jako světlých &mdash; kolik sloupců má rozšířený?\n14.3 Kolik různých rozšířených obrazců má právě 50 tmavých čtverečků?","#C87941")
    body += hint_card("➡️","Nápověda pro 14.1 &mdash; krok za krokem:","""
<p>Výška základního = 5 řad. Dosadím do vzorce:</p>
<p>Tmavých = (šířka + 2) + 2 &times; 5 = šířka + 2 + 10 = šířka + 12</p>
<p>Víme že tmavých = 30: šířka + 12 = 30, takže šířka = _____</p>""","#fff8f0","#A04000")
    body += hint_card("➡️","Nápověda pro 14.2 &mdash; krok za krokem:","""
<p>Rozšířený má 3 řady &rarr; 1 tmavá nahoře + 2 světlé řady (výška základního = 2).</p>
<p>Světlých čtverečků = 2 &times; šířka.</p>
<p>Tmavých čtverečků = (šířka+2) + 2&times;2 = šířka + 6.</p>
<p>Podmínka tmavých = světlých: šířka + 6 = 2 &times; šířka, takže šířka = _____</p>
<p>Rozšířený má 3 řady a šířka+2 = _____ sloupce.</p>""","#fff8f0","#C87941")
    body += answer_box("14.1: šířka základního = _____ (nápověda: 18) &nbsp;&nbsp; 14.2: _____ sloupců rozšířeného (nápověda: 8) &nbsp;&nbsp; 14.3: _____ obrazců")
    body += '</div></div>'

    # SOLO 4,5,6
    solos = [
        ("4","Poutník a kouzelník s dukáty","2025 &middot; 1. řádný termín","posl_25r1_14",
         "Poutník a kouzelník měli oba 54 dukátů. Kouzlo: Poutník dá &#9633; dukátů kouzelníkovi, aby poutník měl polovinu toho, co bude mít kouzelník. Poutníkův zbytek se zdvojnásobí &rarr; oba mají opět stejně.\n14.1 Kolik dukátů dal poutník kouzelníkovi?\n14.2 Kolik dukátů měl poutník po druhém použití kouzla?\n14.3 Kolik dukátů měl poutník, když přestal?"),
        ("5","Obrazce ze čtverečků &mdash; připojování","2025 &middot; 2. řádný termín","posl_25r2_14",
         "1. obrazec: čtverec, obvod = 80 cm. 2. obrazec: čtverec (přidáno 20 čtverečků). 3. obrazec: obdélník (přidáno 11 čtverečků).\n14.1 Obvod 2. obrazce (v cm)?\n14.2 O kolik cm se liší délky sousedních stran 3. obrazce?\n14.3 Délka vyznačené lomené čáry na 3. obrazci (v cm)?"),
        ("6","Trojúhelníkové obrazce z pater","2023 &middot; 2. náhradní termín","posl_23n2_14",
         "Obrazce tvaru trojúhelníku se sestavují skládáním šedých trojúhelníků do pater.\n1. obrazec = 1 trojúhelník, každý další přidá 1 patro.\n14.1 Kolik úseček je v obrazci s 5 patry?\n14.2 Počet úseček v posledním a předposledním obrazci se liší o 96. O kolik se liší počet puntíků?\n14.3 V jednom obrazci je 300 puntíků. Kolik úseček je v NÁSLEDUJÍCÍM obrazci?"),
    ]
    for num, title, src, img_name, zad in solos:
        body += f'<div class="example" style="border-color:#ddd">'
        body += ex_header(num, title, src, "#e8f5e9","#1E8449","🖊 Vyřeš sám/sama","🖊")
        body += '<div class="ex-body">'
        if img_name:
            body += exam_img(img_name)
        body += zadani(zad)
        body += scratch(7)
        body += answer_box()
        body += '</div></div>'

    body += tip("📋","Tabulka je tvůj nejlepší kamarád! Vypiš si hodnoty pro 1., 2., 3., 4. člen a pak hledej pravidlo. Bez tabulky se snadno spletěš.","#fff8f0","#C87941")

    body += ex_header(4,"Sirky &mdash; stálý přírůstek obrazců","2020 &middot; 1. řádný termín","#fff8f0","#C87941","🖊 Vyřeš sám/sama","🖊")
    body += '<div class="ex-body">'
    body += zadani("""1. obrazec je sestaven z 9 sirek, 2. ze 13 sirek. Každý další se zvětšuje podle téhož pravidla.
<ol class="task-list">
<li>O kolik sirek má 5. obrazec více než 3. obrazec?</li>
<li>Z kolika sirek je sestaven 20. obrazec?</li>
<li>Kolikátý obrazec je sestaven ze 129 sirek?</li>
</ol>""")
    body += scratch(5)
    body += answer_box()
    body += '</div></div>'

    body += ex_header(5,"Puntíky ve čtvercích &mdash; vzorec n-tého obrazce","2021 &middot; 1. řádný termín","#fff8f0","#C87941","🖊 Vyřeš sám/sama","🖊")
    body += '<div class="ex-body">'
    body += zadani("""Obrazce jsou tvořeny puntíky ve čtvercích. 1. obrazec = 1 puntík. Strana 2. obrazce = 3 puntíky, každý další má o 2 puntíky více na straně.
<ol class="task-list">
<li>Kolik puntíků obsahuje strana hraničního čtverce 10. obrazce?</li>
<li>O kolik se liší počty puntíků v 9. a 11. obrazci?</li>
<li>U kolikátého obrazce se počty puntíků sousedních obrazců liší o 120?</li>
</ol>""")
    body += scratch(5)
    body += answer_box()
    body += '</div></div>'

    body += ex_header(6,"Sirky &mdash; stálý přírůstek obrazců","2020 &middot; 1. řádný termín","#fff8f0","#C87941","🖊 Vyřeš sám/sama","🖊")
    body += '<div class="ex-body">'
    body += zadani("""1. obrazec je sestaven z 9 sirek, 2. ze 13 sirek. Každý další se zvětšuje podle téhož pravidla.
<ol class="task-list">
<li>O kolik sirek má 5. obrazec více než 3. obrazec?</li>
<li>Z kolika sirek je sestaven 20. obrazec?</li>
<li>Kolikátý obrazec je sestaven ze 129 sirek?</li>
</ol>""")
    body += scratch(5)
    body += answer_box()
    body += '</div></div>'

    body += ex_header(7,"Puntíky ve čtvercích &mdash; vzorec n-tého obrazce","2021 &middot; 1. řádný termín","#fff8f0","#C87941","🖊 Vyřeš sám/sama","🖊")
    body += '<div class="ex-body">'
    body += zadani("""Obrazce jsou tvořeny puntíky ve čtvercích. 1. obrazec = 1 puntík. Strana 2. obrazce = 3 puntíky, každý další má o 2 puntíky více na straně.
<ol class="task-list">
<li>Kolik puntíků obsahuje strana hraničního čtverce 10. obrazce?</li>
<li>O kolik se liší počty puntíků v 9. a 11. obrazci?</li>
<li>U kolikátého obrazce se počty puntíků sousedních obrazců liší o 120?</li>
</ol>""")
    body += scratch(5)
    body += answer_box()
    body += '</div></div>'

    body += tip("💡","Spočítej vždy první rozdíly! Jsou-li stejné → stálý přírůstek. Různé? Spočítej 2. rozdíly.","#fff8f0","#C87941")

    return body

# ══════════════════════════════════════════════════════════════════════
# PL01 &mdash; GEOMETRICKÁ KONSTRUKCE
# ══════════════════════════════════════════════════════════════════════
def pl01():
    CD="#1A5276"; CM="#2980B9"; CL="#D6EAF8"
    body = cover(1,"Geometrická konstrukce","Rýsování trojúhelníků, čtverců a obdélníků &mdash; vždy najdi všechna řešení!","6",CD,CM, "PL01_Geometricka_konstrukce.pdf")

    body += hints_start(CD)
    body += build_hints(HINTS_PL01)
    body += hints_end()

    body += build_quiz(QUIZ_PL01, "#2980B9")
    body += build_quiz_answers(QUIZ_PL01, "#2980B9")

    body += divider("PŘÍKLADY K PROCVIČENÍ")

    # SOLVED
    body += '<div class="example" style="border-color:#2980B9">'
    body += ex_header(1,"Rovnostranný trojúhelník KMS","2025 &middot; 2. náhradní termín","#D6EAF8","#1A5276","✅ Vzorový příklad","✅")
    body += '<div class="ex-body">'
    body += exam_img("geom_25n2_7_1","Zadání z přijímaček")
    body += zadani("Body K, M jsou vrcholy trojúhelníku KLM. Střed strany LM = bod S.\nTrojúhelník KMS je rovnostranný.\nSestrojte bod S a vrchol L. Najděte VŠECHNA řešení.","#2980B9")
    body += '<div class="steps">'
    body += step(1,"Použiji klíčovou informaci","KMS je rovnostranný &rarr; KS = MS = KM (všechny tři strany jsou stejně dlouhé).<br>S hledám jako třetí vrchol rovnostranného trojúhelníku KMS &mdash; k tomu použiji kružítko.","#2980B9","#e8f4ff")
    body += step(2,"Sestrojím bod S kružítkem","Nastav kružítko na délku KM.<br>Nakresli kružnici z K a kružnici z M.<br>Jejich průsečíky jsou 2 možné polohy bodu S.<br>&rarr; <b>Jsou 2 řešení!</b>","#1A5276","#e8f4ff")
    body += step(3,"Najdu bod L","S je STŘED strany LM &mdash; leží přesně uprostřed mezi L a M.<br>L hledám takto: změřím vzdálenost SM kružítkem &rarr; přenesu stejnou vzdálenost na druhou stranu od S &rarr; tam je L.","#154360","#e8f4ff")
    body += step(4,"Ověřím obě řešení","Každé řešení zkontroluj: Je KMS skutečně rovnostranný? Je S skutečně středem LM?","#154360","#e8f4ff")
    body += '</div>'
    body += result("✅","2 řešení &mdash; S nad nebo pod úsečkou KM","#D6EAF8","#154360")
    body += '</div></div>'

    # HINT 2
    body += '<div class="example" style="border-color:#2980B9">'
    body += ex_header(2,"Obdélník ABCD na přímkách","2025 &middot; 1. řádný termín","#e8f4ff","#1A5276","💡 S nápovědou","💡")
    body += '<div class="ex-body">'
    body += exam_img("geom_25r1_7_1","Zadání z přijímaček")
    body += zadani("Přímky p, q se protínají v bodě A (vrchol obdélníku ABCD).\nNa jedné přímce leží B, na druhé leží C.\nStrana BC prochází bodem R.\nSestrojte B, C, D. Najděte všechna řešení.","#2980B9")
    body += hint_card("➡️","Postup:","""
<div class="hint-step"><span class="hint-arrow">1.</span><span class="hint-text">Bod A je vrchol. B leží na přímce p (nebo q) &mdash; zkus obě možnosti!</span></div>
<div class="hint-step"><span class="hint-arrow">2.</span><span class="hint-text">BC musí procházet bodem R &rarr; nakresli přímku přes R kolmo na přímku AB</span></div>
<div class="hint-step"><span class="hint-arrow">3.</span><span class="hint-text">Kde tato kolmice protne druhou přímku &rarr; tam je bod C</span></div>
<div class="hint-step"><span class="hint-arrow">4.</span><span class="hint-text">Bod D: z vrcholu A vztyč kolmici na stranu AB. Na této kolmici odměř stejnou vzdálenost jako AB &mdash; tam je vrchol D.</span></div>
<div class="hint-step"><span class="hint-arrow">5.</span><span class="hint-text">Zkus B na p &rarr; 1. řešení. Zkus B na q &rarr; 2. řešení!</span></div>""","#e8f4ff","#2980B9")
    body += '<div style="height:200px;background:#f8f9fa;border:1px dashed #ccc;border-radius:8px;display:flex;align-items:center;justify-content:center;margin:10px 0;color:#999;font-style:italic">Prostor pro rýsování</div>'
    body += '</div></div>'

    # HINT 3
    body += '<div class="example" style="border-color:#2980B9">'
    body += ex_header(3,"Čtverec ABCD &mdash; bod R na přímce","2023 &middot; 2. náhradní termín","#e8f4ff","#1A5276","💡 S nápovědou","💡")
    body += '<div class="ex-body">'
    body += exam_img("geom_23n2_7_1","Zadání z přijímaček")
    body += zadani("Bod A je vrchol čtverce ABCD. Na přímce p leží vrchol B.\nBod R má od vrcholů A i B STEJNOU vzdálenost. Bod R neleží uvnitř čtverce.\nSestrojte B, C, D. Najděte všechna řešení.","#2980B9")
    body += hint_card("💡","Klíčová nápověda:","""
<p><b>Bod stejně vzdálený od A i B</b> leží na OSE ÚSEČKY AB!</p>
<p>Osa AB = kolmice procházející středem AB.</p>
<div class="hint-step"><span class="hint-arrow">1.</span><span class="hint-text">R leží na přímce p A ZÁROVEŇ na ose úsečky AB &rarr; z toho plyne poloha B!</span></div>
<div class="hint-step"><span class="hint-arrow">2.</span><span class="hint-text">Kružítkem sestrojíš osu AB: z A i B nakresli kružnice &mdash; poloměr nastav na trochu víc než polovinu délky AB. Průsečíky těchto kružnic dají bod na ose.</span></div>
<div class="hint-step"><span class="hint-arrow">3.</span><span class="hint-text">Podmínka: R neleží uvnitř čtverce &rarr; vyber správné řešení!</span></div>""","#e8f4ff","#1A5276")
    body += '<div style="height:200px;background:#f8f9fa;border:1px dashed #ccc;border-radius:8px;display:flex;align-items:center;justify-content:center;margin:10px 0;color:#999;font-style:italic">Prostor pro rýsování</div>'
    body += '</div></div>'

    for num, img_name, title, src, zad in [
        ("4","geom_25r2_7_1","Pravoúhlý trojúhelník ABC","2025 &middot; 2. řádný termín",
         "V rovině leží bod U a různoběžné přímky p, q.\nNa přímkách p, q leží dvě strany pravoúhlého trojúhelníku ABC.\nTřetí strana BC prochází bodem U.\n\n💡 Nápověda: V pravoúhlém trojúhelníku je pravý úhel (90&deg;) u vrcholu A &mdash; ten leží v místě, kde se přímky p a q kříží. Strana AB je na jedné přímce, AC na druhé. Strana BC prochází bodem U.\n\nSestrojte A, B, C. Najděte všechna řešení."),
        ("5","geom_25r1_7_2","Trojúhelník EFG &mdash; bod S stejně vzdálený","2025 &middot; 1. řádný termín",
         "V rovině leží bod S a různoběžné přímky m, n.\nNa m leží strana EF, na n leží strana EG trojúhelníku EFG.\nBod S je stejně daleko od KAŽDÉHO ze tří vrcholů E, F, G.\n💡 Nápověda: sestrojíš osy dvou stran (každá osa = kolmice středem strany). Kde se osy kříží, tam je S.\nSestrojte trojúhelník EFG. Najděte všechna řešení."),
        ("6","geom_25r2_7_2","Obdélník KLMN s podmínkami","2025 &middot; 2. řádný termín",
         "Bod K je vrchol obdélníku KLMN. Strana KL je rovnoběžná s přímkou r.\nNa přímce s leží střed S strany KN a vrchol M obdélníku KLMN.\nSestrojte S a vrcholy L, M, N. Najděte všechna řešení.\n\n💡 Postup: KL rovnoběžná s r &rarr; nakresli rovnoběžku s r bodem K. M leží na přímce s &rarr; M je průsečík rovnoběžky s přímkou s. Pak S je střed KM."),
    ]:
        body += f'<div class="example" style="border-color:#ddd">'
        body += ex_header(num, title, src, "#e8f5e9","#1E8449","🖊 Vyřeš sám/sama","🖊")
        body += '<div class="ex-body">'
        body += exam_img(img_name)
        body += zadani(zad)
        body += '<div style="height:240px;background:#f8f9fa;border:1px dashed #ccc;border-radius:8px;display:flex;align-items:center;justify-content:center;margin:10px 0;color:#999;font-style:italic">Prostor pro rýsování (použij pravítko a kružítko)</div>'
        body += '</div></div>'

    body += tip("✅","Vždy zkontroluj každé řešení: splňuje VŠECHNY podmínky ze zadání? Prochází strana bodem R? Leží bod na přímce?","#e8f4ff","#2980B9")

    return body

# ══════════════════════════════════════════════════════════════════════
# PL02 &mdash; PROSTOROVÁ PŘEDSTAVIVOST
# ══════════════════════════════════════════════════════════════════════
def pl02():
    CD="#0E6655"; CM="#17A589"; CL="#D1F2EB"
    body = cover(2,"Prostorová představivost","Pohledy na tělesa, počítání kostek, přiřazení A&ndash;F","5&ndash;6",CD,CM, "PL02_Prostorova_predstavivost.pdf")

    body += hints_start(CD)
    body += build_hints(HINTS_PL02)
    body += hints_end()

    body += build_quiz(QUIZ_PL02, "#17A589")
    body += build_quiz_answers(QUIZ_PL02, "#17A589")

    body += divider("PŘÍKLADY K PROCVIČENÍ")

    # SOLVED
    body += '<div class="example" style="border-color:#17A589">'
    body += ex_header(1,"Kostky s tečkami &mdash; maximum a minimum","2025 &middot; 1. řádný termín","#D1F2EB","#0E6655","✅ Vzorový příklad","✅")
    body += '<div class="ex-body">'
    body += exam_img("prostor_25r1_13","Zadání z přijímaček &mdash; 3 tělesa")
    body += zadani("Každé těleso je slepeno ze 3 kostek (každá 12 teček).\n1. těleso: co NEJVÍCE teček na povrchu\n2. a 3. těleso: co NEJMÉNĚ teček\nPřiřaď počty teček (A: <20, B:20, C:22, D:24, E:26, F: více než 26)","#17A589")
    body += '<div class="steps">'
    body += step(1,"Spočítám celkové tečky","3 kostky &times; 12 teček = <span class='calc'>36 teček celkem</span>","#17A589","#e8faf5")
    body += step(2,"Každé těleso &mdash; 3 kostky v řadě L","Každé těleso: kostka A + kostka B (v rohu) + kostka C = L-tvar.<br>2 spoje: A&ndash;B a B&ndash;C. Skryjí se <span class='calc'>4 stěny</span> (z každého spoje 2).","#0E6655","#e8faf5")
    body += step(3,"Maximum &mdash; schovám stěny po 1 tečce","U L-tvaru: kout B schová 2 sousední stěny (1+1=2). Konce A, C skryjí po 1 tečce.<br>Ztratím: 2+1+1 = 4 tečky. Na povrchu: 36 &minus; 4 = <span class='calc'>32 teček</span> &rarr; F (32 > 26)","#145A32","#e8faf5")
    body += step(4,"Minimum &mdash; schovám stěny po 3 tečkách","Kout B schová 2 sousední stěny (3+3=6). Konce A, C skryjí po 3 tečkách.<br>Ztratím: 6+3+3 = 12 teček. Na povrchu: 36 &minus; 12 = <span class='calc'>24 teček</span> &rarr; D","#145A32","#e8faf5")
    body += '</div>'
    body += result("✅","1. těleso: F (32 teček, tedy více než 26) &nbsp;|&nbsp; 2. těleso: D (24) &nbsp;|&nbsp; 3. těleso: D (24)","#D1F2EB","#145A32")
    body += '</div></div>'

    # HINT 2
    body += '<div class="example" style="border-color:#17A589">'
    body += ex_header(2,"Pyramida a stavby z kostek","2025 &middot; 2. náhradní termín","#e8faf5","#0E6655","💡 S nápovědou","💡")
    body += '<div class="ex-body">'
    body += exam_img("prostor_25n2_13","Zadání z přijímaček")
    body += zadani("Ze stejně velkých kostek: pyramida (5 pater: 5&times;5, 4&times;4, 3&times;3, 2&times;2, 1&times;1 &mdash; celkem 55 kostek).\nJitka ji zbourala &rarr; nová stavba. Emil zbourával &rarr; pravidelná stavba.\n13.1 Kolik kostek v pyramidě nebylo viditelných z žádné strany?\n13.2 Kolik kostek Jitčiny stavby se dotýkalo podložky?\n13.3 Kolik kostek dohromady mají spodní 2 patra Emilovy stavby?\nPřiřaď (A:<15, B:15, C:18, D:21, E:26, F: více než 26)","#17A589")
    body += hint_card("📦","Nápověda pro 13.1 &mdash; skryté kostky v pyramidě:","""
<p style="font-size:12px;margin-bottom:6px">Kostka je skrytá, pokud má ze všech 6 stran sousední kostky (nedotýká se podložky ani vzduchu).</p>
<table class="ex-table" style="width:100%">
<tr><th style="background:#0E6655;color:white">Patro</th><th style="background:#0E6655;color:white">Rozměr</th><th style="background:#0E6655;color:white">Vnitřní (skryté)</th></tr>
<tr><td>Spodní (1.)</td><td>5&times;5 = 25 kostek</td><td>žádná &mdash; dotýkají se podložky!</td></tr>
<tr><td>2. patro</td><td>4&times;4 = 16 kostek</td><td>vnitřní 2&times;2 = <span class="fill" style="display:inline-block;width:30px;border-bottom:1px solid #ccc"></span> kostky</td></tr>
<tr><td>3. patro</td><td>3&times;3 = 9 kostek</td><td>vnitřní 1&times;1 = <span class="fill" style="display:inline-block;width:30px;border-bottom:1px solid #ccc"></span> kostka</td></tr>
<tr><td>4. patro</td><td>2&times;2 = 4 kostky</td><td>žádná skrytá</td></tr>
<tr><td>5. patro</td><td>1&times;1 = 1 kostka</td><td>žádná skrytá</td></tr>
</table>
<p>Celkem skrytých = _____ + _____ = _____</p>""","#e8faf5","#17A589")
    body += hint_card("🏗️","Nápověda pro 13.2 &mdash; Jitčina stavba:","""
<p>Jitka zbourala pyramidu a přestavěla ji. Z obrázku vidíš, jak vypadá pohled shora.</p>
<p>Dotýkající se podložky = počet kostek v dolní vrstvě = kolik políček vidíš v pohledu shora.</p>""","#e8faf5","#17A589")
    body += hint_card("🔢","Nápověda pro 13.3 &mdash; Emilova stavba:","""
<p>Emil postavil pravidelnou stavbu (vidíš čtyři horní patra). Spočítej kostky v 1. a 2. patře zdola.</p>
<p>Pozor: patra se počítají odzdola &mdash; spodní = 1. patro.</p>""","#e8faf5","#17A589")
    body += answer_box("13.1: _____   13.2: _____   13.3: _____")
    body += '</div></div>'

    # HINT 3
    body += '<div class="example" style="border-color:#17A589">'
    body += ex_header(3,"Pohled na stavbu z válců &mdash; zprava","2023 &middot; 2. řádný termín","#e8faf5","#0E6655","💡 S nápovědou","💡")
    body += '<div class="ex-body">'
    body += exam_img("prostor_23r2_11_12","Zadání z přijímaček")
    body += zadani("Stavba ze stejně velkých válců tří barev.\nZobrazeny: pohled shora a pohled zepředu.\nKterý obrázek A&ndash;E ukazuje pohled ZPRAVA?","#17A589")
    body += hint_card("👁️","Jak vybrat správný pohled zprava:","""
<div class="hint-step"><span class="hint-arrow">1.</span><span class="hint-text">Z pohledu shora zjisti: kolik řad je zepředu dozadu? To je šířka pohledu zprava.</span></div>
<div class="hint-step"><span class="hint-arrow">2.</span><span class="hint-text">Pohled zprava: přejdi doprava od stavby, díváš se doleva &mdash; vidíš sloupce na pravém okraji stavby</span></div>
<div class="hint-step"><span class="hint-arrow">3.</span><span class="hint-text">Barvy: z pravé strany vidíš barvy pravého kraje stavby</span></div>
<div class="hint-step"><span class="hint-arrow">4.</span><span class="hint-text">Zkontroluj každou možnost A&ndash;E: sedí šířka? Sedí výška? Sedí barvy?</span></div>""","#e8faf5","#0E6655")
    body += answer_box("Pohled zprava: _____ (A/B/C/D/E)   Proč: ________________________________")
    body += '</div></div>'

    for num, img_name, title, src, zad in [
        ("4","prostor_23n1_13","Filipův model krychle","2023 &middot; 1. náhradní termín",
         "Denisa (2&times;2&times;2): 8 kuliček, 12 tyček. Emil (3&times;3&times;3): 27 kuliček, 54 tyček.\nFilip (4&times;4&times;4): 144 tyček celkem.\n\nKolik kuliček má Filipův model?\nKolik tyček leží na hranách Filipovy krychle?\n\n💡 Vzorečky pro n&times;n&times;n:\n&bull; Kuliček = n &times; n &times; n (pro 4&times;4&times;4: 4&times;4&times;4 = 64)\n&bull; Tyček na hranách = 12 &times; (n&minus;1) (krychle má 12 hran, na každé je n&minus;1 tyček)"),
        ("5","prostor_25n2_13","Stavby z krychlí &mdash; pohled shora","2025 &middot; 2. náhradní termín",
         "Podívej se na obrázek &mdash; Jitčina stavba je těleso č. 2 (uprostřed).\nZ pohledu shora nakresli mřížku a zapiš výšky sloupců.\nOtázky:\na) Kolik kostek se dotýkalo podložky (= dolní vrstva)?\nb) Kolik kostek bylo viditelných alespoň z jedné strany?\n   (Nápověda: viditelné = všechny mínus skryté)"),
        ("6","prostor_23n1_13","Krychle z kuliček a tyček","2023 &middot; 1. náhradní termín",
         "Pro krychli 5&times;5&times;5 spočítej:\na) Kolik kuliček? (vzorec: n&times;n&times;n)\nb) Kolik tyček na hranách? (vzorec: 12&times;(n&minus;1))\nc) Bonus: kolik tyček celkem? (z tabulky: 2&times;2&times;2=12, 3&times;3&times;3=54, 4&times;4&times;4=144 &mdash; najdi vzorec!)"),
    ]:
        body += f'<div class="example" style="border-color:#ddd">'
        body += ex_header(num, title, src, "#e8f5e9","#1E8449","🖊 Vyřeš sám/sama","🖊")
        body += '<div class="ex-body">'
        body += exam_img(img_name)
        body += zadani(zad)
        body += scratch(6)
        body += answer_box()
        body += '</div></div>'

    # ── Nové příklady 2020-2022 ──
    body += ex_header(4,"Stěny krychliček &mdash; součet čísel z pohledu","2021 &middot; 1. řádný termín","#e8f5e9","#1E8449","🖊 Vyřeš sám/sama","🖊")
    body += '<div class="ex-body">'
    body += zadani("""Na podložce je stavba z 16 krychliček (čtverec 4×4 v jedné vrstvě). Každá viditelná stěna dostane číslo: zepředu=1, zezadu=2, zprava=3, zleva=4, shora=5.
<ol class="task-list">
<li>Jaký je součet všech čísel 5 (pohled shora)?</li>
<li>Jaký je součet všech čísel 3 (pohled zprava)?</li>
<li>O kolik se liší součet čísel 4 (pohled zleva) od součtu čísel 1 (pohled zepředu)?</li>
</ol>""")
    body += scratch(5)
    body += answer_box()
    body += '</div></div>'

    body += ex_header(5,"Diagram s kroužky &mdash; doplň čísla do šipek","2023 &middot; 1. náhradní termín","#e8f5e9","#1E8449","🖊 Vyřeš sám/sama","🖊")
    body += '<div class="ex-body">'
    body += zadani("""V každém diagramu se stejná písmena nahradí stejným kladným číslem. Doplň čísla do kroužků tak, aby výpočty ve směru šipek souhlasily.
<div style="margin:10px 0;padding:10px;background:#f8f9ff;border-radius:8px;font-size:14px"><b>Vzor:</b> K → ÷K → −6 → +K → výsledek 2 &nbsp;→&nbsp; K=8: 8÷8=1, 1−6=−5, −5+8=3 ✗ &nbsp; K=7: 7÷7=1, 1−6=−5, −5+7=2 ✓</div>
<ol class="task-list">
<li>K → ÷3 → −K → +3 → výsledek 2. Jaké číslo je K?</li>
<li>L → ÷L → −3 → +L → výsledek 14. Jaké číslo je L?</li>
<li>M → ÷M → −24 → +M → výsledek 36. Jaké číslo je M?</li>
</ol>""")
    body += scratch(5)
    body += answer_box()
    body += '</div></div>'

    body += ex_header(6,"Popis stavby tabulkou — výška sloupců","2021 &middot; 2. řádný termín","#e8f5e9","#1E8449","🖊 Vyřeš sám/sama","🖊")
    body += '<div class="ex-body">'
    body += zadani("""Stavbu popisuje tabulka — číslo = počet krychliček nad sebou ve sloupci. Tři čísla jsou zakryta kartičkami K, L, M.
<ol class="task-list">
<li>V 1. stavbě je celkem 24 krychliček. Jaké číslo je zakryto kartičkou K?</li>
<li>Ve 2. stavbě se počet krychliček v 5. a 6. patře liší o 6. Jaké číslo skrývá L?</li>
</ol>""")
    body += scratch(5)
    body += answer_box()
    body += '</div></div>'

    body += ex_header(7,"Velká krychle — Klára odebírá krychličky","2021 &middot; 1. náhradní termín","#e8f5e9","#1E8449","🖊 Vyřeš sám/sama","🖊")
    body += '<div class="ex-body">'
    body += zadani("""Velká krychle má 4 vrstvy po 16 krychličkách. Klára odebrala krychličky podle nákresu 1, Mirek odebral z Klářiny stavby podle nákresu 2, Nora odebírala z Mirkovy stavby.
<ol class="task-list">
<li>Kolik krychliček odebrala Klára, aby vytvořila svou stavbu?</li>
<li>Kolik krychliček zbylo v Nořině stavbě?</li>
</ol>""")
    body += scratch(5)
    body += answer_box()
    body += '</div></div>'

    body += tip("👆","Vždy začni pohledem SHORA! Ten ti ukáže, kde jsou sloupce. Pak z každého pohledu přečteš výšky sloupců.","#e8faf5","#17A589")

    return body

# ═══════════════════════════════════════════
# MAIN &mdash; generate all files
# ═══════════════════════════════════════════════════

SHEETS = [
    (1,"Geometricka_konstrukce",  "1A5276","2980B9","D6EAF8","FFFFFF", pl01),
    (2,"Prostorova_predstavivost","0E6655","17A589","D1F2EB","FFFFFF", pl02),
    (3,"Posloupnosti_a_vzory",    "A04000","C87941","FDEBD0","FFFFFF", pl03),
    (4,"Grafy_pravdive_nepravdive","6C3483","9B59B6","F4ECF7","FFFFFF", pl04),
    (5,"Soustavy_podminek",       "1E8449","27AE60","D5F5E3","FFFFFF", pl05),
    (6,"Obvod_a_obsah",          "515A5A","7F8C8D","F2F3F4","FFFFFF", pl06),
    (7,"Vyrazy_a_zavorky",       "C0392B","E74C3C","FDEDEC","FFFFFF", pl07),
    (8,"Jednotky_a_prevody",     "784212","A56A2A","FAE5D3","FFFFFF", pl08),
    (9,"Pomery_a_zlomky",        "B7770D","D4AC0D","FEF9E7","FFFFFF", pl09),
]

for num, name, cd, cm, cl, ct, fn in SHEETS:
    print(f"Generuji PL{num:02d}_{name}...", end="", flush=True)
    body = fn()
    html = make_html(f"PL{num:02d} &mdash; {name.replace('_',' ')}", "", num, cd, cm, cl, ct, body)
    out_html = f"{OUTDIR}/PL{num:02d}_{name}.html"
    with open(out_html,"w",encoding="utf-8") as f:
        f.write(html)
    size = os.path.getsize(out_html)
    print(f" HTML OK ({size//1024} KB)", end="", flush=True)

    # Generate PDF via wkhtmltopdf
    out_pdf = f"{OUTDIR}/PL{num:02d}_{name}.pdf"
    import subprocess
    try:
        r = subprocess.run([
            "wkhtmltopdf",
            "--page-size", "A4",
            "--margin-top", "12mm",
            "--margin-bottom", "12mm",
            "--margin-left", "12mm",
            "--margin-right", "12mm",
            "--encoding", "utf-8",
            "--enable-local-file-access",
            "--zoom", "0.88",
            "--quiet",
            out_html,
            out_pdf
        ], capture_output=True, text=True)
        if r.returncode == 0:
            pdf_size = os.path.getsize(out_pdf)
            print(f" | PDF OK ({pdf_size//1024} KB)")
        else:
            print(f" | PDF ERR: {r.stderr[:80]}")
    except FileNotFoundError:
        print(" | PDF skip (wkhtmltopdf not installed)")

print("Hotovo!")
