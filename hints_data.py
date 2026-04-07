#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Obsah sekcí PRAVIDLA A TIPY + KVÍZ pro všechny pracovní listy."""

def fi(label="?"):
    """Viditelný rámeček pro doplnění hodnoty — místo □."""
    return f'<span class="fillin">{label}</span>'

def diag(svg_code, caption=""):
    cap = f'<div class="diagram-caption">{caption}</div>' if caption else ""
    return f'<div class="hint-diagram">{svg_code}{cap}</div>'

def calc_row(*steps):
    """Výpočetní řádek: střídají se hodnoty a operace."""
    parts = []
    for i, s in enumerate(steps):
        if i % 2 == 0:
            parts.append(f'<b>{s}</b>')
        else:
            parts.append(f'<span class="step-arrow">→ {s} →</span>')
    return f'<div class="hint-calc">{" ".join(parts)}</div>'

# ══════ SVG DIAGRAMS ══════

SVG_KRUZITKO = diag('''<svg viewBox="0 0 380 255" xmlns="http://www.w3.org/2000/svg" style="max-width:380px">
  <!-- Základna KM -->
  <line x1="80" y1="210" x2="260" y2="210" stroke="#1A5276" stroke-width="2.5"/>
  <!-- Kružnice z K (poloměr = KM = 180) -->
  <circle cx="80" cy="210" r="180" fill="none" stroke="#2980B9" stroke-width="1.8" stroke-dasharray="6,4"/>
  <!-- Kružnice z M (stejný poloměr) -->
  <circle cx="260" cy="210" r="180" fill="none" stroke="#C0392B" stroke-width="1.8" stroke-dasharray="6,4"/>
  <!-- Strany trojúhelníku KS a MS -->
  <line x1="80" y1="210" x2="170" y2="54" stroke="#27AE60" stroke-width="1.8"/>
  <line x1="260" y1="210" x2="170" y2="54" stroke="#27AE60" stroke-width="1.8"/>
  <!-- Body K, M, S -->
  <circle cx="80" cy="210" r="6" fill="#1A5276"/>
  <circle cx="260" cy="210" r="6" fill="#1A5276"/>
  <circle cx="170" cy="54" r="6" fill="#27AE60"/>
  <!-- Popisky -->
  <text x="62" y="232" font-size="16" font-weight="bold" fill="#1A5276" font-family="sans-serif">K</text>
  <text x="260" y="232" font-size="16" font-weight="bold" fill="#1A5276" font-family="sans-serif">M</text>
  <text x="160" y="44" font-size="16" font-weight="bold" fill="#27AE60" font-family="sans-serif">S</text>
  <!-- Legenda kružnic -->
  <text x="4" y="108" font-size="12" fill="#2980B9" font-family="sans-serif">kružnice z K</text>
  <text x="280" y="108" font-size="12" fill="#C0392B" font-family="sans-serif">kružnice z M</text>
  <!-- Délky stran -->
  <text x="100" y="246" font-size="12" fill="#555" font-family="sans-serif">KM = KS = MS = stejná délka (rovnostranný!)</text>
</svg>''', "Rovnostranný trojúhelník KMS — průsečík dvou kružnic se stejným poloměrem")

SVG_OSA = diag('''<svg viewBox="0 0 320 180" xmlns="http://www.w3.org/2000/svg" style="max-width:320px">
  <line x1="40" y1="110" x2="280" y2="110" stroke="#1A5276" stroke-width="3"/>
  <circle cx="40" cy="110" r="5" fill="#1A5276"/>
  <circle cx="280" cy="110" r="5" fill="#1A5276"/>
  <text x="28" y="130" font-size="15" font-weight="bold" fill="#1A5276" font-family="sans-serif">A</text>
  <text x="278" y="130" font-size="15" font-weight="bold" fill="#1A5276" font-family="sans-serif">B</text>
  <circle cx="160" cy="110" r="4" fill="#E74C3C"/>
  <line x1="160" y1="15" x2="160" y2="160" stroke="#E74C3C" stroke-width="2.5" stroke-dasharray="6,4"/>
  <rect x="160" y="98" width="14" height="14" fill="none" stroke="#E74C3C" stroke-width="1.5"/>
  <text x="80" y="95" font-size="12" fill="#2980B9" font-family="sans-serif">stejně daleko</text>
  <text x="170" y="95" font-size="12" fill="#2980B9" font-family="sans-serif">stejně daleko</text>
  <text x="128" y="175" font-size="12" fill="#E74C3C" font-family="sans-serif">osa úsečky AB</text>
</svg>''', "Osa úsečky AB — kolmice procházející středem")

SVG_POHLEDY = diag('''<svg viewBox="0 0 440 230" xmlns="http://www.w3.org/2000/svg" style="max-width:440px">
  <text x="22" y="22" font-size="13" font-weight="bold" fill="#2980B9" font-family="sans-serif">Pohled SHORA</text>
  <rect x="22" y="32" width="32" height="32" fill="#BEE3F8" stroke="#2980B9" stroke-width="1.5"/>
  <rect x="54" y="32" width="32" height="32" fill="#BEE3F8" stroke="#2980B9" stroke-width="1.5"/>
  <rect x="22" y="64" width="32" height="32" fill="#9BC5E8" stroke="#2980B9" stroke-width="1.5"/>
  <rect x="54" y="64" width="32" height="32" fill="#BEE3F8" stroke="#2980B9" stroke-width="1.5"/>
  <text x="18" y="118" font-size="11" fill="#555" font-family="sans-serif">2×2 sloupce</text>
  <text x="18" y="132" font-size="11" fill="#555" font-family="sans-serif">kde jsou →</text>

  <text x="168" y="22" font-size="13" font-weight="bold" fill="#27AE60" font-family="sans-serif">Pohled ZEPŘEDU</text>
  <rect x="168" y="32" width="32" height="32" fill="#D5F5E3" stroke="#27AE60" stroke-width="1.5"/>
  <rect x="200" y="32" width="32" height="32" fill="#D5F5E3" stroke="#27AE60" stroke-width="1.5"/>
  <rect x="168" y="64" width="32" height="32" fill="#D5F5E3" stroke="#27AE60" stroke-width="1.5"/>
  <rect x="168" y="96" width="32" height="32" fill="#D5F5E3" stroke="#27AE60" stroke-width="1.5"/>
  <text x="162" y="148" font-size="11" fill="#555" font-family="sans-serif">výška 3 | výška 1</text>
  <text x="162" y="162" font-size="11" fill="#555" font-family="sans-serif">(vždy nejv. sloupec)</text>

  <text x="318" y="22" font-size="13" font-weight="bold" fill="#E67E22" font-family="sans-serif">Pohled ZPRAVA</text>
  <rect x="318" y="32" width="32" height="32" fill="#FDEBD0" stroke="#E67E22" stroke-width="1.5"/>
  <rect x="318" y="64" width="32" height="32" fill="#FDEBD0" stroke="#E67E22" stroke-width="1.5"/>
  <rect x="318" y="96" width="32" height="32" fill="#FDEBD0" stroke="#E67E22" stroke-width="1.5"/>
  <rect x="350" y="96" width="32" height="32" fill="#FAD7A0" stroke="#E67E22" stroke-width="1.5"/>
  <text x="310" y="148" font-size="11" fill="#555" font-family="sans-serif">hloubka 2 řady</text>
  <text x="310" y="162" font-size="11" fill="#555" font-family="sans-serif">(pravý okraj každé řady)</text>
</svg>''', "Tři pohledy na stavbu z kostek — každý ukazuje něco jiného")

SVG_VENN = diag('''<svg viewBox="0 0 380 230" xmlns="http://www.w3.org/2000/svg" style="max-width:380px">
  <circle cx="155" cy="95" r="75" fill="#D6EAF8" fill-opacity=".75" stroke="#2980B9" stroke-width="2"/>
  <circle cx="225" cy="95" r="75" fill="#D5F5E3" fill-opacity=".75" stroke="#27AE60" stroke-width="2"/>
  <circle cx="190" cy="155" r="75" fill="#FDEBD0" fill-opacity=".75" stroke="#E67E22" stroke-width="2"/>
  <text x="100" y="70" font-size="13" font-weight="bold" fill="#1A5276" font-family="sans-serif">Sport 14</text>
  <text x="240" y="70" font-size="13" font-weight="bold" fill="#145A32" font-family="sans-serif">Div. 12</text>
  <text x="165" y="215" font-size="13" font-weight="bold" fill="#784212" font-family="sans-serif">Roboti 6</text>
  <text x="178" y="93" font-size="12" fill="#333" font-family="sans-serif" text-anchor="middle">8 dětí</text>
  <text x="178" y="107" font-size="11" fill="#555" font-family="sans-serif" text-anchor="middle">(právě 2 kr.)</text>
  <text x="190" y="133" font-size="13" font-weight="bold" fill="#922B21" font-family="sans-serif" text-anchor="middle">3</text>
  <text x="190" y="147" font-size="11" fill="#922B21" font-family="sans-serif" text-anchor="middle">(všechny 3)</text>
</svg>''', "Vennův diagram — kroužky SEN (23r1): celkem 18 dětí")

SVG_SOUCET_T = diag('''<svg viewBox="0 0 340 185" xmlns="http://www.w3.org/2000/svg" style="max-width:340px">
  <rect x="20" y="15" width="58" height="44" rx="8" fill="#EAF2FF" stroke="#2980B9" stroke-width="2"/>
  <rect x="141" y="15" width="58" height="44" rx="8" fill="#EAF2FF" stroke="#2980B9" stroke-width="2"/>
  <rect x="262" y="15" width="58" height="44" rx="8" fill="#EAF2FF" stroke="#2980B9" stroke-width="2"/>
  <text x="49" y="44" font-size="20" font-weight="bold" fill="#1A5276" font-family="sans-serif" text-anchor="middle">A</text>
  <text x="170" y="44" font-size="20" font-weight="bold" fill="#1A5276" font-family="sans-serif" text-anchor="middle">B</text>
  <text x="291" y="44" font-size="20" font-weight="bold" fill="#1A5276" font-family="sans-serif" text-anchor="middle">C</text>
  <text x="111" y="42" font-size="14" fill="#888" font-family="sans-serif">+</text>
  <text x="232" y="42" font-size="14" fill="#888" font-family="sans-serif">+</text>
  <line x1="78" y1="59" x2="111" y2="95" stroke="#aaa" stroke-width="1.5"/>
  <line x1="141" y1="59" x2="108" y2="95" stroke="#aaa" stroke-width="1.5"/>
  <line x1="199" y1="59" x2="232" y2="95" stroke="#aaa" stroke-width="1.5"/>
  <line x1="262" y1="59" x2="229" y2="95" stroke="#aaa" stroke-width="1.5"/>
  <rect x="80" y="95" width="66" height="44" rx="8" fill="#D5F5E3" stroke="#27AE60" stroke-width="2"/>
  <rect x="194" y="95" width="66" height="44" rx="8" fill="#D5F5E3" stroke="#27AE60" stroke-width="2"/>
  <text x="113" y="124" font-size="16" font-weight="bold" fill="#145A32" font-family="sans-serif" text-anchor="middle">A+B</text>
  <text x="227" y="124" font-size="16" font-weight="bold" fill="#145A32" font-family="sans-serif" text-anchor="middle">B+C</text>
  <text x="168" y="122" font-size="14" fill="#888" font-family="sans-serif">+</text>
  <line x1="146" y1="139" x2="163" y2="165" stroke="#aaa" stroke-width="1.5"/>
  <line x1="194" y1="139" x2="177" y2="165" stroke="#aaa" stroke-width="1.5"/>
  <rect x="140" y="155" width="80" height="44" rx="8" fill="#FFF9C4" stroke="#F9A825" stroke-width="2.5"/>
  <text x="180" y="184" font-size="16" font-weight="bold" fill="#E65100" font-family="sans-serif" text-anchor="middle">A+2B+C</text>
</svg>''', "Součtový trojúhelník — součet dvou sousedních = číslo pod nimi")

SVG_SOUCET_PRIKLAD = diag('''<svg viewBox="0 0 300 190" xmlns="http://www.w3.org/2000/svg" style="max-width:300px">
  <rect x="10" y="10" width="66" height="48" rx="8" fill="#FDEDEC" stroke="#E74C3C" stroke-width="2.5"/>
  <rect x="117" y="10" width="66" height="48" rx="8" fill="#FDEDEC" stroke="#E74C3C" stroke-width="2.5"/>
  <rect x="224" y="10" width="66" height="48" rx="8" fill="#EAF2FF" stroke="#2980B9" stroke-width="2"/>
  <text x="43" y="41" font-size="22" font-weight="bold" fill="#C0392B" font-family="sans-serif" text-anchor="middle">?</text>
  <text x="150" y="41" font-size="22" font-weight="bold" fill="#C0392B" font-family="sans-serif" text-anchor="middle">?</text>
  <text x="257" y="41" font-size="22" font-weight="bold" fill="#1A5276" font-family="sans-serif" text-anchor="middle">8</text>
  <line x1="76" y1="58" x2="103" y2="88" stroke="#aaa" stroke-width="1.5"/>
  <line x1="117" y1="58" x2="90" y2="88" stroke="#aaa" stroke-width="1.5"/>
  <line x1="183" y1="58" x2="210" y2="88" stroke="#aaa" stroke-width="1.5"/>
  <line x1="224" y1="58" x2="197" y2="88" stroke="#aaa" stroke-width="1.5"/>
  <rect x="63" y="88" width="66" height="48" rx="8" fill="#D5F5E3" stroke="#27AE60" stroke-width="2"/>
  <rect x="171" y="88" width="66" height="48" rx="8" fill="#D5F5E3" stroke="#27AE60" stroke-width="2"/>
  <text x="96" y="119" font-size="18" font-weight="bold" fill="#145A32" font-family="sans-serif" text-anchor="middle">2?</text>
  <text x="204" y="119" font-size="18" font-weight="bold" fill="#145A32" font-family="sans-serif" text-anchor="middle">?+8</text>
  <line x1="129" y1="136" x2="150" y2="158" stroke="#aaa" stroke-width="1.5"/>
  <line x1="171" y1="136" x2="150" y2="158" stroke="#aaa" stroke-width="1.5"/>
  <rect x="117" y="152" width="66" height="48" rx="8" fill="#FFF9C4" stroke="#F9A825" stroke-width="2.5"/>
  <text x="150" y="183" font-size="22" font-weight="bold" fill="#E65100" font-family="sans-serif" text-anchor="middle">44</text>
</svg>''', "Příklad: obě ? jsou stejná → 3? + 8 = 44 → ? = 12")

SVG_ZEBRIK = diag('''<svg viewBox="0 0 430 130" xmlns="http://www.w3.org/2000/svg" style="max-width:430px">
  <rect x="8" y="50" width="414" height="32" rx="16" fill="#FDF3E7" stroke="#E8D5B0" stroke-width="1.5"/>
  <text x="42" y="72" font-size="17" font-weight="800" fill="#784212" font-family="sans-serif" text-anchor="middle">km</text>
  <text x="134" y="72" font-size="17" font-weight="800" fill="#784212" font-family="sans-serif" text-anchor="middle">m</text>
  <text x="226" y="72" font-size="17" font-weight="800" fill="#784212" font-family="sans-serif" text-anchor="middle">dm</text>
  <text x="318" y="72" font-size="17" font-weight="800" fill="#784212" font-family="sans-serif" text-anchor="middle">cm</text>
  <text x="400" y="72" font-size="17" font-weight="800" fill="#784212" font-family="sans-serif" text-anchor="middle">mm</text>
  <text x="88" y="34" font-size="12" fill="#A56A2A" font-family="sans-serif" text-anchor="middle">× 1000</text>
  <text x="180" y="34" font-size="12" fill="#A56A2A" font-family="sans-serif" text-anchor="middle">× 10</text>
  <text x="272" y="34" font-size="12" fill="#A56A2A" font-family="sans-serif" text-anchor="middle">× 10</text>
  <text x="360" y="34" font-size="12" fill="#A56A2A" font-family="sans-serif" text-anchor="middle">× 10</text>
  <path d="M66,46 Q88,26 110,46" fill="none" stroke="#A56A2A" stroke-width="1.8" marker-end="url(#arr)"/>
  <path d="M158,46 Q180,26 202,46" fill="none" stroke="#A56A2A" stroke-width="1.8" marker-end="url(#arr)"/>
  <path d="M250,46 Q272,26 294,46" fill="none" stroke="#A56A2A" stroke-width="1.8" marker-end="url(#arr)"/>
  <path d="M342,46 Q360,26 380,46" fill="none" stroke="#A56A2A" stroke-width="1.8" marker-end="url(#arr)"/>
  <text x="88" y="108" font-size="12" fill="#A56A2A" font-family="sans-serif" text-anchor="middle">÷ 1000</text>
  <text x="180" y="108" font-size="12" fill="#A56A2A" font-family="sans-serif" text-anchor="middle">÷ 10</text>
  <text x="272" y="108" font-size="12" fill="#A56A2A" font-family="sans-serif" text-anchor="middle">÷ 10</text>
  <text x="360" y="108" font-size="12" fill="#A56A2A" font-family="sans-serif" text-anchor="middle">÷ 10</text>
  <path d="M110,86 Q88,106 66,86" fill="none" stroke="#A56A2A" stroke-width="1.8" marker-end="url(#arr)"/>
  <path d="M202,86 Q180,106 158,86" fill="none" stroke="#A56A2A" stroke-width="1.8" marker-end="url(#arr)"/>
  <path d="M294,86 Q272,106 250,86" fill="none" stroke="#A56A2A" stroke-width="1.8" marker-end="url(#arr)"/>
  <path d="M380,86 Q360,106 342,86" fill="none" stroke="#A56A2A" stroke-width="1.8" marker-end="url(#arr)"/>
  <text x="8" y="34" font-size="10" fill="#888" font-family="sans-serif">na menší →</text>
  <text x="8" y="108" font-size="10" fill="#888" font-family="sans-serif">na větší →</text>
</svg>''', "Žebřík délkových jednotek: doleva násobíš (menší), doprava dělíš (větší)")

SVG_SIPKY = diag('''<svg viewBox="0 0 460 110" xmlns="http://www.w3.org/2000/svg" style="max-width:460px">
  <!-- Box: x (vstupní číslo) -->
  <rect x="5" y="18" width="56" height="44" rx="8" fill="#FDEBD0" stroke="#E67E22" stroke-width="2.5"/>
  <text x="33" y="38" font-size="11" fill="#888" font-family="sans-serif" text-anchor="middle">vstup</text>
  <text x="33" y="55" font-size="20" font-weight="bold" fill="#E65100" font-family="sans-serif" text-anchor="middle">x</text>
  <!-- Op: ÷2 -->
  <rect x="72" y="24" width="48" height="32" rx="6" fill="#EAF2FF" stroke="#2980B9" stroke-width="1.5"/>
  <text x="96" y="45" font-size="14" font-weight="bold" fill="#1A5276" font-family="sans-serif" text-anchor="middle">÷ 2</text>
  <line x1="61" y1="40" x2="72" y2="40" stroke="#bbb" stroke-width="2" marker-end="url(#arr)"/>
  <!-- Box: ? (výsledek po ÷2) -->
  <rect x="131" y="18" width="56" height="44" rx="8" fill="#EAF2FF" stroke="#2980B9" stroke-width="1.5"/>
  <text x="159" y="38" font-size="11" fill="#888" font-family="sans-serif" text-anchor="middle">po ÷2</text>
  <text x="159" y="55" font-size="20" font-weight="bold" fill="#1A5276" font-family="sans-serif" text-anchor="middle">?</text>
  <!-- Op: +3 -->
  <rect x="198" y="24" width="48" height="32" rx="6" fill="#EAF2FF" stroke="#2980B9" stroke-width="1.5"/>
  <text x="222" y="45" font-size="14" font-weight="bold" fill="#1A5276" font-family="sans-serif" text-anchor="middle">+ 3</text>
  <line x1="187" y1="40" x2="198" y2="40" stroke="#bbb" stroke-width="2" marker-end="url(#arr)"/>
  <!-- Box: ? (výsledek po +3) -->
  <rect x="257" y="18" width="56" height="44" rx="8" fill="#EAF2FF" stroke="#2980B9" stroke-width="1.5"/>
  <text x="285" y="38" font-size="11" fill="#888" font-family="sans-serif" text-anchor="middle">po +3</text>
  <text x="285" y="55" font-size="20" font-weight="bold" fill="#1A5276" font-family="sans-serif" text-anchor="middle">?</text>
  <!-- Op: ×5 -->
  <rect x="324" y="24" width="48" height="32" rx="6" fill="#EAF2FF" stroke="#2980B9" stroke-width="1.5"/>
  <text x="348" y="45" font-size="14" font-weight="bold" fill="#1A5276" font-family="sans-serif" text-anchor="middle">× 5</text>
  <line x1="313" y1="40" x2="324" y2="40" stroke="#bbb" stroke-width="2" marker-end="url(#arr)"/>
  <!-- Box: 25 (výsledek) -->
  <rect x="383" y="18" width="66" height="44" rx="8" fill="#D5F5E3" stroke="#27AE60" stroke-width="2.5"/>
  <text x="416" y="38" font-size="11" fill="#888" font-family="sans-serif" text-anchor="middle">výsledek</text>
  <text x="416" y="55" font-size="20" font-weight="bold" fill="#145A32" font-family="sans-serif" text-anchor="middle">25</text>
  <line x1="373" y1="40" x2="383" y2="40" stroke="#bbb" stroke-width="2" marker-end="url(#arr)"/>
  <!-- Caption: backward path -->
  <text x="230" y="85" font-size="11" fill="#555" font-family="sans-serif" text-anchor="middle">Pozpátku: 25 ÷5 = 5 → 5−3 = 2 → 2×2 = 4 → x = 4</text>
  <text x="230" y="100" font-size="11" fill="#27AE60" font-family="sans-serif" text-anchor="middle">Ověř dopředu: 4 ÷2 = 2, 2+3 = 5, 5×5 = 25 ✓</text>
</svg>''', "Diagram šipek — neznámé číslo x prochází třemi operacemi a dá výsledek 25")

SVG_MAGICKA = diag('''<svg viewBox="0 0 260 210" xmlns="http://www.w3.org/2000/svg" style="max-width:260px">
  <rect x="30" y="20" width="56" height="56" rx="6" fill="#EAF2FF" stroke="#2980B9" stroke-width="1.5"/>
  <!-- Row 1: 1, ?, 5  (zadáno 1 a 5, hledáme ?) -->
  <rect x="86" y="20" width="56" height="56" rx="6" fill="#FDEBD0" stroke="#E67E22" stroke-width="2.5"/>
  <rect x="142" y="20" width="56" height="56" rx="6" fill="#EAF2FF" stroke="#2980B9" stroke-width="1.5"/>
  <text x="58" y="55" font-size="22" font-weight="bold" fill="#1A5276" font-family="sans-serif" text-anchor="middle">1</text>
  <text x="114" y="55" font-size="22" font-weight="bold" fill="#E65100" font-family="sans-serif" text-anchor="middle">?</text>
  <text x="170" y="55" font-size="22" font-weight="bold" fill="#1A5276" font-family="sans-serif" text-anchor="middle">5</text>
  <!-- Row 2: ?, ?, ?  (střed odvozuješ v Kroku 2 — je to prostřední číslo ze sady!) -->
  <rect x="30" y="76" width="56" height="56" rx="6" fill="#FDEBD0" stroke="#E67E22" stroke-width="2.5"/>
  <rect x="86" y="76" width="56" height="56" rx="6" fill="#FDEBD0" stroke="#E67E22" stroke-width="2.5"/>
  <rect x="142" y="76" width="56" height="56" rx="6" fill="#FDEBD0" stroke="#E67E22" stroke-width="2.5"/>
  <text x="58" y="111" font-size="22" font-weight="bold" fill="#E65100" font-family="sans-serif" text-anchor="middle">?</text>
  <text x="114" y="111" font-size="22" font-weight="bold" fill="#E65100" font-family="sans-serif" text-anchor="middle">?</text>
  <text x="170" y="111" font-size="22" font-weight="bold" fill="#E65100" font-family="sans-serif" text-anchor="middle">?</text>
  <!-- Row 3: 3, ?, 7  (zadáno 3 a 7, hledáme ?) -->
  <rect x="30" y="132" width="56" height="56" rx="6" fill="#EAF2FF" stroke="#2980B9" stroke-width="1.5"/>
  <rect x="86" y="132" width="56" height="56" rx="6" fill="#FDEBD0" stroke="#E67E22" stroke-width="2.5"/>
  <rect x="142" y="132" width="56" height="56" rx="6" fill="#EAF2FF" stroke="#2980B9" stroke-width="1.5"/>
  <text x="58" y="167" font-size="22" font-weight="bold" fill="#1A5276" font-family="sans-serif" text-anchor="middle">3</text>
  <text x="114" y="167" font-size="22" font-weight="bold" fill="#E65100" font-family="sans-serif" text-anchor="middle">?</text>
  <text x="170" y="167" font-size="22" font-weight="bold" fill="#1A5276" font-family="sans-serif" text-anchor="middle">7</text>
  <!-- Row sum labels -->
  <text x="210" y="52" font-size="13" font-weight="bold" fill="#27AE60" font-family="sans-serif">= 12</text>
  <text x="210" y="108" font-size="13" font-weight="bold" fill="#27AE60" font-family="sans-serif">= 12</text>
  <text x="210" y="164" font-size="13" font-weight="bold" fill="#27AE60" font-family="sans-serif">= 12</text>
</svg>''', "Magická tabulka — zadaná čísla (modrá) a políčka k doplnění (oranžová ?). Střed zjistíš v Kroku 2!")

SVG_OSOVA = diag('''<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="max-width:360px">
  <rect x="20" y="30" width="36" height="36" rx="4" fill="#BEE3F8" stroke="#2980B9" stroke-width="1.5"/>
  <rect x="56" y="30" width="36" height="36" rx="4" fill="#BEE3F8" stroke="#2980B9" stroke-width="1.5"/>
  <rect x="20" y="66" width="36" height="36" rx="4" fill="#BEE3F8" stroke="#2980B9" stroke-width="1.5"/>
  <rect x="56" y="66" width="36" height="36" rx="4" fill="#BEE3F8" stroke="#2980B9" stroke-width="1.5"/>
  <rect x="20" y="102" width="36" height="36" rx="4" fill="#BEE3F8" stroke="#2980B9" stroke-width="1.5"/>
  <rect x="56" y="102" width="36" height="36" rx="4" fill="#FDEDEC" stroke="#E74C3C" stroke-width="2.5" stroke-dasharray="5,3"/>
  <line x1="38" y1="16" x2="38" y2="152" stroke="#E74C3C" stroke-width="2.5" stroke-dasharray="7,4"/>
  <text x="12" y="162" font-size="11" fill="#E74C3C" font-family="sans-serif">tento nemá</text>
  <text x="12" y="175" font-size="11" fill="#E74C3C" font-family="sans-serif">protějšek!</text>
  <text x="12" y="188" font-size="11" fill="#E74C3C" font-family="sans-serif">→ odebereme</text>
  <text x="155" y="90" font-size="28" fill="#888" font-family="sans-serif">→</text>
  <rect x="200" y="30" width="36" height="36" rx="4" fill="#D5F5E3" stroke="#27AE60" stroke-width="1.5"/>
  <rect x="236" y="30" width="36" height="36" rx="4" fill="#D5F5E3" stroke="#27AE60" stroke-width="1.5"/>
  <rect x="200" y="66" width="36" height="36" rx="4" fill="#D5F5E3" stroke="#27AE60" stroke-width="1.5"/>
  <rect x="236" y="66" width="36" height="36" rx="4" fill="#D5F5E3" stroke="#27AE60" stroke-width="1.5"/>
  <rect x="200" y="102" width="36" height="36" rx="4" fill="#D5F5E3" stroke="#27AE60" stroke-width="1.5"/>
  <line x1="218" y1="16" x2="218" y2="152" stroke="#E74C3C" stroke-width="2.5" stroke-dasharray="7,4"/>
  <text x="193" y="168" font-size="11" fill="#27AE60" font-family="sans-serif">symetrický ✓</text>
  <text x="193" y="181" font-size="11" fill="#27AE60" font-family="sans-serif">po odebrání</text>
</svg>''', "Osová souměrnost — odeber čtverec bez zrcadlového protějšku")


# ══════════════════════════════════════════════════════════════════
# PL01 — GEOMETRICKÁ KONSTRUKCE
# ══════════════════════════════════════════════════════════════════
HINTS_PL01 = [

("📖", "Jak číst zadání — 5 kroků před rýsováním", f"""
<ol>
<li>Přečti POMALU — <b>poprvé</b> jen pro pochopení, <b>podruhé</b> hledej podmínky</li>
<li>Každou podmínku <b>podtrhni nebo zakroužkuj</b> přímo v zadání</li>
<li>Nakresli si <b>hrubý náčrt od ruky</b> — jak by to mohlo vypadat</li>
<li>Teprve pak rýsuj <b>pravítkem a kružítkem</b> přesně</li>
<li>Na konci zkontroluj <b>každou podmínku zvlášť</b> — všechny musí platit!</li>
</ol>
<div class="ex"><div class="lbl">Nejčastější chyba</div>
Žáci začnou rýsovat dříve, než přečtou celé zadání. Pak zjistí, že poloha bodu nesedí. Vždy přečti celé zadání — teprve pak rýsuj!</div>""", "#e8f4ff", "#1A5276"),

("🔵", "Kružítko — rovnostranný trojúhelník krok za krokem", f"""
{SVG_KRUZITKO}
<div class="ex"><div class="lbl">Proč to funguje</div>
Rovnostranný trojúhelník má KS = MS = KM. Kružnice z K zachytí všechny body ve vzdálenosti KM od K. Kružnice z M zachytí všechny body ve vzdálenosti KM od M. Bod S leží na obou → v jejich průsečíku.
</div>
<div class="ex"><div class="lbl">Postup krok za krokem</div>
<ol>
<li>Změř kružítkem délku KM (nastav poloměr přesně na KM)</li>
<li>Z bodu K narýsuj kružnici s tímto poloměrem</li>
<li>BEZ ZMĚNY poloměru narýsuj kružnici i z bodu M</li>
<li>Průsečíky obou kružnic = možné polohy bodu S</li>
<li>Bývají <b>dva průsečíky</b> = dvě řešení — obě nakresli!</li>
</ol>
</div>""", "#e8f4ff", "#2980B9"),

("📏", "Osa úsečky — co to je a jak ji narýsovat", f"""
{SVG_OSA}
<div class="ex"><div class="lbl">Co je osa úsečky AB</div>
<ul>
<li>Prochází přesně <b>středem</b> úsečky AB</li>
<li>Je <b>kolmá</b> na úsečku AB (svírá 90°)</li>
<li>Každý bod na ose je <b>stejně daleko od A i od B</b></li>
</ul>
</div>
<div class="ex"><div class="lbl">Jak narýsovat kružítkem</div>
<ol>
<li>Nastav kružítko na poloměr <b>větší než polovina AB</b></li>
<li>Z A narýsuj kružnici — ze stejným poloměrem narýsuj kružnici i z B</li>
<li>Spoj oba průsečíky kružnic = to je osa úsečky</li>
</ol>
</div>""", "#e8f4ff", "#1A5276"),

("📐", "Rovnoběžka přes bod a klíčové pojmy", f"""
<div class="ex"><div class="lbl">Jak narýsovat rovnoběžku přes bod K s přímkou r</div>
<ol>
<li>Přilož pravítko těsně <b>podél přímky r</b></li>
<li>Přilož trojúhelník k pravítku jako zarážku (aby se pravítko nesklouz.</li>
<li>Posuň pravítko podél zarážky tak, aby procházelo bodem <b>K</b></li>
<li>Narýsuj přímku — je rovnoběžná s r!</li>
</ol>
</div>
<table class="htable">
<tr><th style="background:#1A5276;color:white">Pojem</th><th style="background:#1A5276;color:white">Co to je</th></tr>
<tr><td><b>Rovnoběžky</b></td><td>Nikdy se neprotnou — jsou stále stejně daleko od sebe</td></tr>
<tr><td><b>Kolmice</b></td><td>Svírají přesně pravý úhel (90°)</td></tr>
<tr><td><b>Osa úsečky</b></td><td>Kolmice středem — každý bod je stejně daleko od obou konců</td></tr>
<tr><td><b>Rovnostranný △</b></td><td>Všechny 3 strany stejně dlouhé</td></tr>
<tr><td><b>Rovnoramenný △</b></td><td>2 strany stejně dlouhé (ramena), třetí jiná (základna)</td></tr>
</table>""", "#e8f4ff", "#1A5276"),

("🔍", "Proč bývají 2 řešení — a jak je systematicky najít", f"""
<div class="ex"><div class="lbl">Kdy vznikají 2 řešení</div>
<ul>
<li>Bod může ležet na přímce <b>vlevo i vpravo</b> od jiného bodu</li>
<li>Trojúhelník může být <b>nad i pod</b> zadanou přímkou</li>
<li>Dvě kružnice se protínají ve <b>dvou bodech</b></li>
</ul>
</div>
<div class="ex"><div class="lbl">Systematický postup</div>
<ol>
<li>Narýsuj první řešení přesně</li>
<li>Zeptej se: „Může bod ležet i na druhé straně?"</li>
<li>Pokud ano — narýsuj druhé řešení</li>
<li>Obě řešení zkontroluj ve <b>všech podmínkách</b></li>
<li>Zapiš závěr: „Nalezena 2 řešení" nebo „Nalezeno 1 řešení"</li>
</ol>
</div>
<div class="ex"><div class="lbl">Jak kontrolovat kružítkem</div>
Nastav kružítko na délku KM. Bez změny přenes na KS — pasuje? Pak jsou stejně dlouhé.</div>""", "#e8f4ff", "#2980B9"),

("⚠️", "Nejčastější chyby při rýsování", f"""
<table class="htable">
<tr><th style="background:#C0392B;color:white">Chyba</th><th style="background:#C0392B;color:white">Jak to správně</th></tr>
<tr><td>🔴 Začnu rýsovat dříve, než přečtu celé zadání</td><td>Přečti 2× — až pak rýsuj</td></tr>
<tr><td>🔴 Pro druhý oblouk změním nastavení kružítka</td><td>Kružítko NIKDY nepřenastavuješ — drž ho přesně stejně</td></tr>
<tr><td>🔴 Narýsuji jen jedno řešení, ačkoliv existují dvě</td><td>Vždy se zeptej: „Může bod ležet i na druhé straně?"</td></tr>
<tr><td>🔴 Zapomenu označit body písmeny (K, M, S...)</td><td>Bez popisků dostaneš 0 bodů — piš písmena hned</td></tr>
<tr><td>🔴 Kružnice je čára, ne tečka — narýsuji jen část</td><td>Narýsuj celou kružnici (nebo aspoň přes místo průsečíku)</td></tr>
</table>
<div class="ex" style="background:#fff8f8;border-left:3px solid #E74C3C"><b>Zlaté pravidlo:</b> Po narýsování projdi KAŽDOU podmínku ze zadání a zkontroluj, zda tvůj výkres splňuje všechny.</div>""", "#fff0f0", "#C0392B"),
]

# ══════════════════════════════════════════════════════════════════
# PL02 — PROSTOROVÁ PŘEDSTAVIVOST
# ══════════════════════════════════════════════════════════════════
HINTS_PL02 = [

("👁️", "Tři pohledy — co každý ukazuje", f"""
{SVG_POHLEDY}
<table class="htable">
<tr><th style="background:#0E6655;color:white">Pohled</th><th style="background:#0E6655;color:white">Co vidíš</th><th style="background:#0E6655;color:white">Co NEvidíš</th></tr>
<tr><td>🔼 <b>Shora</b></td><td>Kde jsou sloupce (jako mapa)</td><td>Jak jsou vysoké</td></tr>
<tr><td>⬛ <b>Zepředu</b></td><td>Šířka + výška. Vždy <b>nejvyšší</b> sloupec v každé řadě</td><td>Kolik jich je za sebou</td></tr>
<tr><td>▶️ <b>Zprava</b></td><td>Hloubka + výška. Pravý okraj každé řady</td><td>Co je za prvním sloupcem</td></tr>
</table>""", "#e8faf5", "#0E6655"),

("🔢", "Jak spočítat kostky ze dvou pohledů — s příkladem", f"""
<div class="ex"><div class="lbl">Jak může zadání vypadat</div>
<i>„Stavba z kostek má pohled shora 2×2, pohled zepředu: levý sloupec výška 3, pravý výška 1. Kolik kostek stavba obsahuje?"</i>
</div>
<div class="ex"><div class="lbl">Krok 1: Z pohledu SHORA nakresli plán</div>
Pohled shora = mapa sloupců. 2×2 = 4 sloupce (jako šachovnice 2×2):
<table class="htable" style="max-width:220px;text-align:center">
<tr><th style="background:#17A589;color:white">← vlevo</th><th style="background:#17A589;color:white">vpravo →</th></tr>
<tr><td><b>A</b> přední-levý</td><td><b>B</b> přední-pravý</td></tr>
<tr><td><b>C</b> zadní-levý</td><td><b>D</b> zadní-pravý</td></tr>
</table>
Pohled zepředu vidí jen <b>přední řadu</b> (A, B) — ale ukazuje výšku celého sloupce (max. z A a C, max. z B a D).
</div>
<div class="ex"><div class="lbl">Krok 2: Z pohledu ZEPŘEDU doplň výšky</div>
Pohled zepředu: levá strana výška 3, pravá výška 1.<br>
→ Levý sloupec (A vpředu, C vzadu) → výška <b>3</b><br>
→ Pravý sloupec (B vpředu, D vzadu) → výška <b>1</b>
<table class="htable" style="max-width:180px;text-align:center">
<tr><td><b>A = 3</b></td><td><b>B = 1</b></td></tr>
<tr><td><b>C = 3</b></td><td><b>D = 1</b></td></tr>
</table>
</div>
<div class="ex"><div class="lbl">Krok 3: Každý sloupec × výška = počet kostek</div>
A: 3 kostek, B: 1 kostka, C: 3 kostky, D: 1 kostka<br>
Celkem: 3+1+3+1 = <span class="hint-result">8 kostek</span>
</div>
<div class="ex"><div class="lbl">Klíčové pravidlo o pohledu zepředu</div>
Pohled zepředu nikdy neukazuje, <b>kolik kostek je za sebou</b> — vidí jen <b>nejvyšší</b> v dané řadě. Proto potřebuješ pohled shora, abys věděl, kde jsou sloupce!
</div>""", "#e8faf5", "#17A589"),

("📦", "Skryté kostky — pravidlo 6 stěn", f"""
<div class="ex"><div class="lbl">Co je skrytá kostka</div>
Kostka je skrytá, když ze žádné strany není vidět — všech 6 stěn sousedí s jinou kostkou nebo podložkou.
</div>
<div class="ex"><div class="lbl">Skrytá kostka NESMÍ být</div>
<ul>
<li>v <b>nejnižší vrstvě</b> — dotýká se podložky → viditelná zdola</li>
<li>na <b>okraji stavby</b> → viditelná z některé strany</li>
</ul>
</div>
<div class="ex"><div class="lbl">Pyramida 5 pater — počet skrytých</div>
<table class="htable">
<tr><th style="background:#0E6655;color:white">Patro</th><th style="background:#0E6655;color:white">Rozměr</th><th style="background:#0E6655;color:white">Skrytých</th><th style="background:#0E6655;color:white">Proč</th></tr>
<tr><td>1. (spodní)</td><td>5×5 = 25</td><td><b>0</b></td><td>dotýká se podložky</td></tr>
<tr><td>2.</td><td>4×4 = 16</td><td><b>4</b></td><td>vnitřní 2×2 = 4 skryté</td></tr>
<tr><td>3.</td><td>3×3 = 9</td><td><b>1</b></td><td>vnitřní 1×1 = 1 skrytá</td></tr>
<tr><td>4. a 5.</td><td>2×2, 1×1</td><td><b>0</b></td><td>vše na okraji</td></tr>
</table>
Celkem: 4 + 1 = <span class="hint-result">5 skrytých kostek</span></div>""", "#e8faf5", "#0E6655"),

("⚫", "Kostky s tečkami — slepování a počítání", f"""
<div class="ex"><div class="lbl">Jedna kostka — základní fakta</div>
<ul>
<li>3 stěny mají po <b>1 tečce</b>, 3 stěny mají po <b>3 tečkách</b></li>
<li>Protilehlé stěny dávají vždy 1+3 = <b>4 tečky</b></li>
<li>Celkem: 3×1 + 3×3 = <span class="hint-result">12 teček</span> na jedné kostce</li>
</ul>
</div>
<div class="ex"><div class="lbl">Slepení = skryji stěny (2 stěny za každý spoj)</div>
<ul>
<li>Chci <b>maximum</b> teček → skryji stěny po <b>1 tečce</b> (ztratím co nejméně)</li>
<li>Chci <b>minimum</b> teček → skryji stěny po <b>3 tečkách</b> (ztratím co nejvíce)</li>
</ul>
</div>
<div class="ex"><div class="lbl">3 kostky v L-tvaru (2 spoje)</div>
Celkem: 3 × 12 = 36 teček.<br>
Maximum (skryji 4× po 1): 36 − 4 = <span class="hint-result">32 teček</span><br>
Minimum (skryji 4× po 3): 36 − 12 = <span class="hint-result">24 teček</span></div>""", "#e8faf5", "#17A589"),

("🏗️", "Filipův model — krychle z tyček a kuliček", f"""
<table class="htable">
<tr><th style="background:#0E6655;color:white">Strana n</th><th style="background:#0E6655;color:white">Kuličky (n×n×n)</th><th style="background:#0E6655;color:white">Tyčky celkem</th><th style="background:#0E6655;color:white">Tyčky jen na hranách</th></tr>
<tr><td>n = 2</td><td>8</td><td>12</td><td>12</td></tr>
<tr><td>n = 3</td><td>27</td><td>54</td><td>24</td></tr>
<tr><td>n = 4</td><td><b>64</b></td><td>144</td><td>36</td></tr>
<tr><td>n = 5</td><td>125</td><td>300</td><td>48</td></tr>
</table>
<div class="ex"><div class="lbl">Vzorce</div>
<ul>
<li>Kuličky = n × n × n</li>
<li>Tyčky celkem = 3 × n × n × (n−1)</li>
<li>Tyčky na hranách = 12 × (n−1) &nbsp; <span style="color:#888">(krychle má 12 hran)</span></li>
</ul>
</div>""", "#e8faf5", "#0E6655"),

("🔵", "Diagram s kroužky — dosaď čísla do šipek", f"""
<div class="ex"><div class="lbl">Jak může zadání vypadat</div>
<i>„Do prázdných kroužků doplňte čísla tak, aby byly všechny výpočty provedené ve směru šipek správné. Stejná písmena = stejné číslo."</i>
</div>
<div class="ex"><div class="lbl">Vzorový příklad (z 23n1)</div>
Diagram: {fi('K')} → ÷K → −6 → +K → výsledek <b>2</b><br>
Zkus K=3: 3÷3=1, 1−6=−5... záporné číslo → K není 3<br>
Zkus K=4: 4÷4=1, 1−6=−5... stále záporné → K není 4<br>
Zkus K=3 jinak: podmínka je <b>÷K, −6, +K → 2</b><br>
Zapíši jako rovnici: (K÷K) − 6 + K = 2 → 1 − 6 + K = 2 → K = <span class="hint-result">7</span><br>
Ověř: 7÷7=1, 1−6=−5, −5+7 = <span class="hint-result">2 ✓</span>
</div>
<div class="ex"><div class="lbl">Postup — 3 kroky</div>
<ol>
<li>Přečti šipky zleva doprava — zapiš co se děje s číslem</li>
<li>Začni od místa, kde <b>výsledek znáš</b> (číslo v kroužku na konci)</li>
<li>Jdi <b>pozpátku</b> nebo zkus hodnoty systematicky (1, 2, 3, 4...)</li>
</ol>
</div>
<div class="ex"><div class="lbl">Klíčový trik — stejná písmena</div>
Pokud se v diagramu opakuje písmeno K, je to vždy <b>stejné číslo</b>.<br>
Napiš si rovnici: (výsledek první operace s K) → další operace → výsledný kroužek<br>
Pak rovnici vyřeš jako neznámé číslo.
</div>""", "#e8faf5", "#17A589"),

("🏷️", "Stěny s čísly — součty viditelných stěn", f"""
<div class="ex"><div class="lbl">Jak může zadání vypadat (21r1)</div>
<i>„Na stavbu z 16 krychliček napíšeme čísla: stěny viditelné zepředu=1, zezadu=2, zprava=3, zleva=4, shora=5. Spočti součet všech zapsaných čísel z každé strany."</i>
</div>
<div class="ex"><div class="lbl">Krok 1: Pochop co „viditelná stěna" znamená</div>
Každá krychlička má 6 stěn. Stěna je <b>viditelná</b>, pokud na ni není přiložená jiná krychlička.<br>
Krajní krychlička v řadě → stěna na okraji = viditelná ✓<br>
Krychlička uprostřed → stěny po stranách zakryté sousedy ✗
</div>
<div class="ex"><div class="lbl">Krok 2: Pro každou stranu spočti viditelné stěny</div>
Příklad: stavba 4×4×1 (16 krychliček v jedné vrstvě):<br>
→ Pohled shora: všech 16 stěn vidět → součet = 16×5 = <b>80</b><br>
→ Pohled zepředu: 4 stěny v přední řadě → součet = 4×1 = <b>4</b><br>
→ Pohled zprava: 4 stěny v pravém sloupci → součet = 4×3 = <b>12</b>
</div>
<div class="ex"><div class="lbl">Tip: Nakresli si plán shora</div>
Zakresli si stavbu jako tabulku (pohled shora). Pro každý pohled projdi celý okraj a spočti kolik stěn je vidět. Dej si pozor na vícepatrové stavby — vyšší patra přidávají stěny shora!
</div>""", "#e8faf5", "#0E6655"),

("⚠️", "Nejčastější chyby u prostorových úloh", f"""
<table class="htable">
<tr><th style="background:#C0392B;color:white">Chyba</th><th style="background:#C0392B;color:white">Jak to správně</th></tr>
<tr><td>🔴 Záměna pohledu ZPRAVA a ZEZADU</td><td>Zprava = pravý okraj každé řady (jak to vidíš z pravé strany)</td></tr>
<tr><td>🔴 Pohled zepředu = výška všech sloupců</td><td>Pohled zepředu ukazuje jen <b>nejvyšší</b> sloupec v každé řadě!</td></tr>
<tr><td>🔴 Při slepování: 1 spoj = 1 ztracená stěna</td><td>1 spoj = <b>2 ztracené stěny</b> (jedna z každé kostky)</td></tr>
<tr><td>🔴 U diagramu: záporný výsledek → „to nefunguje"</td><td>Záporná čísla jsou povolena — třeba −5+7 = 2 je správně!</td></tr>
<tr><td>🔴 U pyramidy: počítám vnější kostky jako skryté</td><td>Skrytá = ze ŽÁDNÉ strany ji nevidíš — na okraji/podložce vždy viditelná</td></tr>
</table>""", "#fff0f0", "#C0392B"),
]

# ══════════════════════════════════════════════════════════════════
# PL03 — POSLOUPNOSTI A VZORY
# ══════════════════════════════════════════════════════════════════
HINTS_PL03 = [

("🔍", "Jak rozpoznat typ posloupnosti — krok za krokem", f"""
<div class="ex"><div class="lbl">Jak může zadání vypadat</div>
<i>„V tabulce jsou čísla: 3, 7, 11, 15, 19, ... Doplňte 6. člen a zjistěte, kolik je 10. člen."</i>
</div>
<div class="ex"><div class="lbl">Krok 1: Spočti 1. rozdíly sousedních členů</div>
Série: 3, 7, 11, 15, 19<br>
Rozdíly: 7−3=<b>4</b>, 11−7=<b>4</b>, 15−11=<b>4</b>, 19−15=<b>4</b><br>
→ Všechny stejné! Jde o <b>přičítání stále stejného čísla</b> (+4).
</div>
<div class="ex"><div class="lbl">Krok 2: Pokud 1. rozdíly nejsou stejné, spočti 2. rozdíly</div>
Jiná série: 2, 6, 12, 20, 30<br>
1. rozdíly: 4, 6, 8, 10 (rostou!)<br>
2. rozdíly: 6−4=<b>2</b>, 8−6=<b>2</b>, 10−8=<b>2</b><br>
→ 2. rozdíly jsou stejné → jde o <b>rostoucí pásy</b> (typicky obrázky z trojúhelníků).
</div>
<table class="htable">
<tr><th style="background:#A04000;color:white">Typ</th><th style="background:#A04000;color:white">Příklad</th><th style="background:#A04000;color:white">Poznám tak</th></tr>
<tr><td><b>Stálý přírůstek</b></td><td>3, 7, 11, 15 (+4)</td><td>1. rozdíly jsou všechny stejné</td></tr>
<tr><td><b>Stálý úbytek</b></td><td>40, 34, 28, 22 (−6)</td><td>1. rozdíly jsou stejné (záporné)</td></tr>
<tr><td><b>Násobení</b></td><td>2, 6, 18, 54 (×3)</td><td>každý člen = předchozí × stejné číslo</td></tr>
<tr><td><b>Rostoucí pásy</b></td><td>2, 6, 12, 20, 30</td><td>2. rozdíly jsou stejné</td></tr>
</table>
<div class="ex"><div class="lbl">Krok 3: Pokračuj v nalezené sérii</div>
Série +4: 3, 7, 11, 15, 19, <span class="hint-result">23</span>, 27, 31, 35, <span class="hint-result">39</span><br>
6. člen = 23, 10. člen = 3 + 9×4 = <span class="hint-result">39</span>
</div>""", "#fff8f0", "#C87941"),

("➕", "Stálý přírůstek nebo úbytek — jak počítat", f"""
<div class="ex"><div class="lbl">Příklad: cyklista jede 5 dní, celkem 200 km, každý den o 6 km méně</div>
<ol>
<li>Označím 1. den jako {fi('?')} km</li>
<li>2. den = {fi('?')}−6, 3. den = {fi('?')}−12, 4. den = {fi('?')}−18, 5. den = {fi('?')}−24</li>
<li>Součet: 5×{fi('?')} − (0+6+12+18+24) = 200</li>
<li>5×{fi('?')} − 60 = 200 → 5×{fi('?')} = 260 → 1. den = <span class="hint-result">52 km</span></li>
</ol>
</div>
<div class="ex"><div class="lbl">Rychlý součet: (první + poslední) × počet ÷ 2</div>
Ověř: (52 + 28) × 5 ÷ 2 = 80 × 5 ÷ 2 = <span class="hint-result">200 ✓</span>
</div>""", "#fff8f0", "#A04000"),

("✖️", "Násobení — každý člen je X-krát větší", f"""
<div class="ex"><div class="lbl">Příklad: 1. skupina = 2, každá další je 4× větší, 3. skupina = 32</div>
<ol>
<li>Zkontroluj: 2×4 = 8 ✓, 8×4 = 32 ✓ → správně, jde o násobení 4</li>
<li>Jdu dopředu: 4. skupina = 32×4 = <span class="hint-result">128</span></li>
<li>Celkem 4 skupiny: 2+8+32+128 = <span class="hint-result">170 korálků</span></li>
</ol>
</div>
<div class="ex"><div class="lbl">Jak jít pozpátku (když znám pozdější člen)</div>
Znám 3. člen = 32, každý je 4× větší. 32 → ÷4 → 8 → ÷4 → 2
</div>""", "#fff8f0", "#C87941"),

("🔷", "Obrázky z trojúhelníků — tabulka je klíč", f"""
<div class="ex"><div class="lbl">Jak vyplnit tabulku</div>
<ol>
<li>Nakresli nebo spočítej první 2–3 obrázky</li>
<li>Zapiš počty do tabulky</li>
<li>Spočti rozdíly → a 2. rozdíly</li>
</ol>
</div>
<table class="htable">
<tr><th style="background:#A04000;color:white">Obrázek</th>
<th style="background:#A04000;color:white">1.</th><th style="background:#A04000;color:white">2.</th>
<th style="background:#A04000;color:white">3.</th><th style="background:#A04000;color:white">4.</th>
<th style="background:#A04000;color:white">5.</th></tr>
<tr><td>Celkem △</td><td>6</td><td>24</td><td>54</td><td>96</td><td>150</td></tr>
<tr><td>Přidaný pás</td><td>—</td><td>+18</td><td>+30</td><td>+42</td><td>+54</td></tr>
<tr><td>Šedých v pásu</td><td>3</td><td>9</td><td>15</td><td>21</td><td>27</td></tr>
<tr><td>2. rozdíl pásu</td><td>—</td><td>—</td><td>+12</td><td>+12</td><td>+12</td></tr>
</table>
<div class="ex"><div class="lbl">Co z toho plyne</div>
<ul>
<li>Šedých v pásu roste vždy o 6 → 6. pás = 27+6 = <b>33 šedých</b></li>
<li>Celkový počet šedých = součet všech pásů</li>
</ul>
</div>""", "#fff8f0", "#A04000"),

("🔄", "Tmavé čtverečky — rozšířený obrazec", f"""
<div class="ex"><div class="lbl">Vzorec pro počet tmavých čtverečků</div>
<b>Tmavých = (šířka světlé části + 2) + 2 × výška světlé části</b>
</div>
<div class="ex"><div class="lbl">Příklad: světlá část je 5 řad × 18 sloupců</div>
Tmavých = (18+2) + 2×5 = 20+10 = <span class="hint-result">30 tmavých čtverečků</span>
</div>
<div class="ex"><div class="lbl">Jak najít šířku: přidáme 30 tmavých, základní má 5 řad</div>
(šířka+2) + 2×5 = 30 → šířka+12 = 30 → šířka = <span class="hint-result">18 sloupců</span>
</div>""", "#fff8f0", "#C87941"),

("⬛", "Puntíky ve čtvercích — vzorec krok za krokem", f"""
<div class="ex"><div class="lbl">Jak může zadání vypadat (20r1, 21r1, 22n1)</div>
<i>„Obrazce jsou tvořeny puntíky uspořádanými do čtverců. Strana 2. obrazce má 3 puntíky, každý další má o 2 více. Kolik puntíků má 10. obrazec?"</i>
</div>
<div class="ex"><div class="lbl">Krok 1: Zjisti stranu n-tého obrazce</div>
<table class="htable">
<tr><th style="background:#A04000;color:white">Obrazec č.</th><th style="background:#A04000;color:white">1.</th><th style="background:#A04000;color:white">2.</th><th style="background:#A04000;color:white">3.</th><th style="background:#A04000;color:white">4.</th><th style="background:#A04000;color:white">5.</th><th style="background:#A04000;color:white">n.</th></tr>
<tr><td>Strana</td><td>1</td><td>3</td><td>5</td><td>7</td><td>9</td><td><b>2n−1</b></td></tr>
<tr><td>Puntíků celkem</td><td>1</td><td>9</td><td>25</td><td>49</td><td>81</td><td><b>(2n−1)²</b></td></tr>
</table>
Vzorec: strana n-tého obrazce = <b>2n−1</b>, celkem puntíků = <b>(2n−1)²</b>
</div>
<div class="ex"><div class="lbl">Krok 2: Dosaď</div>
10. obrazec: strana = 2×10−1 = <b>19 puntíků</b> na straně<br>
Celkem puntíků: 19×19 = ? &nbsp;→ Trik: 20×19 − 19 = 380−19 = <span class="hint-result">361 puntíků</span>
</div>
<div class="ex"><div class="lbl">Krok 3: Jak spočítat rozdíl dvou obrazců</div>
Rozdíl 9. a 11. obrazce = (2×11−1)² − (2×9−1)² = 21² − 17² = 441−289 = <span class="hint-result">152</span><br>
Trik: nemusíš počítat oba zvlášť — postačí (A+B)×(A−B) = (21+17)×(21−17) = 38×4 = 152 ✓
</div>""", "#fff8f0", "#C87941"),

("🔺", "Součtový trojúhelník — čísla do rámečků", f"""
{SVG_SOUCET_T}
<div class="ex"><div class="lbl">Jak funguje součtový trojúhelník</div>
Součet dvou sousedních čísel v jednom řádku = číslo <b>pod nimi</b>.<br>
Třeba: 3 a 7 sousedí → pod nimi je <b>10</b>.
</div>
<div class="ex"><div class="lbl">Krok 1: Znám vrchní řadu — jdu DOLŮ (sčítám)</div>
Horní řada: 3, 7, 2<br>
{calc_row('3 + 7', '= 10')} &nbsp;&nbsp; {calc_row('7 + 2', '= 9')}<br>
{calc_row('10 + 9', '= 19')} ← spodní číslo
</div>
{SVG_SOUCET_PRIKLAD}
<div class="ex"><div class="lbl">Krok 2: Znám spodní číslo a jedno horní — hledám neznámá (?)</div>
Příklad: pravé horní = 8, obě levá horní jsou stejná (?), spodní = 44<br>
Střední řada: levý součet = <b>2?</b>, pravý součet = <b>? + 8</b><br>
Spodní: 2? + (? + 8) = 44 → <b>3? = 36</b> → <span class="hint-result">? = 12</span><br>
Ověř: 12, 12, 8 → 24, 20 → 44 ✓
</div>
<div class="ex"><div class="lbl">Zlaté pravidlo pro hledání ?</div>
Zkus dosadit různá celá čísla a kontroluj zda vyjde správný součet dole.<br>
Nebo: zapíš rovnici (2? + ? + 8 = 44) a řeš krok za krokem bez závorek.
</div>""", "#fff8f0", "#A04000"),

("⚠️", "Nejčastější chyby u posloupností", f"""
<table class="htable">
<tr><th style="background:#C0392B;color:white">Chyba</th><th style="background:#C0392B;color:white">Jak to správně</th></tr>
<tr><td>🔴 U sirek: 1. obrazec má 9, takže n-tý = 9 + 4n</td><td>Správně: n-tý = 9 + 4×(n−1). Ověř: 1. = 9+0=9 ✓, 2. = 9+4=13 ✓</td></tr>
<tr><td>🔴 U puntíků: zapomenu odečíst vnitřní obrazec</td><td>Puntíky n-tého = celý čtverec (2n−1)² — NEZAPOMEŇ odečíst!</td></tr>
<tr><td>🔴 U tmavých čtverečků: záměna šířky a výšky</td><td>Šířka = počet sloupců světlé části, výška = počet řad</td></tr>
<tr><td>🔴 Zapomenu vypsat tabulku pro prvních 4–5 obrazců</td><td>Bez tabulky to nejde — vždy nakresli a vypiš hodnoty!</td></tr>
<tr><td>🔴 U rozdílu dvou obrazců: počítám oba zvlášť</td><td>Trik: (A+B)×(A−B) — např. 21²−17² = 38×4 = 152 (rychlejší!)</td></tr>
<tr><td>🔴 V součtovém trojúhelníku: sčítám špatně (odspodu nahoru)</td><td>Vždy jdi SHORA DOLŮ — součet sousedů je vždy POD nimi, ne nad!</td></tr>
</table>""", "#fff0f0", "#C0392B"),
]

# ══════════════════════════════════════════════════════════════════
# PL04 — GRAFY — PRAVDIVÉ NEBO NEPRAVDIVÉ
# ══════════════════════════════════════════════════════════════════
HINTS_PL04 = [

("📊", "5 kroků jak číst graf — VŽDY stejně", f"""
<div class="ex"><div class="lbl">Jak může zadání vypadat</div>
<i>„Graf znázorňuje kg vytříděného odpadu. Rozhodněte, která tvrzení jsou pravdivá (A) nebo nepravdivá (N)."</i>
</div>
<ol>
<li>Přečti <b>název grafu</b> — co se měřilo a v jakých jednotkách?</li>
<li>Přečti <b>svislou osu</b> — kolik je JEDEN dílek? Začíná od nuly?</li>
<li>Přečti <b>legendu</b> — co znamenají barvy sloupců nebo čar?</li>
<li>Odečti hodnoty VŠECH sloupců a <b>zapiš do tabulky tužkou</b> na papír!</li>
<li>Až pak ověřuj tvrzení — jedno po druhém, pro každé spočítej konkrétní číslo</li>
</ol>
<div class="ex"><div class="lbl">Jak odečíst hodnotu ze sloupce</div>
Sloupec sahá po 6. dílek. Osa: 1 dílek = 10 kg.<br>
{calc_row('6 dílky', '× 10 kg', '60 kg')} ← to je hodnota sloupce.
</div>
<div class="ex"><div class="lbl">⚠️ Nejčastější chyby</div>
<ul>
<li>Osa <b>nemusí začínat od nuly!</b> Vždy si ověř, kde osa začíná.</li>
<li>1 dílek nemusí být 10 — může být 5, 20, 50, 100... vždy přečti.</li>
<li>Záporné sloupce (dolů) = utraceno; kladné (nahoru) = ušetřeno.</li>
<li>Graf s mincemi — hodnoty jsou počty mincí, ale tvrzení mluví o <b>korunách</b> → přepočítej!</li>
</ul>
</div>""", "#f9f0ff", "#6C3483"),

("🔢", "Zlomková tvrzení — největší záludnost", f"""
<div class="ex"><div class="lbl">Klíčový trik: z KTERÉ hodnoty počítám zlomek</div>
„R vytřídil o třetinu méně <b>než S</b>" → třetinu počítám <b>ze S</b>, ne z R!<br>
Výpočet: R = S − S÷3
</div>
<table class="htable">
<tr><th style="background:#6C3483;color:white">Tvrzení</th><th style="background:#6C3483;color:white">Výpočet</th><th style="background:#6C3483;color:white">Příklad (základ=60)</th></tr>
<tr><td>o třetinu <b>více</b></td><td>Z + Z÷3</td><td>60 + 20 = <b>80</b></td></tr>
<tr><td>o třetinu <b>méně</b></td><td>Z − Z÷3</td><td>60 − 20 = <b>40</b></td></tr>
<tr><td><b>třetina</b> z</td><td>Z ÷ 3</td><td>60 ÷ 3 = <b>20</b></td></tr>
<tr><td>třikrát více</td><td>Z × 3</td><td>60 × 3 = <b>180</b></td></tr>
<tr><td>o šestinu menší</td><td>Z − Z÷6</td><td>60 − 10 = <b>50</b></td></tr>
</table>""", "#f9f0ff", "#9B59B6"),

("🔍", "Záludná slova — každé má svůj trik", f"""
<table class="htable">
<tr><th style="background:#6C3483;color:white">Slovo v tvrzení</th><th style="background:#6C3483;color:white">Co musíš udělat</th></tr>
<tr><td><b>„poprvé"</b></td><td>Zkontroluj VŠECHNY předchozí roky — ani jeden nesmí jít stejným směrem</td></tr>
<tr><td><b>„dohromady"</b></td><td>Sečti VŠECHNY skupiny (muži + ženy = celkem)</td></tr>
<tr><td><b>„za celou sezonu"</b></td><td>Sečti VŠECHNY měsíce — ne jen jeden!</td></tr>
<tr><td><b>„právě 3×"</b></td><td>Musí být přesně 3×, ne přibližně</td></tr>
<tr><td><b>„více než 1/9 z"</b></td><td>Spočítej 1/9 z celkového součtu, pak porovnej</td></tr>
</table>
<div class="ex"><div class="lbl">Jak ověřit „poprvé snížily v roce 2018"</div>
<ol>
<li>2015→2016: nesmí klesnout ✓</li>
<li>2016→2017: nesmí klesnout ✓</li>
<li>2017→2018: musí klesnout ✓</li>
<li>Pak je to skutečně <b>první</b> pokles</li>
</ol>
</div>""", "#f9f0ff", "#6C3483"),

("💰", "Mince a koruny — nezapomeň přepočítat!", f"""
<div class="ex"><div class="lbl">Proč je to záludné</div>
Grafy s kasičkou ukazují <b>počty mincí</b>, ale tvrzení mluví o <b>korunách</b>!
</div>
<div class="ex"><div class="lbl">Postup — vždy stejný</div>
<ol>
<li>Odečti počty mincí z grafu → zapiš do tabulky</li>
<li>Každý počet × 50 Kč = koruny</li>
<li>Teprve pak ověřuj tvrzení</li>
</ol>
</div>
<div class="ex"><div class="lbl">Příklad: Věra = 10 mincí, Tomáš = 2 mince</div>
{calc_row('10 mincí', '× 50', '500 Kč')} &nbsp;&nbsp; {calc_row('2 mince', '× 50', '100 Kč')}<br>
Tvrzení „Věra dala 5× více než Tomáš": 500 ÷ 100 = 5 → <span class="hint-result">A ✓</span>
</div>""", "#f9f0ff", "#9B59B6"),

("📋", "Grafy úspor — kladné a záporné sloupce", f"""
<div class="ex"><div class="lbl">Pravidlo čtení</div>
<ul>
<li>Sloupec <b>nahoru</b> = ušetřil → přičítám k aktuálnímu stavu</li>
<li>Sloupec <b>dolů</b> = utratil → odečítám od aktuálního stavu</li>
</ul>
</div>
<div class="ex"><div class="lbl">Příklad: Lukáš začínal se 600 Kč, 6 měsíců</div>
{calc_row('600', '+200', '800', '−150', '650', '+100', '750', '−300', '450', '+50', '500', '−400', '100 Kč')}
</div>
<div class="ex"><div class="lbl">Celkově ušetřil nebo utratil?</div>
Součet kladných: +200+100+50 = 350 Kč<br>
Součet záporných: 150+300+400 = 850 Kč<br>
350 &lt; 850 → celkově <b>utratil</b> (tvrzení „ušetřil celkově" = N)
</div>""", "#f9f0ff", "#6C3483"),

("📈", "Spojnicový graf — dvě čáry najednou", f"""
<div class="ex"><div class="lbl">Jak může zadání vypadat</div>
<i>„Graf udává počet mužů a žen v turistickém oddílu v letech 2015–2018. Rozhodněte, která tvrzení jsou pravdivá (A) nebo nepravdivá (N)."</i>
</div>
<div class="ex"><div class="lbl">Krok 1: Přečti obě čáry a zapiš do tabulky tužkou</div>
<table class="htable">
<tr><th style="background:#6C3483;color:white">Rok</th><th style="background:#6C3483;color:white">Muži</th><th style="background:#6C3483;color:white">Ženy</th><th style="background:#6C3483;color:white">Celkem</th></tr>
<tr><td>2015</td><td>{fi('?')}</td><td>{fi('?')}</td><td>{fi('?')}</td></tr>
<tr><td>2016</td><td>{fi('?')}</td><td>{fi('?')}</td><td>{fi('?')}</td></tr>
</table>
Bez tabulky se v hodnotách snadno ztratíš — vždy si je vypiš!
</div>
<div class="ex"><div class="lbl">Krok 2: Ověřuj tvrzení jedno po druhém</div>
<table class="htable">
<tr><th style="background:#6C3483;color:white">Tvrzení</th><th style="background:#6C3483;color:white">Co počítám</th></tr>
<tr><td>„Celkem v roce 2016"</td><td>Muži + Ženy dohromady</td></tr>
<tr><td>„Mužů bylo o třetinu více než v 2015"</td><td>Hodnota 2015 + hodnota 2015 ÷ 3</td></tr>
<tr><td>„Ženy poprvé poklesly v 2018"</td><td>Zkontroluj 2015→2016, 2016→2017 — nesmí klesat!</td></tr>
<tr><td>„Oddíl rostl každý rok"</td><td>Porovnej celkový součet za každý rok</td></tr>
</table>
</div>
<div class="ex"><div class="lbl">⚠️ Pozor: čáry se mohou křížit!</div>
V místě křížení mají obě čáry <b>stejnou hodnotu</b>. Zkontroluj přesné číselné hodnoty — nekříží se tam, kde to jen vypadá.
</div>""", "#f9f0ff", "#9B59B6"),

("⚠️", "Nejčastější chyby při čtení grafů", f"""
<table class="htable">
<tr><th style="background:#C0392B;color:white">Chyba</th><th style="background:#C0392B;color:white">Jak to správně</th></tr>
<tr><td>🔴 Osa začíná od 0 — čtu přímo výšku sloupce</td><td>VŽDY zkontroluj kde osa začíná! Může začínat od 20, 30...</td></tr>
<tr><td>🔴 „R vytřídil o třetinu méně než S" → třetina z R</td><td>Třetina se počítá ze S (ze srovnávané hodnoty!)</td></tr>
<tr><td>🔴 Graf mincí: porovnávám počty mincí</td><td>Přepočítej na koruny: počet mincí × 50 Kč</td></tr>
<tr><td>🔴 „Poprvé kleslo v 2018" — zkontroluji jen 2018</td><td>Musíš zkontrolovat VŠECHNY předchozí roky — ani jeden nesmí klesat!</td></tr>
<tr><td>🔴 U dvou čar: čtu jen jednu a zapomenu na druhou</td><td>Vypiš obě čáry do tabulky — pak ověřuj tvrzení</td></tr>
<tr><td>🔴 Sečtu hodnoty místo porovnání tvrzení</td><td>Nejdřív si vypiš hodnoty do tabulky, pak teprve ověřuj</td></tr>
</table>""", "#fff0f0", "#C0392B"),
]

# ══════════════════════════════════════════════════════════════════
# PL05 — SOUSTAVY PODMÍNEK
# ══════════════════════════════════════════════════════════════════
HINTS_PL05 = [

("📋", "Tabulka = záchrana — VŽDY ji nakresli", f"""
<div class="ex"><div class="lbl">Kdy nakreslit tabulku</div>
Kdykoli je v zadání více skupin nebo více vlastností — nakresli tabulku hned na začátku.
</div>
<div class="ex"><div class="lbl">Jak může zadání vypadat</div>
<i>„Dům má 3 patra a bydlí v něm 11 dětí. Ve 2. patře bydlí jen dívky. V 1.+2. patře dohromady 8 dětí. Ze všech chlapců bydlí mimo 3. patro jen 3."</i>
</div>
<div class="ex"><div class="lbl">Krok 1: Nakresli prázdnou tabulku</div>
<table class="htable">
<tr><th style="background:#1E8449;color:white">Patro</th><th style="background:#1E8449;color:white">Chlapci</th><th style="background:#1E8449;color:white">Dívky</th><th style="background:#1E8449;color:white">Celkem</th></tr>
<tr><td>1.</td><td class="fill">{fi()}</td><td class="fill">{fi()}</td><td class="fill">{fi()}</td></tr>
<tr><td>2.</td><td style="background:#fff3cd;font-weight:700">0 ← jen dívky!</td><td class="fill">{fi()}</td><td class="fill">{fi()}</td></tr>
<tr><td>3.</td><td class="fill">{fi()}</td><td class="fill">{fi()}</td><td class="fill">{fi()}</td></tr>
<tr><td><b>CELKEM</b></td><td class="fill">{fi()}</td><td class="fill">{fi()}</td><td><b>11</b></td></tr>
</table>
</div>
<div class="ex"><div class="lbl">Krok 2: Doplň co znáš přímo ze zadání</div>
<ul>
<li>2. patro: chlapci = <b>0</b> (jen dívky)</li>
<li>1.+2. patro celkem = <b>8</b> → 3. patro = 11−8 = <b>3 děti</b></li>
<li>Chlapci mimo 3. patro = jen 3 → chlapci v 1.+2. = <b>3</b> → chlapci ve 2. = 0 → chlapci v 1. = <b>3</b></li>
</ul>
</div>
<div class="ex"><div class="lbl">Krok 3: Dopočítej zbývající (řádky a sloupce musí sedět)</div>
<table class="htable">
<tr><th style="background:#1E8449;color:white">Patro</th><th style="background:#1E8449;color:white">Chlapci</th><th style="background:#1E8449;color:white">Dívky</th><th style="background:#1E8449;color:white">Celkem</th></tr>
<tr><td>1.</td><td><b>3</b></td><td><b>?</b></td><td><b>?</b></td></tr>
<tr><td>2.</td><td><b>0</b></td><td><b>?</b></td><td><b>?</b></td></tr>
<tr><td>3.</td><td><b>?</b></td><td><b>?</b></td><td><b>3</b></td></tr>
<tr><td>CELKEM</td><td><b>?</b></td><td><b>?</b></td><td><b>11</b></td></tr>
</table>
Doplňuj tak, aby každý řádek i sloupec dal správný součet!
</div>""", "#eafaf1", "#1E8449"),

("🔵", "Vennův diagram — průnik skupin", f"""
{SVG_VENN}
<div class="ex"><div class="lbl">Jak spočítat celkový počet — krok za krokem</div>
<ol>
<li>Sečti všechny kroužky: 14+12+6 = 32 (ale průniky jsou počítány víckrát!)</li>
<li>Odečti děti v právě 2 kroužcích jednou: 32−8 = 24</li>
<li>Odečti děti ve všech 3 kroužcích dvakrát: 24−2×3 = 24−6 = <span class="hint-result">18 dětí</span></li>
</ol>
</div>
<div class="ex"><div class="lbl">Kolik navštěvuje POUZE jeden kroužek</div>
18 celkem − 8 (právě dva kroužky) − 3 (všechny tři) = <span class="hint-result">7 dětí</span>
</div>""", "#eafaf1", "#27AE60"),

("🔺", "Součtový trojúhelník — krok za krokem", f"""
{SVG_SOUCET_T}
{SVG_SOUCET_PRIKLAD}
<div class="ex"><div class="lbl">Jak řešit: obě ? jsou stejná čísla, výsledek = 44</div>
<ol>
<li>Označím hledané číslo jako {fi('A')}</li>
<li>Prostřední řádek: vlevo = {fi('A')}+{fi('A')} = 2{fi('A')}, vpravo = {fi('A')}+8</li>
<li>Dole: 2{fi('A')} + ({fi('A')}+8) = 3{fi('A')}+8 = 44</li>
<li>3{fi('A')} = 36 → {fi('A')} = <span class="hint-result">12</span></li>
<li>Ověř: nahoře 12, 12, 8 → prostřední: 24, 20 → dole: 44 ✓</li>
</ol>
</div>
<div class="ex"><div class="lbl">💡 Bez rovnic — vizuální alternativa</div>
Dole = 44. Číslo 8 je na kraji → odečti: 44 − 8 = 36.<br>
Zbývají 3 stejné části → 36 ÷ 3 = <span class="hint-result">12</span> = A ✓
</div>""", "#eafaf1", "#1E8449"),

("🔢", "Zlomky celku — krok za krokem", f"""
<div class="ex"><div class="lbl">Příklad: třetina žlutých, 12 červených, zbytek modrý. Modrých = 18.</div>
<ol>
<li>Červené + modré = 12+18 = 30</li>
<li>Žluté jsou třetina → červené+modré jsou <b>dvě třetiny</b> ze všech</li>
<li>Dvě třetiny = 30 → jedna třetina = 15 → celkem = <span class="hint-result">45 kuliček</span></li>
</ol>
</div>
<div class="ex"><div class="lbl">Obecný vzorec: část = X z Y dílů celku</div>
Celkem = část ÷ X × Y<br>
Příklad: ⅔ = 30 → celkem = 30 ÷ 2 × 3 = 45 ✓
</div>
<div class="ex"><div class="lbl">Příklad: Ondra, Pavel a Šárka mají dohromady 750 Kč. Ondra má 2× tolik co Šárka. Pavel má také 2× tolik co Šárka. Kolik má Šárka?</div>
Označím Šárku jako {fi('?')}. Ondra = 2×{fi('?')}, Pavel = 2×{fi('?')}.<br>
{fi('?')} + 2×{fi('?')} + 2×{fi('?')} = 5×{fi('?')} = 750 Kč<br>
{fi('?')} = 750 ÷ 5 = <span class="hint-result">150 Kč</span>. Ondra = Pavel = 300 Kč. Ověř: 150+300+300 = 750 ✓
</div>""", "#eafaf1", "#27AE60"),

("💡", "Dosaď jednu podmínku do druhé", f"""
<div class="ex"><div class="lbl">Příklad (Jana a sešity, 23r1)</div>
2 linkované + 2 čtverečkované = 180 Kč. 2 čtverečkované stojí jako 3 linkované.
<ol>
<li>Z 2. podmínky: 2 čtverečkované = 3 linkované</li>
<li>Dosadím do 1.: 2 linkované + 3 linkované = 5 linkovaných = 180 Kč</li>
<li>1 linkovaný = <span class="hint-result">36 Kč</span></li>
<li>1 čtverečkovaný = 3×36÷2 = <span class="hint-result">54 Kč</span></li>
</ol>
</div>
<div class="ex"><div class="lbl">Příklad: dvě čísla, součet = 150, druhé = polovina prvního</div>
<ol>
<li>Druhé = první÷2</li>
<li>první + první÷2 = tři poloviny prvního čísla = 150</li>
<li>Tři poloviny = 150 → jedna polovina = 50 → celé první číslo = <span class="hint-result">100</span>. Druhé = 50. Ověř: 100+50 = 150 ✓</li>
</ol>
</div>""", "#eafaf1", "#1E8449"),

("⚠️", "Nejčastější chyby u soustav podmínek", f"""
<table class="htable">
<tr><th style="background:#C0392B;color:white">Chyba</th><th style="background:#C0392B;color:white">Jak to správně</th></tr>
<tr><td>🔴 Nenakresli tabulku → ztratím se v podmínkách</td><td>Tabulka je povinná! Bez ní nemůžeš správně řešit</td></tr>
<tr><td>🔴 Venn: sečtu všechny kroužky = celkový počet</td><td>Průniky jsou počítány víckrát — musíš je odečíst!</td></tr>
<tr><td>🔴 Součtový trojúhelník: dole = součet horní řady</td><td>Dole = součet PROSTŘEDNÍ řady (ne horní!)</td></tr>
<tr><td>🔴 „Čtvrtina je 12" → celkem = 12 × 4 ✓ (toto je správně!)</td><td>Ale: „dvě třetiny jsou 30" → celkem = 30 ÷ 2 × 3 = 45 (ne 30÷2!)</td></tr>
<tr><td>🔴 Neověřím výsledek v KAŽDÉ podmínce</td><td>Zkontroluj každou podmínku zvlášť — soudné řešení splňuje všechny</td></tr>
</table>""", "#fff0f0", "#C0392B"),
]

# ══════════════════════════════════════════════════════════════════
# PL06 — OBVOD A OBSAH
# ══════════════════════════════════════════════════════════════════
HINTS_PL06 = [

("📏", "Obvod vs. obsah — základní rozdíl", f"""
<table class="htable">
<tr><th style="background:#515A5A;color:white">Obvod</th><th style="background:#515A5A;color:white">Obsah</th></tr>
<tr><td>= Cesta kolem <b>dokola</b></td><td>= Plocha <b>uvnitř</b></td></tr>
<tr><td>Jednotky: cm, m, mm</td><td>Jednotky: cm², m²</td></tr>
<tr><td>Jdi prstem PO OKRAJI</td><td>Počítej čtverečky UVNITŘ</td></tr>
</table>
<table class="htable" style="margin-top:10px">
<tr><th style="background:#515A5A;color:white">Tvar</th><th style="background:#515A5A;color:white">Obvod</th><th style="background:#515A5A;color:white">Obsah</th></tr>
<tr><td><b>Čtverec</b> (strana a)</td><td>4 × a</td><td>a × a</td></tr>
<tr><td><b>Obdélník</b> (strany a, b)</td><td>2 × (a + b)</td><td>a × b</td></tr>
<tr><td><b>Trojúhelník</b></td><td>a + b + c</td><td>základna × výška ÷ 2</td></tr>
</table>""", "#f5f5f5", "#515A5A"),

("🔲", "Složené tvary — dvě metody s příkladem", f"""
<div class="ex"><div class="lbl">Jak může zadání vypadat</div>
<i>„Vypočtěte obsah a obvod tvaru v čtvercové síti, kde 1 čtverec = 1 cm²."</i>
</div>
{diag('''<svg viewBox="0 0 380 200" xmlns="http://www.w3.org/2000/svg" style="max-width:380px">
  <defs><style>
    .sq{{fill:#D5EAF7;stroke:#2980B9;stroke-width:1.5}}
    .missing{{fill:#f5f5f5;stroke:#ccc;stroke-width:1;stroke-dasharray:4,3}}
    .dim{{font-size:12px;fill:#555;font-family:sans-serif;text-anchor:middle}}
    .cut{{fill:#FDEDEC;stroke:#E74C3C;stroke-width:1.5;stroke-dasharray:4,3}}
  </style></defs>
  <!-- Full 8×5 L-shape (unit=20px): columns 0-7, rows 0-4 -->
  <!-- Left half: all 5 rows, columns 0-3 (4 cols wide) -->
  <!-- Right half: only rows 2-4 (bottom 3 rows), columns 4-7 (but H said 4×2 so cols 4-7, rows 3-4) -->
  <!-- Actually: L = 8 wide, 5 tall, missing top-right 4×3 -->
  <!-- Left block 4×5 -->
  <rect x="20" y="20" width="80" height="100" class="sq"/>
  <!-- Right-bottom block 4×2 -->
  <rect x="100" y="80" width="80" height="40" class="sq"/>
  <!-- Missing top-right 4×3 (dashed) -->
  <rect x="100" y="20" width="80" height="60" class="missing"/>
  <!-- Cut line (division) -->
  <line x1="100" y1="20" x2="100" y2="120" stroke="#E74C3C" stroke-width="2" stroke-dasharray="6,4"/>
  <!-- Dimension labels -->
  <text x="60" y="15" class="dim" fill="#2980B9" font-weight="bold">4 cm</text>
  <text x="140" y="15" class="dim" fill="#C0392B">4 cm (chybí)</text>
  <text x="14" y="72" class="dim" font-size="11" fill="#2980B9" transform="rotate(-90,14,72)">5 cm</text>
  <text x="188" y="104" class="dim" font-size="11" fill="#2980B9" transform="rotate(-90,188,104)">2 cm</text>
  <text x="60" y="138" class="dim" fill="#27AE60" font-weight="bold">4 × 5 = 20</text>
  <text x="140" y="108" class="dim" fill="#27AE60" font-weight="bold">4 × 2 = 8</text>
  <text x="140" y="53" class="dim" fill="#C0392B">odebráno: 4×3=12</text>

  <!-- Method labels -->
  <text x="60" y="160" class="dim" fill="#27AE60" font-weight="bold">Metoda 1: 20+8 = 28 cm²</text>
  <text x="60" y="178" class="dim" fill="#2980B9">Metoda 2: 8×5−4×3 = 40−12 = 28 cm²</text>
</svg>''', "L-tvar: 8 cm wide, 5 cm tall, chybějící roh 4×3 — obě metody dají 28 cm²")}
<div class="ex"><div class="lbl">Metoda 1: ROZDĚLIT červenou čarou</div>
<ol>
<li>Svislá červená čára rozdělí tvar na dvě části</li>
<li>Levý obdélník: 4 × 5 = <b>20 cm²</b></li>
<li>Pravý obdélník: 4 × 2 = <b>8 cm²</b></li>
<li>Obsah celkem: 20 + 8 = <span class="hint-result">28 cm²</span></li>
</ol>
</div>
<div class="ex"><div class="lbl">Metoda 2: RÁMEČEK (8×5) minus chybějící roh (4×3)</div>
<ol>
<li>Celý obdélník: 8 × 5 = <b>40 cm²</b></li>
<li>Chybějící roh (přerušovaně): 4 × 3 = <b>12 cm²</b></li>
<li>Obsah: 40 − 12 = <span class="hint-result">28 cm²</span> ✓</li>
</ol>
</div>
<div class="ex"><div class="lbl">⚠️ Obvod — nejčastější chyba</div>
Jdi prstem <b>PO VNĚJŠÍM OKRAJI</b> — jen oranžové strany se počítají do obvodu!<br>
Červená dělicí čára se <b>NEPOČÍTÁ</b> — je to jen pomyslná čára pro výpočet, ne skutečná strana tvaru.
</div>""", "#f5f5f5", "#7F8C8D"),

("♟️", "Osová souměrnost — jak poznat a opravit", f"""
{SVG_OSOVA}
<div class="ex"><div class="lbl">Jak najít čtverec k odebrání</div>
<ol>
<li>Pro každý čtverec v tvaru najdi jeho <b>zrcadlový protějšek</b> přes osu</li>
<li>Který čtverec <b>nemá žádný protějšek</b> přes žádnou osu → ten je navíc</li>
<li>Odebereme ho → tvar bude symetrický</li>
<li>Hledej pro svislou, vodorovnou i šikmou osu (45°)</li>
</ol>
</div>""", "#f5f5f5", "#515A5A"),

("🔷", "Ve čtvercové síti — počítej chytře", f"""
<div class="ex"><div class="lbl">Obsah trojúhelníku v síti</div>
<ol>
<li>Nakresli obdélník kolem trojúhelníku</li>
<li>Obsah trojúhelníku = obsah obdélníku ÷ 2</li>
</ol>
</div>
<div class="ex"><div class="lbl">Jakou část sítě zabírá šedý tvar</div>
<ol>
<li>Spočítej čtverečky šedého tvaru (i půlky!)</li>
<li>Spočítej celkový počet čtverečků sítě</li>
<li>Šedý ÷ celkový = zlomek → zjednoduš ho</li>
</ol>
Příklad: šedý = 12, celkem = 24 → 12÷24 = <span class="hint-result">½ = polovina</span>
</div>
<div class="ex"><div class="lbl">Obdélník s obvodem 18 cm — systematicky všechny možnosti</div>
<table class="htable" style="max-width:260px">
<tr><th style="background:#515A5A;color:white">Strany a, b</th><th style="background:#515A5A;color:white">Obsah a×b</th></tr>
<tr><td>1 cm, 8 cm</td><td>8 cm²</td></tr>
<tr><td>2 cm, 7 cm</td><td>14 cm²</td></tr>
<tr><td>3 cm, 6 cm</td><td>18 cm²</td></tr>
<tr style="background:#d5f5e3"><td><b>4 cm, 5 cm</b></td><td><b>20 cm² ← největší!</b></td></tr>
</table>
</div>""", "#f5f5f5", "#7F8C8D"),

("📐", "Pevný obvod → největší obsah a záhon", f"""
<div class="ex"><div class="lbl">Zlaté pravidlo</div>
Ze všech obdélníků se stejným obvodem má <b>největší obsah ten, jehož strany jsou si nejbližší</b>. Čtverec by byl úplně nejlepší.
</div>
<div class="ex"><div class="lbl">Rovnostranný trojúhelník: záhon se 39 rostlinami na obvodu</div>
<ol>
<li>Obvod = 39, tři stejně dlouhé strany</li>
<li>39 ÷ 3 = 13 mezer na každé straně</li>
<li>Na každé straně = 13 mezer + 1 rohová rostlina = <span class="hint-result">14 rostlin</span></li>
</ol>
Proč +1? Na každé straně je 13 <em>mezer mezi rostlinami</em> = 14 rostlin (13 mezer + 2 rohové?). Ne! Každý ze 3 rohů patří dvěma stranám → nezapočítáme ho dvakrát:<br>
<b>Počet rostlin na straně = počet mezer + 1 rohová</b> = 13+1 = 14.<br>
Celkem: 3 strany × 14 − 3 rohové (které jsme počítali 2×) = 42−3 = <span class="hint-result">39 rostlin ✓</span>
</div>""", "#f5f5f5", "#515A5A"),

("📐", "Obvod v čtvercové síti — pozor na šikmé strany!", f"""
<div class="ex"><div class="lbl">Jak může zadání vypadat (25r1, 22r1, 24n1)</div>
<i>„Ve čtvercové síti jsou trojúhelník ABC a čtverec DEFG. O kolik cm se liší jejich obvody?"</i>
</div>
<div class="ex"><div class="lbl">Pravidlo 1: Vodorovná a svislá strana — jednoduchá</div>
Strana jde přímo po mřížce → délka = počet čtverečků × 1 cm<br>
Příklad: strana přes 3 čtverečky = <span class="hint-result">3 cm</span>
</div>
<div class="ex"><div class="lbl">Pravidlo 2: Šikmá strana — je DELŠÍ než vypadá!</div>
Šikmá strana přes 1 čtvereček diagonálně ≈ <b>1,4 cm</b> (ne 1 cm!)<br>
Šikmá strana přes 3 vpravo a 4 dolů ≈ <b>5 cm</b> (Pythagorova trojice 3-4-5)<br>
<table class="htable" style="margin-top:6px">
<tr><th style="background:#515A5A;color:white">Posun (vpravo × dolů)</th><th style="background:#515A5A;color:white">Délka strany</th><th style="background:#515A5A;color:white">Jak poznám</th></tr>
<tr><td>1 × 1</td><td>≈ 1,4 cm</td><td>diagonála jednoho čtverečku</td></tr>
<tr><td>2 × 2</td><td>≈ 2,8 cm</td><td>diagonála 2×2 bloku</td></tr>
<tr><td>3 × 4 nebo 4 × 3</td><td>= 5 cm</td><td>Pythagorova trojice!</td></tr>
<tr><td>1 × 2 nebo 2 × 1</td><td>≈ 2,2 cm</td><td>kratší než 3 cm, delší než 2 cm</td></tr>
</table>
</div>
<div class="ex"><div class="lbl">Postup: porovnání dvou obvodů</div>
<ol>
<li>Spočítej obvod 1. tvaru — rozlišuj přímé a šikmé strany</li>
<li>Spočítej obvod 2. tvaru stejně</li>
<li>Odečti: větší − menší = rozdíl</li>
</ol>
Šikmé strany vždy <b>prodlužují</b> obvod — tvar s šikmými stranami bude mít větší obvod než tvar se stejnými přímými stranami!
</div>""", "#f5f5f5", "#515A5A"),

("⚠️", "Nejčastější chyby při výpočtu obvodu a obsahu", f"""
<table class="htable">
<tr><th style="background:#C0392B;color:white">Chyba</th><th style="background:#C0392B;color:white">Jak to správně</th></tr>
<tr><td>🔴 Zahrnu vnitřní dělicí čáru do obvodu</td><td>Do obvodu patří jen VNĚJŠÍ okraj — vnitřní čáry se NEpočítají!</td></tr>
<tr><td>🔴 Pletám obvod (cm) a obsah (cm²)</td><td>Obvod = délka cesty okolo, obsah = plocha uvnitř. Jiné jednotky!</td></tr>
<tr><td>🔴 Šikmá strana v síti = 1 cm (jako přímá)</td><td>Šikmá strana je VŽDY delší! Diagonála 1×1 ≈ 1,4 cm, trojice 3-4-5 = 5 cm</td></tr>
<tr><td>🔴 U záhonu: rohové rostliny počítám dvakrát</td><td>Rohová rostlina patří oběma stranám — každý roh počítám jen jednou</td></tr>
<tr><td>🔴 U trojúhelníku v síti: beru špatnou výšku</td><td>Výška musí být KOLMÁ na základnu — ne šikmá strana</td></tr>
<tr><td>🔴 1 m² = 100 cm²</td><td>1 m² = 10 000 cm² (protože 100 cm × 100 cm = 10 000 cm²!)</td></tr>
</table>""", "#fff0f0", "#C0392B"),
]

# ══════════════════════════════════════════════════════════════════
# PL07 — VÝRAZY A ZÁVORKY
# ══════════════════════════════════════════════════════════════════
HINTS_PL07 = [

("🔢", "Pořadí operací — ZÁKON nade vše", f"""
<div class="ex"><div class="lbl">Pevné pořadí — vždy stejné</div>
<ol>
<li><b>Závorky</b> — vždy jako první, zevnitř ven</li>
<li><b>Násobení a dělení</b> — zleva doprava</li>
<li><b>Sčítání a odčítání</b> — zleva doprava</li>
</ol>
</div>
<div class="ex"><div class="lbl">Jednoduchý příklad pro začátek</div>
Výraz: <b>(3 + 5) × 2 − 4</b><br>
1. Závorka: (3+5) = <b>8</b><br>
2. Násobení: 8×2 = <b>16</b><br>
3. Odčítání: 16−4 = <span class="hint-result">12</span>
</div>
<div class="ex"><div class="lbl">Náročnější příklad: 5 × 120 + (700 − 6 × 25) ÷ (10 − 7 + 2)</div>
Závorky: (700 − 6×25) = 700−150 = <b>550</b> &nbsp;&nbsp; (10−7+2) = <b>5</b><br>
Násobení/dělení: 5×120 = <b>600</b> &nbsp;&nbsp; 550÷5 = <b>110</b><br>
Sčítání: 600 + 110 = <span class="hint-result">710</span>
</div>
<div class="ex"><div class="lbl">Příklad: (5 + 5 × 29) − 4 × (176 ÷ 8 − 8 × 2)</div>
Závorky: 5+5×29 = 5+145 = 150 &nbsp;&nbsp; 176÷8=22, 8×2=16, 22−16=6 → 4×6=24<br>
Výsledek: 150 − 24 = <span class="hint-result">126</span>
</div>""", "#E8F8F5", "#148F77"),

("🔄", "Závorky mění vše — jak je vyzkoušet", f"""
<div class="ex"><div class="lbl">Závorka mění pořadí — co je uvnitř se počítá DŘÍV</div>
Výraz: 9 × 8 − 6 ÷ 2 = 72−3 = <b>69</b> (bez závorek)
<table class="htable" style="margin-top:8px">
<tr><th style="background:#148F77;color:white">Se závorkou</th><th style="background:#148F77;color:white">Výpočet</th><th style="background:#148F77;color:white">Výsledek</th></tr>
<tr><td>(9 × 8 − 6) ÷ 2</td><td>66 ÷ 2</td><td><b>33</b></td></tr>
<tr><td>9 × (8 − 6) ÷ 2</td><td>9 × 2 ÷ 2</td><td><b>9</b></td></tr>
<tr><td>9 × (8 − 6 ÷ 2)</td><td>9 × 5</td><td><b>45</b></td></tr>
</table>
</div>
<div class="ex"><div class="lbl">Jak vyzkoušet VŠECHNA místa pro závorku</div>
U 4 čísel: závorka může začínat u 1., 2. nebo 3. čísla.<br>
Závorka kolem celého výrazu = stejný výsledek jako bez závorky → nevede k novému výsledku!
</div>""", "#E8F8F5", "#17A589"),

("□", "Neznámé číslo — jdi pozpátku", f"""
<div class="ex"><div class="lbl">Tabulka: jak otočit každou operaci</div>
<table class="htable">
<tr><th style="background:#148F77;color:white">Operace dopředu</th><th style="background:#148F77;color:white">Pozpátku (otoč!)</th></tr>
<tr><td>+ 5 (přičtu 5)</td><td>− 5 (odečtu 5)</td></tr>
<tr><td>− 6 (odečtu 6)</td><td>+ 6 (přičtu 6)</td></tr>
<tr><td>× 3 (vynásobím 3)</td><td>÷ 3 (vydělím 3)</td></tr>
<tr><td>÷ 4 (vydělím 4)</td><td>× 4 (vynásobím 4)</td></tr>
</table>
</div>
<div class="ex"><div class="lbl">Příklad: vydělím 7, přičtu 3, zdvojnásobím → dostanu 20</div>
{calc_row('20', '÷2', '10', '−3', '7', '×7', '49')}<br>
Ověř: 49÷7=7, +3=10, ×2=<span class="hint-result">20 ✓</span>
</div>
<div class="ex"><div class="lbl">Příklad: (188−152)÷(1+{fi('?')}) = 4+20÷4</div>
Pravá strana: 4+5=9. Levá: 36÷(1+{fi('?')})=9 → 1+{fi('?')}=4 → {fi('?')}=<span class="hint-result">3</span>
</div>
<div class="ex"><div class="lbl">🆕 Typ: „zvětšené o svou polovinu" — krok za krokem</div>
Zadání: <i>„Číslo zvětšené o svou polovinu se rovná 198."</i><br>
Co to znamená: číslo + (číslo ÷ 2) = 198<br>
Dvě poloviny + jedna polovina = <b>tři poloviny</b> celkem = 198<br>
→ Jedna polovina = 198 ÷ 3 = <b>66</b><br>
→ Celé číslo = 66 × 2 = <span class="hint-result">132</span><br>
Ověř: 132 + 66 = 198 ✓
<div style="margin-top:8px;padding:8px;background:#ffebee;border-radius:6px;font-size:13px">
⛔ Záměna! „198 ÷ 2 = 99" je číslo <b>zmenšené</b> na polovinu — to je úplně jiná úloha!
</div>
</div>""", "#E8F8F5", "#148F77"),

("🧮", "Magická tabulka — jak vyplnit krok za krokem", f"""
{SVG_MAGICKA}
<div class="ex"><div class="lbl">Jak může zadání vypadat</div>
<i>„Doplňte do prázdných políček čísla 0–8 (každé právě jednou) tak, aby součet každého řádku i každého sloupce byl stejný."</i><br>
V obrázku výše jsou <b>zadána</b> čísla 1, 5, 3, 7 — zbývá doplnit 5 chybějících čísel (včetně středu!)
</div>
<div class="ex"><div class="lbl">Krok 1: Zjisti, kolik musí dávat každý řádek</div>
Sečti všechna čísla: 0+1+2+3+4+5+6+7+8 = <b>36</b><br>
Tabulka má 3 řádky → každý řádek musí dát: 36 ÷ 3 = <span class="hint-result">12</span>
</div>
<div class="ex"><div class="lbl">Krok 2: Střed tabulky — proč je to vždy 4?</div>
Seřaď čísla od nejmenšího po největší: 0, 1, 2, 3, <b>4</b>, 5, 6, 7, 8<br>
Číslo uprostřed tohoto seznamu (5. z 9) je <b>4</b>.<br>
A prostřední políčko tabulky musí být právě toto střední číslo — jinak by řádky a sloupce nevyšly.<br>
→ <b>Jednoduché pravidlo:</b> střed = prostřední číslo ze sady (vždy!)
</div>
<div class="ex"><div class="lbl">Krok 3: Doplňuj řádek po řádku — „12 minus ostatní"</div>
Máš-li v řádku 2 čísla, třetí = 12 − součet těch dvou.<br>
Řádek 1 má 1 a 5 → třetí = 12 − 1 − 5 = <span class="hint-result">6</span> ✓<br>
Řádek 3 má 3 a 7 → třetí = 12 − 3 − 7 = <span class="hint-result">2</span> ✓<br>
Řádek 2 má 4 a ... zbytek = 0 a 8 → 12 − 4 − 0 = 8 nebo 12 − 4 − 8 = 0.<br>
Vyber tak, aby sloupce také vycházely!
</div>
<div class="ex"><div class="lbl">💡 Trik: vypiš všechny dvojice co dají 12 z čísel 0–8</div>
Dvojice (a+b=12): 4+8, 5+7, 3+9✗(9 není v sadě)... Platné: (4,8), (5,7).<br>
Trojice (a+b+c=12): 0+5+7, 1+4+7, 2+3+7, 1+3+8, 0+4+8, 2+4+6, 1+5+6, 3+4+5 — zkus každou!
</div>
<div class="ex"><div class="lbl">Krok 4: Ověř všechny sloupce a úhlopříčky</div>
Správné řešení pro zadaná čísla 1, 5, 4, 3, 7:
<table class="htable" style="max-width:300px;text-align:center">
<tr><th style="background:#1A5276;color:white">řádek 1</th><td><b>1</b></td><td><b>6</b></td><td><b>5</b></td><td style="color:#27AE60;font-weight:700">=12 ✓</td></tr>
<tr><th style="background:#1A5276;color:white">řádek 2</th><td><b>8</b></td><td><b>4</b></td><td><b>0</b></td><td style="color:#27AE60;font-weight:700">=12 ✓</td></tr>
<tr><th style="background:#1A5276;color:white">řádek 3</th><td><b>3</b></td><td><b>2</b></td><td><b>7</b></td><td style="color:#27AE60;font-weight:700">=12 ✓</td></tr>
<tr><td></td><td style="color:#27AE60;font-weight:700">=12✓</td><td style="color:#27AE60;font-weight:700">=12✓</td><td style="color:#27AE60;font-weight:700">=12✓</td><td></td></tr>
</table>
Úhlopříčky: 1+4+7 = <b>12 ✓</b> &nbsp;&nbsp; 5+4+3 = <b>12 ✓</b>
</div>""", "#E8F8F5", "#17A589"),

("➡️", "Diagram šipek — jdi vždy pozpátku", f"""
{SVG_SIPKY}
<div class="ex"><div class="lbl">Co diagram říká</div>
Neznámé číslo <b>x</b> prochází třemi operacemi a výsledek je <b>25</b>.<br>
Operace v pořadí: nejprve ÷2, pak +3, nakonec ×5.
</div>
<div class="ex"><div class="lbl">Jak najít x — jdi POZPÁTKU od výsledku</div>
Každou operaci obrátíš na opak (÷ ↔ ×, + ↔ −) a jdeš zprava doleva:<br>
{calc_row('25', '÷5', '5', '−3', '2', '×2', 'x = 4')}
</div>
<div class="ex"><div class="lbl">Ověření dopředu (vždy zkontroluj!)</div>
4 ÷ 2 = <b>2</b> &nbsp;→&nbsp; 2 + 3 = <b>5</b> &nbsp;→&nbsp; 5 × 5 = <span class="hint-result">25 ✓</span>
</div>
<div class="ex"><div class="lbl">Tabulka: jak otočit operace</div>
<table class="htable">
<tr><th style="background:#148F77;color:white">Operace v diagramu</th><th style="background:#148F77;color:white">Otočím na (pozpátku)</th></tr>
<tr><td>× 5 (vynásobím 5)</td><td>÷ 5 (vydělím 5)</td></tr>
<tr><td>+ 3 (přičtu 3)</td><td>− 3 (odečtu 3)</td></tr>
<tr><td>÷ 2 (vydělím 2)</td><td>× 2 (vynásobím 2)</td></tr>
</table>
Pravidlo: <b>×↔÷</b> a <b>+↔−</b>. Nic jiného se nestane!
</div>""", "#E8F8F5", "#148F77"),

("⚠️", "Nejčastější chyby u výrazů a závorek", f"""
<table class="htable">
<tr><th style="background:#C0392B;color:white">Chyba</th><th style="background:#C0392B;color:white">Jak to správně</th></tr>
<tr><td>🔴 Počítám zleva doprava bez ohledu na pravidla</td><td>Pořadí: 1. závorky, 2. násobení/dělení, 3. sčítání/odčítání</td></tr>
<tr><td>🔴 Záporný výsledek v diagramu = chyba</td><td>−5 je platný výsledek! Pokračuj dál: −5+7=2 ✓</td></tr>
<tr><td>🔴 Magická tabulka: začnu doplňovat bez výpočtu cíle</td><td>Nejdřív: 0+1+...+8=36, 36÷3=12 — každý řádek musí dát 12</td></tr>
<tr><td>🔴 Při pozpátku: otoč operaci ale jdi stále dopředu</td><td>Otoč operaci A JDI ZPRAVA DOLEVA: od výsledku k začátku</td></tr>
<tr><td>🔴 Závorka kolem celého výrazu = nový výsledek</td><td>Závorka kolem VŠEHO výsledek nezmění — nepočítej ji!</td></tr>
<tr><td>🔴 „Zvětšené o polovinu" → dělím 198 ÷ 2 = 99</td><td>Zvětšené o polovinu = číslo + polovina = tři poloviny. 198 ÷ 3 = 66, číslo = 66×2 = <b>132</b>!</td></tr>
</table>""", "#fff0f0", "#C0392B"),
]

# ══════════════════════════════════════════════════════════════════
# PL08 — JEDNOTKY A PŘEVODY
# ══════════════════════════════════════════════════════════════════
HINTS_PL08 = [

("📏", "Žebřík délkových jednotek — nahoře VELKÉ, dole MALÉ", f"""
{SVG_ZEBRIK}
<table class="htable">
<tr><th style="background:#784212;color:white">Z</th><th style="background:#784212;color:white">Na</th><th style="background:#784212;color:white">Násobíš</th><th style="background:#784212;color:white">Příklad</th></tr>
<tr><td>m</td><td>cm</td><td>× 100</td><td>3 m = 300 cm</td></tr>
<tr><td>m</td><td>mm</td><td>× 1000</td><td>2,5 m = 2 500 mm</td></tr>
<tr><td>cm</td><td>mm</td><td>× 10</td><td>52 cm = 520 mm</td></tr>
<tr><td>km</td><td>m</td><td>× 1000</td><td>7 km = 7 000 m</td></tr>
</table>
<div class="ex"><div class="lbl">Smíchané — vždy přepočítej na jednu jednotku</div>
2 m 4 cm 2 mm → v mm: {calc_row('2×1000', '=2000', '+', '4×10=40', '+', '2', '= 2 042 mm')}
</div>""", "#fdf5ec", "#784212"),

("⚖️⏱️", "Hmotnost a čas — zlomky jsou zrádné!", f"""
<div class="ex"><div class="lbl">Zlaté pravidlo: čas nebo hmotnost ÷ jmenovatel zlomku</div>
1/4 hodiny = 60 ÷ 4 = <span class="hint-result">15 min</span> (NE 25 — to by bylo 1/4 ze 100!)<br>
1/3 hodiny = 60 ÷ 3 = <span class="hint-result">20 min</span> (NE 30!)
</div>
<table class="htable">
<tr><th style="background:#784212;color:white">Zlomek</th>
<th style="background:#784212;color:white">Z 1 kg (1000 g)</th>
<th style="background:#784212;color:white">Z 1 hodiny (60 min)</th></tr>
<tr><td><b>1/2</b></td><td>500 g</td><td>30 min</td></tr>
<tr><td><b>1/3</b></td><td>333⅓ g</td><td><b>20 min</b></td></tr>
<tr><td><b>1/4</b></td><td>250 g</td><td><b>15 min</b></td></tr>
<tr><td><b>1/5</b></td><td>200 g</td><td>12 min</td></tr>
<tr><td><b>1/6</b></td><td>167 g</td><td><b>10 min</b></td></tr>
</table>""", "#fdf5ec", "#A56A2A"),

("🚂", "Rovnoměrné tempo — jak na příklady krok za krokem", f"""
<div class="ex"><div class="lbl">Jak může zadání vypadat</div>
<i>„Vlak jede stále stejnou rychlostí. Za 8 minut ujede 7 km. Za jak dlouho ujede 35 km?"</i>
</div>
<div class="ex"><div class="lbl">Zlaté pravidlo — poměr se nemění</div>
Stále stejná rychlost: <b>2× více km = 2× více minut</b>. Vždy!<br>
Nikdy nezměníš rychlost — proto vždy platí: čas ÷ km = stejné číslo.
</div>
<div class="ex"><div class="lbl">Metoda 1: Kolikrát víc km → kolikrát víc minut</div>
{calc_row('35 km', '÷ 7 km', '5× víc', '× 8 min', '40 minut')}
</div>
<div class="ex"><div class="lbl">Metoda 2: Přes 1 km <span style="color:#E74C3C">(⚠️ jen když vychází celé číslo!)</span></div>
Za 1 km = 8 ÷ 7 min → vychází desetinné číslo → <b>pro tuto úlohu použij Metodu 1!</b><br>
Za 35 km = 35 × (8÷7) = 35×8÷7 = 280÷7 = <span class="hint-result">40 minut</span>
</div>
<div class="ex"><div class="lbl">Záludnější příklad: cesta tam a zpět</div>
<i>„Katka jede do školy 2× déle než ze školy. Celá cesta trvá 33 minut."</i><br>
Označím cestu ze školy jako {fi('?')}. Do školy = 2×{fi('?')}.<br>
Celkem: {fi('?')} + 2×{fi('?')} = 3×{fi('?')} = 33<br>
{fi('?')} = 33 ÷ 3 = <span class="hint-result">11 minut ze školy</span>, do školy = 22 minut.
</div>
<div class="ex"><div class="lbl">Tip: jak zkontrolovat</div>
11 + 22 = 33 ✓ &nbsp;&nbsp; A 22 = 2×11 ✓ &nbsp;&nbsp; Obě podmínky splněny!
</div>""", "#fdf5ec", "#784212"),

("🔧", "Smíchané jednotky — 4 kroky", f"""
<ol>
<li><b>Vypiš</b> všechny jednotky ze zadání</li>
<li><b>Zvol</b> jednu — obvykle tu nejmenší v zadání</li>
<li><b>Převeď</b> na ni KAŽDÉ číslo ze zadání — žádné nevynechej!</li>
<li><b>Počítej</b> a výsledek převeď zpět pokud je potřeba</li>
</ol>
<div class="ex"><div class="lbl">Příklad: 18 m − 15 dm + {fi('?')} cm = 20 m</div>
Na cm: 18 m = <b>1800 cm</b>. 15 dm = <b>150 cm</b>. 20 m = <b>2000 cm</b>.<br>
1800 − 150 + {fi('?')} = 2000 → {fi('?')} = 2000−1650 = <span class="hint-result">350 cm</span>
</div>
<div class="ex"><div class="lbl">Příklad: 4 × {fi('?')} g − 3 kg = 1/5 kg</div>
Na gramy: 3 kg = 3000 g. 1/5 kg = 200 g.<br>
4×{fi('?')} = 3000+200 = 3200 → {fi('?')} = <span class="hint-result">800 g</span>
</div>""", "#fdf5ec", "#A56A2A"),

("⚠️", "Zákeřné pasti — přečti si před každým příkladem!", f"""
<table class="htable">
<tr><th style="background:#784212;color:white">Past</th><th style="background:#784212;color:white">Špatně ✗</th><th style="background:#784212;color:white">Správně ✓</th></tr>
<tr><td>1 m² = ? cm²</td><td>100 cm²</td><td><b>10 000 cm²</b> (100×100!)</td></tr>
<tr><td>7:43 + 22 minut</td><td>7:65</td><td><b>8:05</b> (43+22=65 min = 1 hod 5 min)</td></tr>
<tr><td>2 m 4 cm → mm</td><td>204 mm</td><td><b>2 040 mm</b> (2000+40)</td></tr>
<tr><td>1/4 hodiny = ?</td><td>25 min</td><td><b>15 min</b> (60÷4)</td></tr>
<tr><td>cesta 2× déle, celkem 33 min</td><td>33÷2</td><td>33÷3 = <b>11 min</b></td></tr>
</table>""", "#fdf5ec", "#784212"),

("⚠️", "Nejčastější chyby při převodech jednotek", f"""
<table class="htable">
<tr><th style="background:#C0392B;color:white">Chyba</th><th style="background:#C0392B;color:white">Jak to správně</th></tr>
<tr><td>🔴 1/4 hodiny = 25 minut</td><td>1/4 hodiny = 60÷4 = <b>15 minut</b> (ne čtvrtina ze 100!)</td></tr>
<tr><td>🔴 2 m 4 cm = 24 cm nebo 204 mm</td><td>2 m 4 cm = 200+4 = 204 cm = 2 040 mm (ne 204 mm!)</td></tr>
<tr><td>🔴 1 m² = 100 cm²</td><td>1 m² = <b>10 000 cm²</b> (100×100 = 10 000)</td></tr>
<tr><td>🔴 Cesta 2× déle, celkem 33 min → 33÷2</td><td>Ze školy = □, do školy = 2□, dohromady = 3□ = 33 → □ = 11 min</td></tr>
<tr><td>🔴 Smíchané jednotky: přepočítám jen jedno číslo</td><td>Přepočítej KAŽDÉ číslo v zadání — žádné nevynechej!</td></tr>
</table>""", "#fff0f0", "#C0392B"),
]

# ══════════════════════════════════════════════════════════════════
# PL09 — POMĚRY A ZLOMKY
# ══════════════════════════════════════════════════════════════════
HINTS_PL09 = [

("⚖️", "Co je poměr — základ", f"""
<div class="ex"><div class="lbl">Co poměr říká</div>
Poměr 3:5 čteme „3 ku 5" — říká, že první je 3 díly a druhý 5 dílů.<br>
Nezáleží na celkovém počtu — poměr popisuje <b>vztah</b> dvou čísel.
</div>
<div class="ex"><div class="lbl">Jak zjednodušit poměr</div>
Obě čísla vydělíme stejným číslem (největším společným dělitelem):<br>
{calc_row('6:4', '÷ 2', '3:2')} &nbsp;&nbsp; {calc_row('15:25', '÷ 5', '3:5')} &nbsp;&nbsp; {calc_row('12:8', '÷ 4', '3:2')}
</div>
<div class="ex"><div class="lbl">Poměr a zlomek — totéž!</div>
Poměr 3:5 = zlomek 3/5 = „tři pětiny"<br>
Poměr 1:4 = zlomek 1/4 = „čtvrtina"<br>
Poměr 1:2 = zlomek 1/2 = „polovina"
</div>
<table class="htable">
<tr><th style="background:#B7770D;color:white">Poměr</th><th style="background:#B7770D;color:white">Výpočet zlomku (z celku)</th><th style="background:#B7770D;color:white">Slovy</th></tr>
<tr><td>1:2</td><td>÷ 2</td><td>polovina</td></tr>
<tr><td>1:3</td><td>÷ 3</td><td>třetina</td></tr>
<tr><td>1:4</td><td>÷ 4</td><td>čtvrtina</td></tr>
<tr><td>1:5</td><td>÷ 5</td><td>pětina</td></tr>
<tr><td>2:5</td><td>÷ 5 × 2</td><td>dvě pětiny</td></tr>
</table>""", "#fffbf0", "#B7770D"),

("📐", "Přímá úměrnost — výpočet bez rovnic", f"""
<div class="ex"><div class="lbl">Jak může zadání vypadat (25r1 úloha 3)</div>
<i>„Mirkovo kolo se otočilo 30×, tátovo 25× — urazili stejnou vzdálenost. Kolikrát se Mirkovo otočí, pokud tátovo 30×?"</i>
</div>
<div class="ex"><div class="lbl">Základní pravidlo přímé úměrnosti</div>
Pokud jde čas 2× déle → vzdálenost 2× větší.<br>
Pokud je rychlost 3× větší → za stejný čas ujede 3× dál.<br>
<b>Stejný poměr, jiné hodnoty.</b>
</div>
<div class="ex"><div class="lbl">Metoda tabulky — vždy bezpečná</div>
<table class="htable">
<tr><th style="background:#B7770D;color:white">Mirkovo kolo</th><th style="background:#B7770D;color:white">Tátovo kolo</th></tr>
<tr><td>30 otáček</td><td>25 otáček</td></tr>
<tr><td>{fi('?')} otáček</td><td>30 otáček</td></tr>
</table>
Tátovo vzrostlo z 25 na 30 → násobíme 30÷25 = <b>6/5</b><br>
Mirkovo: 30 × (6/5) = 30 × 6 ÷ 5 = 180 ÷ 5 = <span class="hint-result">36 otáček</span>
</div>
<div class="ex"><div class="lbl">Rychlý způsob: křížové násobení</div>
Mirkovo × Tátovo2 = Tátovo × Mirkovo2<br>
30 × 30 = 25 × {fi('?')} → 900 = 25 × {fi('?')} → {fi('?')} = 900 ÷ 25 = <span class="hint-result">36</span>
</div>""", "#fffbf0", "#D4AC0D"),

("🍕", "Zlomky a části celku — jak počítat", f"""
<div class="ex"><div class="lbl">Jak může zadání vypadat (25r1 úloha 10)</div>
<i>„Maminka rozdělila peníze. Janě dala pětinu celkové částky, Ivo dostal dvakrát více než Jana a zbylých 240 Kč dala Evě. Kolik celkem?"</i>
</div>
<div class="ex"><div class="lbl">Krok 1: Zjisti, z ČEHO se počítá zlomek (základ = celek)</div>
„Pětina <b>celkové částky</b>" → základ = celková částka = {fi('C')}<br>
Jana = C ÷ 5 = <b>1/5 C</b><br>
Ivo = 2 × (C ÷ 5) = <b>2/5 C</b><br>
Eva = 240 Kč (zbytek)
</div>
<div class="ex"><div class="lbl">Krok 2: Doplň do celku = 1</div>
Jana + Ivo + Eva = celkem<br>
1/5 C + 2/5 C + 240 = C<br>
3/5 C + 240 = C → 240 = C − 3/5 C = 2/5 C<br>
C = 240 × 5 ÷ 2 = <span class="hint-result">600 Kč</span>
</div>
<div class="ex"><div class="lbl">Trik: zbývající část × (celek/zbytek) = celek</div>
Zbývá 2/5 → celku, tedy 240 = 2/5 celku → celku = 240 ÷ 2 × 5 = <span class="hint-result">600 Kč ✓</span>
</div>""", "#fffbf0", "#B7770D"),

("🔍", "Záludná slova — ne vše je co vypadá", f"""
<table class="htable">
<tr><th style="background:#B7770D;color:white">Slovo v zadání</th><th style="background:#B7770D;color:white">Výpočet</th><th style="background:#B7770D;color:white">Příklad (základ=60)</th></tr>
<tr><td><b>dvakrát více</b></td><td>základ × 2</td><td>60 × 2 = <b>120</b></td></tr>
<tr><td><b>o 2 více</b></td><td>základ + 2</td><td>60 + 2 = <b>62</b></td></tr>
<tr><td><b>o třetinu více</b></td><td>základ + základ÷3</td><td>60 + 20 = <b>80</b></td></tr>
<tr><td><b>třetina z</b></td><td>základ ÷ 3</td><td>60 ÷ 3 = <b>20</b></td></tr>
<tr><td><b>o třetinu méně</b></td><td>základ − základ÷3</td><td>60 − 20 = <b>40</b></td></tr>
<tr><td><b>třikrát méně</b> ⚠️</td><td>základ ÷ 3 (ne −3!)</td><td>60 ÷ 3 = <b>20</b></td></tr>
</table>
<div class="ex"><div class="lbl">Nejčastější záměna: dvakrát více vs. o dvě více</div>
„Ivo dostal <b>dvakrát více</b> než Jana" → Ivo = 2 × Jana (ne Jana + 2!)<br>
Pokud Jana = 80 Kč → Ivo = 2 × 80 = <span class="hint-result">160 Kč</span>
</div>""", "#fffbf0", "#D4AC0D"),

("➗", "Rozdělit v poměru — krok za krokem", f"""
<div class="ex"><div class="lbl">Jak může zadání vypadat</div>
<i>„Maminka rozdělila 240 Kč mezi Jana a Ivo v poměru 1:2."</i>
</div>
<div class="ex"><div class="lbl">Postup</div>
<ol>
<li>Sečti díly: 1 + 2 = <b>3 díly</b> celkem</li>
<li>Jeden díl: 240 ÷ 3 = <b>80 Kč</b></li>
<li>Jana: 1 díl = <b>80 Kč</b></li>
<li>Ivo: 2 díly = 2 × 80 = <b>160 Kč</b></li>
<li>Ověř: 80 + 160 = 240 ✓</li>
</ol>
</div>
<div class="ex"><div class="lbl">Obecný vzorec</div>
Poměr a:b → celkem ÷ (a+b) = <b>1 díl</b><br>
{calc_row('celkem', '÷ (a+b)', '1 díl')} → {calc_row('1 díl', '× a', 'část A')} a {calc_row('1 díl', '× b', 'část B')}
</div>
<div class="ex"><div class="lbl">Příklad: poměr kuliček (25r1 úloha 4)</div>
Na váze: 1 velká (30g) + 2 malé (20g) na každou velkou, celkem 560g<br>
Hledám: kolik velkých?<br>
1 velká + 2 malé = 30 + 40 = <b>70g za skupinu</b><br>
Počet skupin: 560 ÷ 70 = <b>8 skupin</b> → <span class="hint-result">8 velkých, 16 malých</span>
</div>""", "#fffbf0", "#B7770D"),

("⚠️", "Nejčastější chyby u poměrů a zlomků", f"""
<table class="htable">
<tr><th style="background:#C0392B;color:white">Chyba</th><th style="background:#C0392B;color:white">Jak to správně</th></tr>
<tr><td>🔴 „Pětina celku" → dělím pětinou (×1/5) ale myslím ×5</td><td>Pětina = ÷5. Ověř: pětina ze 100 = 20, ne 500!</td></tr>
<tr><td>🔴 „Dvakrát více" → přičítám 2 místo násobení 2</td><td>Dvakrát více = ×2. Třikrát více = ×3. „Více" = násobit!</td></tr>
<tr><td>🔴 Zjednodušuji poměr: 6:4 = 3:2 — dělím jen jedno číslo</td><td>Vždy děl OBOJE čísla stejným číslem!</td></tr>
<tr><td>🔴 U přímé úměrnosti: míchám čí hodnoty jsou čí</td><td>Vypiš tabulku: Mirkovo | Tátovo | řádek 1 a řádek 2</td></tr>
<tr><td>🔴 „Zbývá 240 Kč" — myslím to je polovina celku</td><td>Zjisti, jaký zlomek zbývá (1 − součet ostatních dílů)</td></tr>
</table>""", "#fff0f0", "#C0392B"),
]

# ══ QUIZ DATA (imported from quiz_backup.py) ══
exec(open('/home/claude/quiz_backup.py', encoding='utf-8').read())
