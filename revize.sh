#!/usr/bin/env bash
# =============================================================================
# REVIZE A KOREKTURY — MA5 Prijimacky
# Použití: bash revize.sh [PL01|PL02|...|PL09|25n1|25r1|...|strategie35|...]
#
# Agent 1 — UČITEL MATEMATIKY:  upravuje obsah (hinty / kroky řešení)
# Agent 2 — ŽÁK 5. TŘÍDY:      testuje srozumitelnost, zpětná vazba
# Agent 3 — PRACOVNÍK CERMAT:   posuzuje strukturu a správnost
# Agent 4 — GRAFIK CERMAT:      navrhuje obrázky, grafy a vizuální doplnění
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
  [23r1]="MA5-C · 1. řádný termín 2023"
)

declare -A PRUVODCE_NAMES=(
  [23r1]="MA5-C · 1. řádný termín 2023"
)

declare -A PRUVODCE_PO_NAMES=(
  [23r1]="MA5-C · 1. řádný termín 2023"
)

declare -A PAGE_NAMES=(
  [strategie35]="Strategie 35 bodů"
  [cviceni39b]="Procvičování na 39 bodů"
)
declare -A PAGE_FILES=(
  [strategie35]="docs/pages/PL_Strategie35.html"
  [cviceni39b]="docs/pages/PL_Cviceni_39b.html"
)

# ── rozpoznání typu (PL vs řešení vs průvodce vs pruvodce_po) ─────────────
# Formát: PL01, 25n1, pruvodce-23r1, pruvodce_po-23r1
MODE=""
RAW_ID="$ID"

if [[ "$ID" == pruvodce_po-* ]]; then
  MODE="pruvodce_po"
  PRUVODCE_PO_KEY="${ID#pruvodce_po-}"
  if [[ -z "${PRUVODCE_PO_NAMES[$PRUVODCE_PO_KEY]+x}" ]]; then
    echo "Chyba: Neznámý průvodce_po '$PRUVODCE_PO_KEY'." >&2
    echo "Platné hodnoty: ${!PRUVODCE_PO_NAMES[*]}" >&2
    exit 1
  fi
  PRUVODCE_PO_ID="$PRUVODCE_PO_KEY"
  PRUVODCE_PO_NAME="${PRUVODCE_PO_NAMES[$PRUVODCE_PO_KEY]}"
  PRUVODCE_PO_FILE="$SCRIPT_DIR/docs/pruvodce_po/${PRUVODCE_PO_ID}.html"
  if [[ ! -f "$PRUVODCE_PO_FILE" ]]; then
    echo "Chyba: Soubor '$PRUVODCE_PO_FILE' neexistuje." >&2
    exit 1
  fi
elif [[ "$ID" == pruvodce-* ]]; then
  MODE="pruvodce"
  PRUVODCE_KEY="${ID#pruvodce-}"
  if [[ -z "${PRUVODCE_NAMES[$PRUVODCE_KEY]+x}" ]]; then
    echo "Chyba: Neznámý průvodce '$PRUVODCE_KEY'." >&2
    echo "Platné hodnoty: ${!PRUVODCE_NAMES[*]}" >&2
    exit 1
  fi
  PRUVODCE_ID="$PRUVODCE_KEY"
  PRUVODCE_NAME="${PRUVODCE_NAMES[$PRUVODCE_KEY]}"
  PRUVODCE_FILE="$SCRIPT_DIR/docs/pruvodce/${PRUVODCE_ID}.html"
  if [[ ! -f "$PRUVODCE_FILE" ]]; then
    echo "Chyba: Soubor '$PRUVODCE_FILE' neexistuje." >&2
    exit 1
  fi
elif [[ -n "${PL_NAMES[$ID]+x}" ]]; then
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
elif [[ -n "${PAGE_NAMES[$ID]+x}" ]]; then
  MODE="page"
  PAGE_ID="$ID"
  PAGE_NAME="${PAGE_NAMES[$ID]}"
  PAGE_FILE="$SCRIPT_DIR/${PAGE_FILES[$ID]}"
  if [[ ! -f "$PAGE_FILE" ]]; then
    echo "Chyba: Soubor '$PAGE_FILE' neexistuje." >&2
    exit 1
  fi
else
  echo "Chyba: Neznámé ID '$ID'." >&2
  echo "Platné hodnoty: PL01–PL09, 25n1, 25n2, 25r1, 25r2, 23r1, pruvodce-23r1, pruvodce_po-23r1, strategie35" >&2
  exit 1
fi

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
REPORT_FILE="$REPORTS_DIR/${ID}_${TIMESTAMP}.md"
TEACHER_FILE="$REPORTS_DIR/.teacher_tmp.txt"
STUDENT_FILE="$REPORTS_DIR/.student_tmp.txt"
GRAFIK_FILE="$REPORTS_DIR/.grafik_tmp.txt"
DIALOG_FILE="$REPORTS_DIR/.dialog_tmp.txt"
DIALOG_ROUNDS="${DIALOG_ROUNDS:-2}"

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

# ── dialóg učitel ↔ žák ───────────────────────────────────────────────────
# Použití: run_dialog "<instrukce co číst>" "<název kontextu>" "<system prompt učitele>"
# Čte TEACHER_FILE (shrnutí Agent 1), zapisuje transcript do DIALOG_FILE.
# Žák: ✅ ROZUMÍM / ❌ NEROZUMÍM pro každý krok.
# Učitel: opravuje POUZE části označené ❌ a přidává je do souboru přes Edit.
# Pokud žák neoznačí žádné ❌, smyčka se ukončí předčasně.
run_dialog() {
  local file_read="$1" ctx_name="$2" teacher_sys="$3"
  local round teacher_summary student_reply prompt_tmp
  : > "$DIALOG_FILE"
  teacher_summary=$(cat "$TEACHER_FILE")

  for round in $(seq 1 "$DIALOG_ROUNDS"); do
    banner "DIALOG — KOLO $round / $DIALOG_ROUNDS  (učitel ↔ žák)"

    # ─── Žák reaguje ──────────────────────────────────────────────────────
    step "Žák čte vysvětlení a reaguje (kolo $round)..."
    prompt_tmp=$(mktemp)
    printf '%s\n\n' "$file_read" > "$prompt_tmp"
    printf 'Kontext: %s\n\n' "$ctx_name" >> "$prompt_tmp"
    printf 'Učitel právě upravil vysvětlení. Co změnil:\n--- CO UČITEL ZMĚNIL ---\n%s\n--- KONEC ---\n\n' \
      "$teacher_summary" >> "$prompt_tmp"
    cat >> "$prompt_tmp" << 'ŽÁKINST'
Projdi každou upravenou část POSTUPNĚ — krok po kroku, vysvětlení po vysvětlení.
Pro každý krok nebo princip napiš přesně jednu z těchto dvou reakcí:

  ✅ ROZUMÍM — [napiš co ti bylo jasné a proč to dává smysl]
  ❌ NEROZUMÍM — [cituj přesnou větu nebo krok, který nechápeš, a řekni PROČ ti to nedává smysl]

Pravidla:
- Buď velmi konkrétní. Nestačí napsat "nechápu to" — musíš říct přesně která věta nebo číslo.
- Nikdy netvrdíš že rozumíš, když to není pravda — učitel musí vědět co opravit.
- Piš jako žák 5. třídy, neformálně.
ŽÁKINST
    student_reply=$("$CLAUDE_BIN" -p \
      --system-prompt "Jsi žák nebo žákyně 5. třídy, 11 let. Připravuješ se na přijímací zkoušky MA5. Matematiku celkem zvládáš, ale potřebuješ jasné, konkrétní vysvětlení každého kroku. Odpovídáš upřímně a přesně — říkáš konkrétně co chápeš a co ne. Nikdy netvrdíš že rozumíš, když to není pravda." \
      --allowedTools "Read" \
      < "$prompt_tmp" 2>&1)
    rm -f "$prompt_tmp"

    ok "Žák odpověděl (kolo $round)."
    echo ""
    echo "$student_reply"
    printf '\n### Dialog kolo %s — Žák\n\n%s\n' "$round" "$student_reply" >> "$DIALOG_FILE"

    # ─── Konec pokud vše jasné ────────────────────────────────────────────
    if ! echo "$student_reply" | grep -qi 'NEROZUMÍM'; then
      ok "Žák neoznačil žádné ❌ — dialog ukončen předčasně po kole $round."
      return
    fi

    # ─── Učitel opravuje (ne v posledním kole) ───────────────────────────
    if [[ $round -lt $DIALOG_ROUNDS ]]; then
      step "Učitel opravuje nepochopené části (kolo $round)..."
      prompt_tmp=$(mktemp)
      printf '%s\n\n' "$file_read" > "$prompt_tmp"
      printf 'Žák 5. třídy reagoval takto:\n--- ZPĚTNÁ VAZBA ŽÁKA ---\n%s\n--- KONEC ---\n\n' \
        "$student_reply" >> "$prompt_tmp"
      cat >> "$prompt_tmp" << 'UČITELINST'
Zaměř se VÝHRADNĚ na části, kde žák napsal "❌ NEROZUMÍM".
Pro každou takovou část uprav text přímo v souboru (nástrojem Edit):
  - Rozlom krok na menší části nebo přidej mezikrok
  - Použij jednodušší slova nebo přirovnání z každodenního života (jablka, peníze, vzdálenost...)
  - Přidej konkrétní číselný příklad pokud chybí
  - Nahraď abstraktní popis konkrétním postupem

NEUPRAVUJ části označené "✅ ROZUMÍM" — ty jsou v pořádku, neměň je.

Napiš stručné shrnutí: které části jsi upravil/a a jak to řeší žákovy konkrétní problémy.
UČITELINST
      teacher_summary=$("$CLAUDE_BIN" -p \
        --system-prompt "$teacher_sys" \
        --allowedTools "Read,Edit" \
        --permission-mode acceptEdits \
        < "$prompt_tmp" 2>&1)
      rm -f "$prompt_tmp"

      ok "Učitel upravil (kolo $round)."
      echo ""
      echo "$teacher_summary"
      printf '\n### Dialog kolo %s — Učitel\n\n%s\n' "$round" "$teacher_summary" >> "$DIALOG_FILE"
    fi
  done
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

  # DIALOG: UČITEL ↔ ŽÁK — iterativní zpřesňování vysvětlení
  banner "DIALOG — UČITEL ↔ ŽÁK (${DIALOG_ROUNDS} kola)"
  run_dialog \
    "Přečti si sekci HINTS_${PL_ID} v souboru hints_data.py (téma: ${PL_NAME})." \
    "${PL_ID} — ${PL_NAME}" \
    "Jsi zkušený učitel matematiky s 15 lety praxe. Připravuješ žáky 5. třídy na MA5. Nikdy nepoužíváš rovnice ani algebru. Dostáváš konkrétní zpětnou vazbu od žáka a upravuješ POUZE místa, která jsou nejasná — cíleně a konkrétně."

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

  # AGENT 4: GRAFIK CERMAT — navrhuje vizuální doplnění
  banner "AGENT 4 — GRAFIK CERMAT (navrhuje obrázky a grafy)"
  step "Spouštím grafického agenta..."

  TEACHER_SUMMARY=$(cat "$TEACHER_FILE")
  STUDENT_FEEDBACK=$(cat "$STUDENT_FILE")
  PROMPT4=$(mktemp)
  cat > "$PROMPT4" <<PROMPT
Posud vizuální stránku didaktického materiálu pro přijímací zkoušky MA5.

Pracovní list: ${PL_ID} — ${PL_NAME}

Shrnutí učitele (co bylo upraveno):
--- SHRNUTÍ UČITELE ---
${TEACHER_SUMMARY}
--- KONEC SHRNUTÍ ---

Zpětná vazba žáka 5. třídy:
--- ZPĚTNÁ VAZBA ŽÁKA ---
${STUDENT_FEEDBACK}
--- KONEC ZPĚTNÉ VAZBY ---

Přečti si aktuální stav sekce HINTS_${PL_ID} v hints_data.py a vygenerovaný HTML soubor docs/pages/PL${PL_ID#PL}_*.html.

Z pozice zkušeného grafika navrhni:

1. **Stávající vizuály** — Existují v materiálu SVG diagramy, tabulky nebo schémata? Jsou srozumitelné pro 11leté dítě? Navrhni konkrétní vylepšení (barvy, popisky, velikost).

2. **Kde chybí obrázek nebo graf** — Projdi každý hint a příklad. U kterých by přidání vizuálu výrazně pomohlo pochopení? Pro každý návrh uveď:
   - Přesné místo (číslo hintu, název, kontext)
   - Typ vizuálu (schéma, diagram, graf, tabulka, nákres)
   - Co přesně má vizuál zobrazovat
   - Proč to pomůže žákovi

3. **Grafy pro procvičování** — Navrhni 1–2 vizuály, které by mohly sloužit jako samostatné cvičení (žák čte z grafu, doplňuje do schématu apod.)

4. **Technické doporučení** — Jaký formát vizuálu je nejvhodnější (inline SVG v hints_data.py, obrázek PNG, ASCII diagram)? Jak zajistit čitelnost na mobilu i při tisku?

Buď konkrétní — u každého návrhu popiš CO nakreslit, ne jen „přidej obrázek". Max 500 slov.
PROMPT

  "$CLAUDE_BIN" -p \
    --system-prompt "Jsi zkušený autor grafů a ilustrací pro didaktické materiály CERMAT s 10 lety praxe. Tvoříš obrázky, schémata, diagramy a grafy pro přijímací testy MA5 na víceletá gymnázia. Výborně znáš, jak vizualizovat matematické koncepty pro žáky 5. třídy — používáš jasné barvy, velké popisky, jednoduché tvary a minimální text. Víš, že správný obrázek dokáže vysvětlit víc než odstavec textu. Tvé vizuály jsou přehledné, barevně konzistentní a fungují jak na obrazovce, tak při tisku na papír." \
    --allowedTools "Read,Glob" \
    < "$PROMPT4" > "$GRAFIK_FILE" 2>&1
  rm -f "$PROMPT4"

  ok "Grafik dokončil návrhy."
  echo ""
  cat "$GRAFIK_FILE"

elif [[ "$MODE" == "reseni" ]]; then
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

  # DIALOG: UČITEL ↔ ŽÁK — iterativní zpřesňování kroků řešení
  banner "DIALOG — UČITEL ↔ ŽÁK (${DIALOG_ROUNDS} kola)"
  run_dialog \
    "Přečti si soubor docs/reseni/${RESENI_ID}.html — vzorové řešení testu ${RESENI_NAME}." \
    "${RESENI_ID} — ${RESENI_NAME}" \
    "Jsi zkušený učitel matematiky s 15 lety praxe. Připravuješ žáky 5. třídy na MA5. Nikdy nepoužíváš rovnice ani algebru. Dostáváš konkrétní zpětnou vazbu od žáka a upravuješ POUZE kroky řešení, která jsou nejasná — cíleně a konkrétně."

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

  # AGENT 4: GRAFIK CERMAT — navrhuje vizuální doplnění řešení
  banner "AGENT 4 — GRAFIK CERMAT (navrhuje obrázky a grafy)"
  step "Spouštím grafického agenta..."

  TEACHER_SUMMARY=$(cat "$TEACHER_FILE")
  STUDENT_FEEDBACK=$(cat "$STUDENT_FILE")
  PROMPT4=$(mktemp)
  cat > "$PROMPT4" <<PROMPT
Posud vizuální stránku vzorového řešení přijímacího testu MA5: ${RESENI_NAME}.

Soubor: docs/reseni/${RESENI_ID}.html

Shrnutí učitele (co bylo upraveno):
--- SHRNUTÍ UČITELE ---
${TEACHER_SUMMARY}
--- KONEC SHRNUTÍ ---

Zpětná vazba žáka 5. třídy:
--- ZPĚTNÁ VAZBA ŽÁKA ---
${STUDENT_FEEDBACK}
--- KONEC ZPĚTNÉ VAZBY ---

Přečti si aktuální stav souboru docs/reseni/${RESENI_ID}.html.

Z pozice zkušeného grafika navrhni:

1. **Kde chybí obrázek nebo graf** — Projdi kroky řešení všech 14 úloh. U kterých by přidání vizuálu výrazně pomohlo pochopení? Pro každý návrh uveď:
   - Číslo úlohy a konkrétní krok
   - Typ vizuálu (schéma, diagram, nákres, tabulka)
   - Co přesně má vizuál zobrazovat
   - Proč to pomůže žákovi pochopit řešení

2. **Stávající tabulky a schémata** — Jsou existující tabulky (sol-table) přehledné? Navrhni vylepšení barev, popisků, zvýraznění klíčových hodnot.

3. **Vizuální postup řešení** — U kterých úloh by pomohl „vizuální průvodce" kroky (šipky, čísla v kroužcích, barevné zvýraznění mezivýsledků)?

4. **Technické doporučení** — Jaký formát vizuálu je nejvhodnější (inline SVG, CSS diagram, emoji schéma)? Jak zajistit čitelnost na mobilu i při tisku?

Buď konkrétní — u každého návrhu popiš CO nakreslit, ne jen „přidej obrázek". Max 500 slov.
PROMPT

  "$CLAUDE_BIN" -p \
    --system-prompt "Jsi zkušený autor grafů a ilustrací pro didaktické materiály CERMAT s 10 lety praxe. Tvoříš obrázky, schémata, diagramy a grafy pro přijímací testy MA5 na víceletá gymnázia. Výborně znáš, jak vizualizovat matematické koncepty pro žáky 5. třídy — používáš jasné barvy, velké popisky, jednoduché tvary a minimální text. Víš, že správný obrázek dokáže vysvětlit víc než odstavec textu. Tvé vizuály jsou přehledné, barevně konzistentní a fungují jak na obrazovce, tak při tisku na papír." \
    --allowedTools "Read,Glob" \
    < "$PROMPT4" > "$GRAFIK_FILE" 2>&1
  rm -f "$PROMPT4"

  ok "Grafik dokončil návrhy."
  echo ""
  cat "$GRAFIK_FILE"
fi

# =============================================================================
# REŽIM: PRŮVODCE TYPY ÚLOH
# =============================================================================
if [[ "$MODE" == "pruvodce" ]]; then
  banner "PIPELINE: pruvodce-${PRUVODCE_ID} — ${PRUVODCE_NAME} (průvodce typy úloh)"

  # AGENT 1: UČITEL — kontroluje správnost principů a pedagogický jazyk
  banner "AGENT 1 — UČITEL MATEMATIKY (správnost principů)"
  step "Spouštím učitelského agenta..."

  "$CLAUDE_BIN" -p \
    --system-prompt "Jsi zkušený učitel matematiky na 1. stupni základní školy s 15 lety praxe. Specializuješ se na přípravu žáků 5. třídy na přijímací zkoušky MA5. Nikdy nepoužíváš rovnice ani algebru — vše vysvětluješ logicky. Dbáš na to, aby žák pochopil PROČ." \
    --allowedTools "Read,Edit,Glob" \
    --permission-mode acceptEdits \
    "Přečti soubor docs/pruvodce/${PRUVODCE_ID}.html — průvodce typy úloh pro test ${PRUVODCE_NAME}.

Dokument obsahuje karty pro každý typ úlohy v testu. Každá karta popisuje:
- Typ / název problému
- Princip řešení (kroky)
- Ilustrativní příklad (abstraktní)
- Varování před nejčastější chybou

Jako zkušený učitel:
1. Zkontroluj, zda jsou PRINCIPY matematicky správné a pedagogicky vhodné pro 5. třídu
2. Zkontroluj, zda každá karta mapuje na správnou úlohu v testu
3. Uprav nebo doplň maximálně 3–4 karty, kde:
   - Princip je příliš abstraktní nebo používá nevhodný jazyk
   - Chybí důležitý krok v postupu
   - Varování nezachycuje nejčastější chybu žáků
4. NEMĚŇ HTML strukturu, třídy ani CSS
5. Výsledky konkrétního testu NEUVÁDĚT — průvodce je bez výsledků

Na konci napiš shrnutí (max 200 slov): co jsi upravil/a a proč." \
    > "$TEACHER_FILE" 2>&1

  ok "Učitel dokončil kontrolu."
  echo ""
  cat "$TEACHER_FILE"

  # DIALOG: UČITEL ↔ ŽÁK — iterativní zpřesňování průvodce
  banner "DIALOG — UČITEL ↔ ŽÁK (${DIALOG_ROUNDS} kola)"
  run_dialog \
    "Přečti si soubor docs/pruvodce/${PRUVODCE_ID}.html — průvodce typy úloh pro test ${PRUVODCE_NAME}." \
    "pruvodce-${PRUVODCE_ID} — ${PRUVODCE_NAME}" \
    "Jsi zkušený učitel matematiky s 15 lety praxe. Připravuješ žáky 5. třídy na MA5. Nikdy nepoužíváš rovnice ani algebru. Dostáváš konkrétní zpětnou vazbu od žáka a upravuješ POUZE principy a kroky, která jsou nejasná — cíleně a konkrétně."

  # AGENT 2: ŽÁK — testuje, zda průvodce opravdu pomáhá před testem
  banner "AGENT 2 — ŽÁK 5. TŘÍDY (testuje použitelnost průvodce)"
  step "Spouštím žákovského agenta..."

  TEACHER_SUMMARY=$(cat "$TEACHER_FILE")
  PROMPT2=$(mktemp)
  cat > "$PROMPT2" <<PROMPT
Přečti soubor docs/pruvodce/${PRUVODCE_ID}.html — průvodce typy úloh pro test ${PRUVODCE_NAME}.

Učitel průvodce upravil. Tady je jeho shrnutí:
--- SHRNUTÍ UČITELE ---
${TEACHER_SUMMARY}
--- KONEC SHRNUTÍ ---

Přečti si průvodce celý a odpověz jako žák 5. třídy, který si ho čte PŘED začátkem kontrolního testu:

1. **Které karty ti dávaly smysl** — u kterých typů úloh víš po přečtení, jak postupovat?
2. **Kde ses zasekl/a** — které karty jsou matoucí, příliš složité nebo neúplné?
3. **Chybí ti nějaký typ úlohy?** — přijde ti, že průvodce pokrývá vše, nebo na něco zapomněl?
4. **Nejlepší karta** — která je nejjasnější a proč?
5. **Co bys změnil/a** — jak by se ti průvodce lépe četl?
6. **Hodnocení** — jak moc ti průvodce pomůže před testem? (1 = výborně, 5 = vůbec)

Piš neformálně, upřímně.
PROMPT

  "$CLAUDE_BIN" -p \
    --system-prompt "Jsi žák nebo žákyně 5. třídy, 11 let. Připravuješ se na přijímací zkoušky MA5. Čteš průvodce PŘED testem — chceš si rychle připomenout, jak na každý typ úlohy. Nemáš rád/a nudné texty. Odpovídáš upřímně." \
    --allowedTools "Read" \
    < "$PROMPT2" > "$STUDENT_FILE" 2>&1
  rm -f "$PROMPT2"

  ok "Žák dokončil hodnocení."
  echo ""
  cat "$STUDENT_FILE"

  # AGENT 3: CERMAT — odborná kontrola správnosti a úplnosti
  banner "AGENT 3 — PRACOVNÍK CERMAT (správnost a úplnost)"
  step "Spouštím CERMAT agenta..."

  TEACHER_SUMMARY=$(cat "$TEACHER_FILE")
  STUDENT_FEEDBACK=$(cat "$STUDENT_FILE")
  PROMPT3=$(mktemp)
  cat > "$PROMPT3" <<PROMPT
Posud průvodce typy úloh pro přijímací test MA5: ${PRUVODCE_NAME}.

Soubor: docs/pruvodce/${PRUVODCE_ID}.html

Shrnutí učitele:
--- SHRNUTÍ UČITELE ---
${TEACHER_SUMMARY}
--- KONEC SHRNUTÍ ---

Zpětná vazba žáka:
--- ZPĚTNÁ VAZBA ŽÁKA ---
${STUDENT_FEEDBACK}
--- KONEC ZPĚTNÉ VAZBY ---

Přečti soubor docs/pruvodce/${PRUVODCE_ID}.html.

Z pozice pracovníka CERMAT posud:

1. **Správnost principů** — jsou popsané postupy matematicky správné? Odpovídají typům úloh v testu MA5?
2. **Úplnost pokrytí** — pokrývá průvodce všechny typy úloh, které se v daném testu vyskytují? Co chybí?
3. **Pedagogická vhodnost** — jsou principy vysvětleny bez rovnic a algebry, přístupně pro 5. třídu?
4. **Přesnost varování** — zachycují varování skutečně nejčastější chyby žáků v MA5 testech?
5. **Konkrétní doporučení** — co přesně upravit?

Max 400 slov.
PROMPT

  "$CLAUDE_BIN" -p \
    --system-prompt "Jsi zkušený odborný pracovník CERMAT s 10 lety zkušeností s MA5 testy. Hodnotíš didaktické přípravné materiály odborně a konkrétně." \
    --allowedTools "Read" \
    < "$PROMPT3" 2>&1 | tee -a "$REPORT_FILE.cermat_tmp"
  rm -f "$PROMPT3"

  CERMAT_REPORT=$(cat "$REPORT_FILE.cermat_tmp" 2>/dev/null || echo "")

  # AGENT 4: GRAFIK — navrhuje vizuální vylepšení průvodce
  banner "AGENT 4 — GRAFIK CERMAT (vizuální vylepšení průvodce)"
  step "Spouštím grafického agenta..."

  TEACHER_SUMMARY=$(cat "$TEACHER_FILE")
  STUDENT_FEEDBACK=$(cat "$STUDENT_FILE")
  PROMPT4=$(mktemp)
  cat > "$PROMPT4" <<PROMPT
Posud vizuální stránku průvodce typy úloh pro test MA5: ${PRUVODCE_NAME}.

Soubor: docs/pruvodce/${PRUVODCE_ID}.html

Přečti si soubor docs/pruvodce/${PRUVODCE_ID}.html.

Shrnutí učitele:
--- SHRNUTÍ UČITELE ---
${TEACHER_SUMMARY}
--- KONEC SHRNUTÍ ---

Zpětná vazba žáka:
--- ZPĚTNÁ VAZBA ŽÁKA ---
${STUDENT_FEEDBACK}
--- KONEC ZPĚTNÉ VAZBY ---

Z pozice grafika navrhni:

1. **Kde by vizuál pomohl pochopit princip** — u kterých karet by malý SVG nákres / diagram / schéma okamžitě vysvětlil princip lépe než text? Pro každý návrh uveď:
   - Číslo karty / typ úlohy
   - Co přesně nakreslit (ne jen „přidej obrázek")
   - Proč to pomůže žákovi

2. **Čitelnost a přehlednost karet** — jsou karty vizuálně přehledné? Co zlepšit v barvách, struktuře, délce textu?

3. **Tiskový formát** — průvodce je čten před testem, možná i vytisknutý. Je vhodný pro tisk? Co zlepšit?

4. **Prioritní návrhy** — seřaď návrhy od nejdůležitějšího po méně důležité.

Max 400 slov.
PROMPT

  "$CLAUDE_BIN" -p \
    --system-prompt "Jsi zkušený grafik CERMAT tvořící přehledné didaktické materiály pro žáky 5. třídy. Víš, že správný jednoduchý obrázek vysvětlí víc než odstavec textu." \
    --allowedTools "Read,Glob" \
    < "$PROMPT4" > "$GRAFIK_FILE" 2>&1
  rm -f "$PROMPT4"

  ok "Grafik dokončil návrhy."
  echo ""
  cat "$GRAFIK_FILE"
fi

if [[ "$MODE" == "pruvodce_po" ]]; then
  banner "PIPELINE: pruvodce_po-${PRUVODCE_PO_ID} — ${PRUVODCE_PO_NAME} (průvodce po testu)"

  # AGENT 1: UČITEL — kontroluje, zda nápovědy vedou ke správnému postupu
  banner "AGENT 1 — UČITEL MATEMATIKY (správnost nápověd)"
  step "Spouštím učitelského agenta..."

  "$CLAUDE_BIN" -p \
    --system-prompt "Jsi zkušený učitel matematiky na 1. stupni základní školy s 15 lety praxe. Specializuješ se na přípravu žáků 5. třídy na přijímací zkoušky MA5. Nikdy nepoužíváš rovnice ani algebru — vše vysvětluješ logicky, pomocí dílků, skupinek, záměny a nákresu." \
    --allowedTools "Read,Edit,Glob" \
    --permission-mode acceptEdits \
    "Přečti soubor docs/pruvodce_po/${PRUVODCE_PO_ID}.html — průvodce PO testu pro ${PRUVODCE_PO_NAME}.

Přečti také vzorové řešení docs/reseni/${PRUVODCE_PO_ID}.html — to je referenční postup pro žáka 5. třídy.

Dokument pruvodce_po obsahuje pro každou úlohu konkrétní nápovědu:
- Uvádí čísla ze zadání
- Naznačuje další krok výpočtu (NE výsledek)
- Vede žáka přesně tou metodou, jakou používá vzorové řešení

Jako zkušený učitel zkontroluj a oprav:
1. Shoduje se metoda v nápovědě s metodou ve vzorovém řešení? (dílky, skupinky, záměna, NSN listing…)
2. Je nápověda formulována bez algebry, přístupně pro 5. třídu?
3. Nezradí nápověda výsledek — zastaví se těsně před ním?
4. Jsou čísla v nápovědách správně převzata ze zadání?
5. Uprav maximálně 3–4 místa, kde je nápověda zavádějící, příliš algebraická nebo kde metoda neodpovídá řešení.
6. NEMĚŇ HTML strukturu, třídy ani CSS.

Na konci napiš shrnutí (max 200 slov): co jsi upravil/a a proč." \
    > "$TEACHER_FILE" 2>&1

  ok "Učitel dokončil kontrolu."
  echo ""
  cat "$TEACHER_FILE"

  # DIALOG: UČITEL ↔ ŽÁK — iterativní zpřesňování nápověd
  banner "DIALOG — UČITEL ↔ ŽÁK (${DIALOG_ROUNDS} kola)"
  run_dialog \
    "Přečti si soubor docs/pruvodce_po/${PRUVODCE_PO_ID}.html — průvodce po testu pro ${PRUVODCE_PO_NAME}." \
    "pruvodce_po-${PRUVODCE_PO_ID} — ${PRUVODCE_PO_NAME}" \
    "Jsi zkušený učitel matematiky s 15 lety praxe. Připravuješ žáky 5. třídy na MA5. Nikdy nepoužíváš rovnice ani algebru. Dostáváš konkrétní zpětnou vazbu od žáka a upravuješ POUZE nápovědy, která jsou nejasná — cíleně a konkrétně."

  # AGENT 2: ŽÁK — testuje, zda nápovědy skutečně pomáhají dokončit úlohy
  banner "AGENT 2 — ŽÁK 5. TŘÍDY (testuje použitelnost nápověd)"
  step "Spouštím žákovského agenta..."

  TEACHER_SUMMARY=$(cat "$TEACHER_FILE")
  PROMPT2=$(mktemp)
  cat > "$PROMPT2" <<PROMPT
Přečti soubor docs/pruvodce_po/${PRUVODCE_PO_ID}.html — průvodce po testu pro ${PRUVODCE_PO_NAME}.

Učitel nápovědy zkontroloval. Shrnutí:
--- SHRNUTÍ UČITELE ---
${TEACHER_SUMMARY}
--- KONEC SHRNUTÍ ---

Přečti si průvodce_po celý a odpověz jako žák 5. třídy, který právě odevzdal test a kouká se do tohoto dokumentu, aby dopočítal úlohy, kde se zasekl:

1. **Které nápovědy mi okamžitě pomohly** — po přečtení jsem věděl/a, co spočítat?
2. **Kde nápověda nestačila** — příliš vágní, stále nevím jak dál?
3. **Kde nápověda prozradila příliš mnoho** — skoro řekla výsledek?
4. **Nejlepší nápověda** — která je nejlepší a proč?
5. **Co bys změnil/a** — jak by nápovědy mohly být lepší?
6. **Hodnocení** — jak moc ti průvodce_po pomohl dokončit nevypracované úlohy? (1 = výborně, 5 = vůbec)

Piš neformálně, upřímně.
PROMPT

  "$CLAUDE_BIN" -p \
    --system-prompt "Jsi žák nebo žákyně 5. třídy, 11 let. Právě jsi odevzdal/a test a teď koukáš do průvodce PO testu, aby ses pokusil/a dopočítat úlohy, kde jsi se zasekl/a. Nejsi si jistý/á výsledky — nápovědy potřebuješ konkrétní, ale ne takové, aby ti rovnou řekly odpověď." \
    --allowedTools "Read" \
    < "$PROMPT2" > "$STUDENT_FILE" 2>&1
  rm -f "$PROMPT2"

  ok "Žák dokončil hodnocení."
  echo ""
  cat "$STUDENT_FILE"

  # AGENT 3: CERMAT — odborná kontrola správnosti nápověd
  banner "AGENT 3 — PRACOVNÍK CERMAT (správnost a pedagogická vhodnost)"
  step "Spouštím CERMAT agenta..."

  TEACHER_SUMMARY=$(cat "$TEACHER_FILE")
  STUDENT_FEEDBACK=$(cat "$STUDENT_FILE")
  PROMPT3=$(mktemp)
  cat > "$PROMPT3" <<PROMPT
Posud průvodce PO testu (pruvodce_po) pro přijímací test MA5: ${PRUVODCE_PO_NAME}.

Soubor: docs/pruvodce_po/${PRUVODCE_PO_ID}.html
Vzorové řešení (referenční postup): docs/reseni/${PRUVODCE_PO_ID}.html

Shrnutí učitele:
--- SHRNUTÍ UČITELE ---
${TEACHER_SUMMARY}
--- KONEC SHRNUTÍ ---

Zpětná vazba žáka:
--- ZPĚTNÁ VAZBA ŽÁKA ---
${STUDENT_FEEDBACK}
--- KONEC ZPĚTNÉ VAZBY ---

Přečti soubor docs/pruvodce_po/${PRUVODCE_PO_ID}.html a vzorové řešení.

Z pozice pracovníka CERMAT posud:

1. **Shoda s vzorovým řešením** — odpovídají metody v nápovědách metodám ve vzorovém řešení (dílky, skupinky, záměna, NSN…)? Kde je nesoulad?
2. **Pedagogická přiměřenost** — jsou nápovědy bez algebry, vhodné pro 5. třídu?
3. **Rovnováha hint/answer** — zastavuje se nápověda těsně před výsledkem? Nebo prozrazuje příliš / příliš málo?
4. **Úplnost** — je každá úloha 1–14 pokryta nápovědou?
5. **Konkrétní doporučení** — seřazená prioritou.

Max 400 slov.
PROMPT

  "$CLAUDE_BIN" -p \
    --system-prompt "Jsi zkušený odborný pracovník CERMAT s 10 lety zkušeností s MA5 testy. Hodnotíš didaktické přípravné materiály odborně a konkrétně. Znáš typické chyby žáků 5. třídy." \
    --allowedTools "Read" \
    < "$PROMPT3" 2>&1 | tee -a "$REPORT_FILE.cermat_tmp"
  rm -f "$PROMPT3"

  CERMAT_REPORT=$(cat "$REPORT_FILE.cermat_tmp" 2>/dev/null || echo "")

  # AGENT 4: GRAFIK — navrhuje vizuální vylepšení pruvodce_po
  banner "AGENT 4 — GRAFIK CERMAT (vizuální vylepšení)"
  step "Spouštím grafického agenta..."

  TEACHER_SUMMARY=$(cat "$TEACHER_FILE")
  STUDENT_FEEDBACK=$(cat "$STUDENT_FILE")
  PROMPT4=$(mktemp)
  cat > "$PROMPT4" <<PROMPT
Posud vizuální stránku průvodce PO testu pro MA5: ${PRUVODCE_PO_NAME}.

Soubor: docs/pruvodce_po/${PRUVODCE_PO_ID}.html

Přečti si soubor docs/pruvodce_po/${PRUVODCE_PO_ID}.html.

Shrnutí učitele:
--- SHRNUTÍ UČITELE ---
${TEACHER_SUMMARY}
--- KONEC SHRNUTÍ ---

Zpětná vazba žáka:
--- ZPĚTNÁ VAZBA ŽÁKA ---
${STUDENT_FEEDBACK}
--- KONEC ZPĚTNÉ VAZBY ---

Z pozice grafika navrhni:

1. **Kde by vizuál pomohl** — u kterých úloh by malý SVG diagram / schéma / scaffold okamžitě vysvětlil nápovědu lépe než text?
   - Číslo úlohy, co přesně nakreslit, proč to pomůže

2. **Čitelnost scaffold polí** — jsou prázdná políčka (blanks) pro doplnění dostatečně viditelná a přehledná?

3. **Rozlišení nudge/scaffold/zadání** — pozná žák vizuálně, co je zadání, co je nápověda a co je scaffold pro výpočet?

4. **Prioritní návrhy** — od nejdůležitějšího.

Max 350 slov.
PROMPT

  "$CLAUDE_BIN" -p \
    --system-prompt "Jsi zkušený grafik CERMAT tvořící přehledné didaktické materiály pro žáky 5. třídy. Věříš, že dobré vizuální rozlišení typů bloků (zadání / nápověda / scaffold) je klíčové pro použitelnost dokumentu." \
    --allowedTools "Read,Glob" \
    < "$PROMPT4" > "$GRAFIK_FILE" 2>&1
  rm -f "$PROMPT4"

  ok "Grafik dokončil návrhy."
  echo ""
  cat "$GRAFIK_FILE"
fi

# =============================================================================
# REŽIM: STRÁNKA V docs/pages/ (strategie35, ...)
# =============================================================================
if [[ "$MODE" == "page" ]]; then
  banner "PIPELINE: ${PAGE_ID} — ${PAGE_NAME}"

  # AGENT 1: UČITEL MATEMATIKY — kontroluje obsah a vylepšuje vysvětlení
  banner "AGENT 1 — UČITEL MATEMATIKY (vylepšuje příklady a strategie)"
  step "Spouštím učitelského agenta..."

  "$CLAUDE_BIN" -p \
    --system-prompt "Jsi zkušený učitel matematiky na 1. stupni základní školy s 15 lety praxe. Specializuješ se na přípravu žáků 5. třídy na přijímací zkoušky MA5 na víceletá gymnázia. Používáš vizuální metody, konkrétní příklady z každodenního života a postup krok za krokem. Nikdy nepoužíváš rovnice ani algebru — vše vysvětluješ logicky a graficky. Dbáš na to, aby žák pochopil PROČ, nejen JAK. Mluvíš jazykem přátelským pro 11leté dítě." \
    --allowedTools "Read,Edit,Glob" \
    --permission-mode acceptEdits \
    "Přečti soubor ${PAGE_FILE} — pracovní list '${PAGE_NAME}'.

Dokument obsahuje sekce pro jednotlivé typy úloh. Každá sekce má:
- Oranžový box s příkladem z reálného testu (div.ukazka)
- Zelenou strategii (div.strategy)
- Krokové řešení (div.steps s div.step)
- Výsledek (div.answer) a varování (div.warn)

Jako zkušený učitel matematiky vylepši obsah pro žáka 5. třídy:

1. Prostuduj všechny sekce (typy úloh)
2. Vyber 2–3 sekce, kde lze pedagogicky vylepšit strategii nebo kroky řešení
3. Uprav je přímo v HTML souboru nástrojem Edit:
   - Doplň přirovnání z každodenního života (peníze, jablka, délky...)
   - Přidej mezikrok tam, kde žák přeskočí příliš velký myšlenkový skok
   - Zjednodušš jazyk — žádná slova jako 'eliminace', 'substituce', 'soustava'
   - Uprav varování (div.warn) tak, aby zachytilo skutečnou nejčastější chybu
4. NEMĚŇ výsledky, správné odpovědi ani HTML strukturu (třídy, tagy, CSS)
5. Zachovej <span class=\"calc\"> pro výpočty

Na konci napiš stručné shrnutí (max 300 slov):
- Které sekce jsi upravil/a (název + co)
- Co konkrétně jsi přidal/a a proč
- Jak to pomůže žákovi lépe pochopit daný typ úlohy" \
    > "$TEACHER_FILE" 2>&1

  ok "Učitel dokončil úpravy."
  echo ""
  cat "$TEACHER_FILE"

  # DIALOG: UČITEL ↔ ŽÁK
  banner "DIALOG — UČITEL ↔ ŽÁK (${DIALOG_ROUNDS} kola)"
  run_dialog \
    "Přečti si soubor ${PAGE_FILE} — pracovní list '${PAGE_NAME}'." \
    "${PAGE_ID} — ${PAGE_NAME}" \
    "Jsi zkušený učitel matematiky s 15 lety praxe. Připravuješ žáky 5. třídy na MA5. Nikdy nepoužíváš rovnice ani algebru. Dostáváš konkrétní zpětnou vazbu od žáka a upravuješ POUZE místa, která jsou nejasná — cíleně a konkrétně."

  # AGENT 2: ŽÁK 5. TŘÍDY — testuje srozumitelnost
  banner "AGENT 2 — ŽÁK 5. TŘÍDY (testuje srozumitelnost)"
  step "Spouštím žákovského agenta..."

  TEACHER_SUMMARY=$(cat "$TEACHER_FILE")
  PROMPT2=$(mktemp)
  cat > "$PROMPT2" <<PROMPT
Přečti soubor ${PAGE_FILE} — pracovní list '${PAGE_NAME}'.

Učitel pracovní list právě upravil. Tady je jeho shrnutí:
--- SHRNUTÍ UČITELE ---
${TEACHER_SUMMARY}
--- KONEC SHRNUTÍ ---

Přečti si celý dokument a odpověz jako žák 5. třídy, který se připravuje na přijímací zkoušky:

1. **Které strategie ti byly jasné** — u kterých typů úloh víš po přečtení, co dělat?
2. **Kde ses zasekl/a** — které kroky nebo strategie ti nedávají smysl? Buď konkrétní.
3. **Nejlepší příklad** — který vzorový příklad ti pomohl nejvíc a proč?
4. **Nejtěžší typ** — který typ úlohy stále nechápáš i po přečtení?
5. **Co bys změnil/a** — jak by se ti pracovní list lépe studoval?
6. **Hodnocení** — jak moc ti tento list pomůže u zkoušky? (1 = výborně, 5 = vůbec)

Piš neformálně a upřímně.
PROMPT

  "$CLAUDE_BIN" -p \
    --system-prompt "Jsi žák nebo žákyně 5. třídy základní školy, je ti 11 let. Připravuješ se na přijímací zkoušky na víceleté gymnázium. Matematiku celkem zvládáš, ale někdy se zasekneš u složitějšího zadání. Nemáš rád/a nudné texty plné odborných slov. Chceš jasné, rychlé vysvětlení s příklady. Odpovídáš upřímně a neformálně — jako skutečný žák, ne jako dospělý." \
    --allowedTools "Read" \
    < "$PROMPT2" > "$STUDENT_FILE" 2>&1
  rm -f "$PROMPT2"

  ok "Žák dokončil hodnocení."
  echo ""
  cat "$STUDENT_FILE"

  # AGENT 3: PRACOVNÍK CERMAT — ověřuje správnost a úplnost
  banner "AGENT 3 — PRACOVNÍK CERMAT (správnost, úplnost, didaktika)"
  step "Spouštím CERMAT agenta..."

  TEACHER_SUMMARY=$(cat "$TEACHER_FILE")
  STUDENT_FEEDBACK=$(cat "$STUDENT_FILE")
  PROMPT3=$(mktemp)
  cat > "$PROMPT3" <<PROMPT
Posud didaktický pracovní list '${PAGE_NAME}' pro přípravu na přijímací zkoušky MA5.

Soubor: ${PAGE_FILE}

Učitel upravil obsah:
--- SHRNUTÍ UČITELE ---
${TEACHER_SUMMARY}
--- KONEC SHRNUTÍ ---

Zpětná vazba žáka 5. třídy:
--- ZPĚTNÁ VAZBA ŽÁKA ---
${STUDENT_FEEDBACK}
--- KONEC ZPĚTNÉ VAZBY ---

Přečti si aktuální stav souboru ${PAGE_FILE}.

Z pozice pracovníka CERMAT posud:

1. **Správnost výsledků a postupů** — jsou vzorová řešení matematicky správná? Jsou výpočty v krocích bezchybné?
2. **Soulad s testovými úlohami** — odpovídají popsané strategie skutečným typům úloh v MA5? Chybí důležitý typ?
3. **Pedagogická vhodnost** — jsou postupy bez algebry a rovnic, přístupné pro 5. třídu?
4. **Gradace obtížnosti** — je přechod od jednoduchého ke složitějšímu vhodný?
5. **Konkrétní doporučení** — co přesně opravit nebo doplnit? Cituj konkrétní pasáže.

Buď konkrétní a konstruktivní. Max 500 slov.
PROMPT

  "$CLAUDE_BIN" -p \
    --system-prompt "Jsi zkušený odborný pracovník Centra pro zjišťování výsledků vzdělávání (CERMAT) s 10 lety zkušeností. Podílel/a ses na tvorbě a hodnocení didaktických testů MA5 pro přijímací zkoušky na víceletá gymnázia. Výborně znáš požadavky na matematické kompetence žáků 5. třídy, typické chyby v testech a způsoby, jak na ně žáky připravit. Hodnotíš didaktické materiály odborně, konstruktivně a konkrétně." \
    --allowedTools "Read" \
    < "$PROMPT3" 2>&1 | tee -a "$REPORT_FILE.cermat_tmp"
  rm -f "$PROMPT3"

  CERMAT_REPORT=$(cat "$REPORT_FILE.cermat_tmp" 2>/dev/null || echo "")

  # AGENT 4: GRAFIK CERMAT — navrhuje vizuální doplnění
  banner "AGENT 4 — GRAFIK CERMAT (navrhuje vizuální doplnění)"
  step "Spouštím grafického agenta..."

  TEACHER_SUMMARY=$(cat "$TEACHER_FILE")
  STUDENT_FEEDBACK=$(cat "$STUDENT_FILE")
  PROMPT4=$(mktemp)
  cat > "$PROMPT4" <<PROMPT
Posud vizuální stránku pracovního listu '${PAGE_NAME}' pro MA5.

Soubor: ${PAGE_FILE}

Shrnutí učitele:
--- SHRNUTÍ UČITELE ---
${TEACHER_SUMMARY}
--- KONEC SHRNUTÍ ---

Zpětná vazba žáka:
--- ZPĚTNÁ VAZBA ŽÁKA ---
${STUDENT_FEEDBACK}
--- KONEC ZPĚTNÉ VAZBY ---

Přečti si soubor ${PAGE_FILE}.

Z pozice zkušeného grafika navrhni:

1. **Kde chybí vizuál** — u kterých typů úloh by SVG diagram, tabulka nebo schéma pomohlo pochopit strategii lépe než text? Pro každý návrh uveď:
   - Název sekce (typ úlohy)
   - Typ vizuálu (schéma, diagram, tabulka, nákres)
   - Co přesně má vizuál zobrazovat
   - Proč to pomůže žákovi

2. **Stávající SVG a tabulky** — jsou přehledné, správně popsané, čitelné na mobilu i tisku?

3. **Vizuální průvodce strategií** — navrhni 1–2 místa, kde by krátký „krokovník" (3–4 rámečky se šipkami) vizuálně znázornil postup řešení.

4. **Technické doporučení** — formát vizuálu (inline SVG, CSS), čitelnost na mobilu i tisku.

Buď konkrétní. Max 500 slov.
PROMPT

  "$CLAUDE_BIN" -p \
    --system-prompt "Jsi zkušený autor grafů a ilustrací pro didaktické materiály CERMAT s 10 lety praxe. Tvoříš obrázky, schémata, diagramy a grafy pro přijímací testy MA5 na víceletá gymnázia. Výborně znáš, jak vizualizovat matematické koncepty pro žáky 5. třídy — používáš jasné barvy, velké popisky, jednoduché tvary a minimální text. Víš, že správný obrázek dokáže vysvětlit víc než odstavec textu. Tvé vizuály jsou přehledné, barevně konzistentní a fungují jak na obrazovce, tak při tisku na papír." \
    --allowedTools "Read,Glob" \
    < "$PROMPT4" > "$GRAFIK_FILE" 2>&1
  rm -f "$PROMPT4"

  ok "Grafik dokončil návrhy."
  echo ""
  cat "$GRAFIK_FILE"
fi

# =============================================================================
# VÝSTUPNÍ REPORT
# =============================================================================
banner "VÝSTUPNÍ REPORT"

if [[ "$MODE" == "pl" ]]; then
  REPORT_TITLE="${PL_ID} — ${PL_NAME}"
elif [[ "$MODE" == "pruvodce" ]]; then
  REPORT_TITLE="pruvodce-${PRUVODCE_ID} — ${PRUVODCE_NAME} (průvodce typy úloh)"
elif [[ "$MODE" == "pruvodce_po" ]]; then
  REPORT_TITLE="pruvodce_po-${PRUVODCE_PO_ID} — ${PRUVODCE_PO_NAME} (průvodce po testu)"
elif [[ "$MODE" == "page" ]]; then
  REPORT_TITLE="${PAGE_ID} — ${PAGE_NAME}"
else
  REPORT_TITLE="${RESENI_ID} — ${RESENI_NAME} (vzorové řešení)"
fi

CERMAT_REPORT=$(cat "$REPORT_FILE.cermat_tmp" 2>/dev/null || echo "")
GRAFIK_REPORT=$(cat "$GRAFIK_FILE" 2>/dev/null || echo "")

DIALOG_REPORT=$(cat "$DIALOG_FILE" 2>/dev/null || echo "")

cat > "$REPORT_FILE" << HEREDOC
# Revize a korektury: ${REPORT_TITLE}
Datum: $(date '+%d. %m. %Y %H:%M')

---

## Agent 1 — Učitel matematiky: Co bylo upraveno

$(cat "$TEACHER_FILE")

---

## Dialog — Učitel ↔ Žák (${DIALOG_ROUNDS} kola)

${DIALOG_REPORT}

---

## Agent 2 — Žák 5. třídy: Zpětná vazba

$(cat "$STUDENT_FILE")

---

## Agent 3 — Pracovník CERMAT: Doporučení

${CERMAT_REPORT}

---

## Agent 4 — Grafik CERMAT: Vizuální návrhy

${GRAFIK_REPORT}

---
*Vygenerováno revize.sh*
HEREDOC

# úklid dočasných souborů
rm -f "$TEACHER_FILE" "$STUDENT_FILE" "$GRAFIK_FILE" "$DIALOG_FILE" "$REPORT_FILE.cermat_tmp"

ok "Report uložen: $REPORT_FILE"
banner "REVIZE DOKONČENA"
