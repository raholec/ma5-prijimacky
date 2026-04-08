#!/usr/bin/env bash
# =============================================================================
# PIPELINE TŘÍ AGENTŮ — MA5 Prijimacky
# Použití: bash pipeline.sh [PL01|PL02|...|PL09|25n1|25r1|...]
#
# Pracovní listy (PL01–PL09):
#   Agent 1 — UČITEL MATEMATIKY: čte a upravuje hints_data.py
#   Agent 2 — ŽÁK 5. TŘÍDY:      testuje srozumitelnost, dává zpětnou vazbu
#   Agent 3 — PRACOVNÍK CERMAT:   posuzuje strukturu, doporučuje změny
#
# Vzorová řešení (25n1, 25r1, ...):
#   Agent 1 — UČITEL MATEMATIKY: vylepšuje kroky řešení v HTML
#   Agent 2 — ŽÁK 5. TŘÍDY:      testuje srozumitelnost kroků
#   Agent 3 — PRACOVNÍK CERMAT:   ověřuje správnost a didaktiku
# =============================================================================
set -euo pipefail

# ── konfigurace ────────────────────────────────────────────────────────────
ID="${1:-PL01}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPORTS_DIR="$SCRIPT_DIR/reports"
CLAUDE_BIN="${CLAUDE_BIN:-claude}"

declare -A PL_NAMES=(
  [PL01]="Geometrická konstrukce"
  [PL02]="Prostorová představivost"
  [PL03]="Posloupnosti a vzory"
  [PL04]="Grafy pravdivé/nepravdivé"
  [PL05]="Soustavy podmínek"
  [PL06]="Obvod a obsah"
  [PL07]="Výrazy a závorky"
  [PL08]="Jednotky a převody"
  [PL09]="Poměry a zlomky"
)

declare -A RESENI_NAMES=(
  [25n1]="MA5-C · 1. náhradní termín 2025"
  [25n2]="MA5-C · 2. náhradní termín 2025"
  [25r1]="MA5-C · 1. řádný termín 2025"
  [25r2]="MA5-C · 2. řádný termín 2025"
)

# ── rozpoznání typu (PL vs řešení) ────────────────────────────────────────
MODE=""
if [[ -n "${PL_NAMES[$ID]+x}" ]]; then
  MODE="pl"
  PL_ID="$ID"
  PL_NAME="${PL_NAMES[$ID]}"
elif [[ -n "${RESENI_NAMES[$ID]+x}" ]]; then
  MODE="reseni"
  RESENI_ID="$ID"
  RESENI_NAME="${RESENI_NAMES[$ID]}"
  RESENI_FILE="$SCRIPT_DIR/docs/reseni/${RESENI_ID}.html"
  if [[ ! -f "$RESENI_FILE" ]]; then
    echo "Chyba: Soubor '$RESENI_FILE' neexistuje." >&2
    exit 1
  fi
else
  echo "Chyba: Neznámé ID '$ID'." >&2
  echo "Platné hodnoty: PL01–PL09, 25n1, 25n2, 25r1, 25r2" >&2
  exit 1
fi

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
REPORT_FILE="$REPORTS_DIR/${ID}_${TIMESTAMP}.md"
TEACHER_FILE="$REPORTS_DIR/.teacher_tmp.txt"
STUDENT_FILE="$REPORTS_DIR/.student_tmp.txt"

mkdir -p "$REPORTS_DIR"

# ── pomocné funkce ─────────────────────────────────────────────────────────
banner() {
  echo ""
  echo "══════════════════════════════════════════════════════════════"
  echo "  $1"
  echo "══════════════════════════════════════════════════════════════"
}

step() {
  echo ""
  echo "  ▶ $1"
}

ok() {
  echo "  ✓ $1"
}

# ── hlavní pipeline ────────────────────────────────────────────────────────
cd "$SCRIPT_DIR"

if [[ "$MODE" == "pl" ]]; then
  # ═══════════════════════════════════════════════════════════════════════
  # REŽIM: PRACOVNÍ LIST (PL01–PL09)
  # ═══════════════════════════════════════════════════════════════════════
  banner "PIPELINE: $PL_ID — $PL_NAME"

  # AGENT 1: UČITEL MATEMATIKY — upravuje hints_data.py
  banner "AGENT 1 — UČITEL MATEMATIKY (upravuje hints_data.py)"
  step "Spouštím učitelského agenta..."

  "$CLAUDE_BIN" -p \
    --system-prompt "Jsi zkušený učitel matematiky na 1. stupni základní školy s 15 lety praxe. Specializuješ se na přípravu žáků 5. třídy na přijímací zkoušky MA5 na víceletá gymnázia. Používáš vizuální metody, konkrétní příklady z každodenního života a postup krok za krokem. Nikdy nepoužíváš rovnice ani algebru — vše vysvětluješ logicky a graficky. Dbáš na to, aby žák pochopil PROČ, nejen JAK. Mluvíš jazykem přátelským pro 11leté dítě." \
    --allowedTools "Read,Edit,Glob" \
    --permission-mode acceptEdits \
    "Přečti soubor hints_data.py. Najdi sekci HINTS_${PL_ID} (pracovní list ${PL_ID} — ${PL_NAME}).

Jako zkušený učitel matematiky chystající se doučovat žáka 5. třídy:

1. Prostuduj každý hint blok v sekci HINTS_${PL_ID}
2. Vyber 2–3 hinty, které lze pedagogicky vylepšit pro 11leté dítě
3. Uprav je přímo v hints_data.py nástrojem Edit — přidej:
   - Konkrétní příklady z života (jablka, délky, čas, peníze...)
   - Jednodušší jazyk bez zbytečných odborných termínů
   - Postup krok za krokem s mezivýsledky
   - Tip nebo varování na nejčastější chybu žáků
4. Zachovej Python syntaxi, f-stringy a HTML strukturu
5. Neměň SVG kód ani funkce fi(), diag(), calc_row()
6. Posledni hint blok s 'Nejčastější chyby' vždy zachovej nebo vylepši

Na konci napiš stručné shrnutí (max 300 slov):
- Které hinty jsi změnil/a (číslo + název)
- Co konkrétně jsi přidal/a a proč
- Jak to pomůže žákovi lépe pochopit látku" \
    > "$TEACHER_FILE" 2>&1

  ok "Učitel dokončil úpravy."
  echo ""
  cat "$TEACHER_FILE"

  # AGENT 2: ŽÁK 5. TŘÍDY — testuje srozumitelnost hintů
  banner "AGENT 2 — ŽÁK 5. TŘÍDY (testuje srozumitelnost)"
  step "Spouštím žákovského agenta..."

  TEACHER_SUMMARY=$(cat "$TEACHER_FILE")
  PROMPT2=$(mktemp)
  cat > "$PROMPT2" <<PROMPT
Přečti sekci HINTS_${PL_ID} v souboru hints_data.py (téma: ${PL_NAME}).

Učitel pracovní list právě upravil. Tady je jeho shrnutí změn:
--- SHRNUTÍ UČITELE ---
${TEACHER_SUMMARY}
--- KONEC SHRNUTÍ ---

Přečti si vysvětlení v sekci HINTS_${PL_ID} a odpověz jako žák 5. třídy:

1. **Co ti bylo jasné** — které vysvětlení ti pomohlo, proč?
2. **Co ti bylo nejasné** — kde ses zasekl/a, co nechápeš?
3. **Nejlepší vysvětlení** — které ti sedlo nejvíc a proč?
4. **Co bys změnil/a** — jak by se ti studovalo lépe?
5. **Hodnocení hvězdičkami** — dej pracovnímu listu 1–5 ⭐ (1 = nejlepší)

Piš neformálně, jako když píšeš kamarádovi. Buď upřímný/á.
PROMPT

  "$CLAUDE_BIN" -p \
    --system-prompt "Jsi žák nebo žákyně 5. třídy základní školy, je ti 11 let. Připravuješ se na přijímací zkoušky na víceleté gymnázium. Matematiku celkem zvládáš, ale někdy se zasekneš u složitějšího zadání. Nemáš rád/a nudné texty plné odborných slov. Chceš jasné, rychlé vysvětlení s příklady. Odpovídáš upřímně a neformálně — jako skutečný žák, ne jako dospělý." \
    --allowedTools "Read" \
    < "$PROMPT2" > "$STUDENT_FILE" 2>&1
  rm -f "$PROMPT2"

  ok "Žák dokončil hodnocení."
  echo ""
  cat "$STUDENT_FILE"

  # AGENT 3: PRACOVNÍK CERMAT — posuzuje strukturu
  banner "AGENT 3 — PRACOVNÍK CERMAT (posuzuje strukturu)"
  step "Spouštím CERMAT agenta..."

  TEACHER_SUMMARY=$(cat "$TEACHER_FILE")
  STUDENT_FEEDBACK=$(cat "$STUDENT_FILE")
  PROMPT3=$(mktemp)
  cat > "$PROMPT3" <<PROMPT
Posuz didaktický materiál pro přípravu na přijímací zkoušky MA5.

Pracovní list: ${PL_ID} — ${PL_NAME}

Co učitel upravil v hints_data.py:
--- SHRNUTÍ UČITELE ---
${TEACHER_SUMMARY}
--- KONEC SHRNUTÍ ---

Zpětná vazba žáka 5. třídy:
--- ZPĚTNÁ VAZBA ŽÁKA ---
${STUDENT_FEEDBACK}
--- KONEC ZPĚTNÉ VAZBY ---

Přečti si aktuální stav sekce HINTS_${PL_ID} v hints_data.py.

Z pozice pracovníka CERMAT posud:

1. **Soulad s testovými úlohami** — odpovídají vysvětlení tomu, co MA5 skutečně testuje? Chybí nějaký typ úlohy?
2. **Pedagogická správnost** — je postup vysvětlování didakticky vhodný pro věkovou skupinu?
3. **Gradace obtížnosti** — je přechod od jednoduchého ke složitějšímu správný?
4. **Pokrytí typických chyb** — jsou pokryty chyby, které žáci v MA5 testech nejčastěji dělají?
5. **Konkrétní doporučení** — co přesně změnit ve struktuře nebo postupu?

Buď konkrétní — cituj části textu a navrhuj přesné změny. Max 500 slov.
PROMPT

  "$CLAUDE_BIN" -p \
    --system-prompt "Jsi zkušený odborný pracovník Centra pro zjišťování výsledků vzdělávání (CERMAT) s 10 lety zkušeností. Podílel/a ses na tvorbě a hodnocení didaktických testů MA5 pro přijímací zkoušky na víceletá gymnázia. Výborně znáš požadavky na matematické kompetence žáků 5. třídy, typické chyby v testech a způsoby, jak na ně žáky připravit. Hodnotíš didaktické materiály odborně, konstruktivně a konkrétně." \
    --allowedTools "Read" \
    < "$PROMPT3" 2>&1 | tee -a "$REPORT_FILE.cermat_tmp"
  rm -f "$PROMPT3"

  CERMAT_REPORT=$(cat "$REPORT_FILE.cermat_tmp" 2>/dev/null || echo "")

else
  # ═══════════════════════════════════════════════════════════════════════
  # REŽIM: VZOROVÉ ŘEŠENÍ (25n1, 25r1, ...)
  # ═══════════════════════════════════════════════════════════════════════
  banner "PIPELINE: $RESENI_ID — $RESENI_NAME (vzorové řešení)"

  # AGENT 1: UČITEL MATEMATIKY — vylepšuje kroky řešení v HTML
  banner "AGENT 1 — UČITEL MATEMATIKY (vylepšuje kroky řešení)"
  step "Spouštím učitelského agenta..."

  "$CLAUDE_BIN" -p \
    --system-prompt "Jsi zkušený učitel matematiky na 1. stupni základní školy s 15 lety praxe. Specializuješ se na přípravu žáků 5. třídy na přijímací zkoušky MA5 na víceletá gymnázia. Používáš vizuální metody, konkrétní příklady z každodenního života a postup krok za krokem. Nikdy nepoužíváš rovnice ani algebru — vše vysvětluješ logicky a graficky. Dbáš na to, aby žák pochopil PROČ, nejen JAK. Mluvíš jazykem přátelským pro 11leté dítě." \
    --allowedTools "Read,Edit,Glob" \
    --permission-mode acceptEdits \
    "Přečti soubor docs/reseni/${RESENI_ID}.html — vzorové řešení testu ${RESENI_NAME}.

Soubor obsahuje 14 úloh z přijímacího testu MA5 s krokovým řešením. Každá úloha má:
- div.zadani — zadání úlohy
- div.steps s div.step — jednotlivé kroky řešení
- div.answer — výsledek

Jako zkušený učitel matematiky vylepši vysvětlení kroků pro žáka 5. třídy:

1. Prostuduj všech 14 úloh a jejich kroky
2. Vyber 3–5 úloh, jejichž kroky řešení lze pedagogicky vylepšit
3. Uprav je přímo v HTML souboru nástrojem Edit:
   - Přidej mezikroky tam, kde žák přeskakuje příliš velký myšlenkový skok
   - Přepiš odborný jazyk do řeči srozumitelné 11letému dítěti
   - Přidej konkrétní příklady z života (jablka, peníze, cesta do školy...)
   - Přidej vizuální nápovědu (emoji, zvýraznění klíčových čísel)
   - Upozorni na nejčastější chybu v kroku (kde se žáci nejčastěji spletou)
4. NEMĚŇ výsledky, odpovědi ani HTML strukturu (třídy, tagy)
5. NEMĚŇ CSS styly ani hlavičku stránky
6. Zachovej <span class=\"calc\"> pro důležité mezivýsledky

Na konci napiš stručné shrnutí (max 300 slov):
- Které úlohy jsi vylepšil/a (číslo + název)
- Co konkrétně jsi přidal/a a proč
- Jak to pomůže žákovi lépe pochopit postup řešení" \
    > "$TEACHER_FILE" 2>&1

  ok "Učitel dokončil úpravy."
  echo ""
  cat "$TEACHER_FILE"

  # AGENT 2: ŽÁK 5. TŘÍDY — testuje srozumitelnost kroků řešení
  banner "AGENT 2 — ŽÁK 5. TŘÍDY (testuje srozumitelnost)"
  step "Spouštím žákovského agenta..."

  TEACHER_SUMMARY=$(cat "$TEACHER_FILE")
  PROMPT2=$(mktemp)
  cat > "$PROMPT2" <<PROMPT
Přečti soubor docs/reseni/${RESENI_ID}.html — vzorové řešení testu ${RESENI_NAME}.

Učitel právě vylepšil kroky řešení. Tady je jeho shrnutí:
--- SHRNUTÍ UČITELE ---
${TEACHER_SUMMARY}
--- KONEC SHRNUTÍ ---

Přečti si kroky řešení u všech 14 úloh a odpověz jako žák 5. třídy:

1. **Která řešení ti byla jasná** — u kterých úloh jsi pochopil/a každý krok?
2. **Kde ses zasekl/a** — u kterého kroku které úlohy ses ztratil/a? Co nechápeš?
3. **Nejlepší vysvětlení** — která úloha měla úplně nejlepší kroky a proč?
4. **Nejtěžší úloha** — kterou bys bez pomoci nespočítal/a? Co ti chybí?
5. **Co bys změnil/a** — jak by se ti řešení studovalo lépe?
6. **Hodnocení hvězdičkami** — dej vzorovému řešení 1–5 ⭐ (1 = nejlepší)

Piš neformálně, jako když píšeš kamarádovi. Buď upřímný/á.
PROMPT

  "$CLAUDE_BIN" -p \
    --system-prompt "Jsi žák nebo žákyně 5. třídy základní školy, je ti 11 let. Připravuješ se na přijímací zkoušky na víceleté gymnázium. Matematiku celkem zvládáš, ale někdy se zasekneš u složitějšího zadání. Nemáš rád/a nudné texty plné odborných slov. Chceš jasné, rychlé vysvětlení s příklady. Odpovídáš upřímně a neformálně — jako skutečný žák, ne jako dospělý." \
    --allowedTools "Read" \
    < "$PROMPT2" > "$STUDENT_FILE" 2>&1
  rm -f "$PROMPT2"

  ok "Žák dokončil hodnocení."
  echo ""
  cat "$STUDENT_FILE"

  # AGENT 3: PRACOVNÍK CERMAT — ověřuje správnost a didaktiku řešení
  banner "AGENT 3 — PRACOVNÍK CERMAT (ověřuje správnost a didaktiku)"
  step "Spouštím CERMAT agenta..."

  TEACHER_SUMMARY=$(cat "$TEACHER_FILE")
  STUDENT_FEEDBACK=$(cat "$STUDENT_FILE")
  PROMPT3=$(mktemp)
  cat > "$PROMPT3" <<PROMPT
Posud vzorové řešení přijímacího testu MA5: ${RESENI_NAME}.

Soubor: docs/reseni/${RESENI_ID}.html

Učitel vylepšil kroky řešení:
--- SHRNUTÍ UČITELE ---
${TEACHER_SUMMARY}
--- KONEC SHRNUTÍ ---

Zpětná vazba žáka 5. třídy:
--- ZPĚTNÁ VAZBA ŽÁKA ---
${STUDENT_FEEDBACK}
--- KONEC ZPĚTNÉ VAZBY ---

Přečti si aktuální stav souboru docs/reseni/${RESENI_ID}.html.

Z pozice pracovníka CERMAT posud:

1. **Správnost výsledků** — souhlasí výsledky s oficiálním klíčem CZVV? Jsou výpočty v krocích správné?
2. **Úplnost řešení** — jsou kroky dostatečně podrobné? Nechybí důležitý mezikrok?
3. **Pedagogická vhodnost** — je postup řešení vhodný pro žáka 5. třídy (bez rovnic, algebry)?
4. **Srozumitelnost** — pochopí žák z kroků PROČ se daný postup používá, nejen JAK?
5. **Konkrétní doporučení** — co přesně vylepšit v krocích řešení? Cituj konkrétní pasáže.

Buď konkrétní a konstruktivní. Max 500 slov.
PROMPT

  "$CLAUDE_BIN" -p \
    --system-prompt "Jsi zkušený odborný pracovník Centra pro zjišťování výsledků vzdělávání (CERMAT) s 10 lety zkušeností. Podílel/a ses na tvorbě a hodnocení didaktických testů MA5 pro přijímací zkoušky na víceletá gymnázia. Výborně znáš požadavky na matematické kompetence žáků 5. třídy, typické chyby v testech a způsoby, jak na ně žáky připravit. Hodnotíš didaktické materiály odborně, konstruktivně a konkrétně." \
    --allowedTools "Read" \
    < "$PROMPT3" 2>&1 | tee -a "$REPORT_FILE.cermat_tmp"
  rm -f "$PROMPT3"

  CERMAT_REPORT=$(cat "$REPORT_FILE.cermat_tmp" 2>/dev/null || echo "")
fi

# =============================================================================
# VÝSTUPNÍ REPORT
# =============================================================================
banner "VÝSTUPNÍ REPORT"

if [[ "$MODE" == "pl" ]]; then
  REPORT_TITLE="${PL_ID} — ${PL_NAME}"
else
  REPORT_TITLE="${RESENI_ID} — ${RESENI_NAME} (vzorové řešení)"
fi

cat > "$REPORT_FILE" << HEREDOC
# Pipeline Report: ${REPORT_TITLE}
Datum: $(date '+%d. %m. %Y %H:%M')

---

## Agent 1 — Učitel matematiky: Co bylo upraveno

$(cat "$TEACHER_FILE")

---

## Agent 2 — Žák 5. třídy: Zpětná vazba

$(cat "$STUDENT_FILE")

---

## Agent 3 — Pracovník CERMAT: Doporučení

${CERMAT_REPORT}

---
*Vygenerováno pipeline.sh*
HEREDOC

# úklid dočasných souborů
rm -f "$TEACHER_FILE" "$STUDENT_FILE" "$REPORT_FILE.cermat_tmp"

ok "Report uložen: $REPORT_FILE"
banner "PIPELINE DOKONČENA"
