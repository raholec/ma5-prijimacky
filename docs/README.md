# MA5 Přijímačky — Příprava na osmileté gymnázium

Pracovní listy pro přípravu žáků 5. třídy na přijímací zkoušky z matematiky na osmileté gymnázium.  
Úlohy vycházejí ze zadání státních přijímaček (MA5) z let **2023–2025**.

## 🌐 Web

**→ [Otevřít online](https://GITHUB_USERNAME.github.io/ma5-prijimacky/)**

## 📁 Obsah

| Pracovní list | Téma | Body v testu |
|---|---|---|
| PL05 | Soustavy podmínek | 18 bodů (36 %) |
| PL07 | Výrazy a závorky | 8 bodů (16 %) |
| PL01 | Geometrická konstrukce | 6 bodů (12 %) |
| PL03 | Posloupnosti a vzory | 5 bodů (10 %) |
| PL04 | Grafy — pravdivé / nepravdivé | 4 body (8 %) |
| PL02 | Prostorová představivost | 4 body (8 %) |
| PL06 | Obvod a obsah | 4 body (8 %) |
| PL08 | Jednotky a převody | 4 body (8 %) |

## 🗂️ Struktura projektu

```
ma5-prijimacky/
├── index.html              ← Hlavní stránka
├── pages/                  ← Procvičovací listy (HTML)
│   ├── PL01_Geometricka_konstrukce.html
│   ├── PL02_Prostorova_predstavivost.html
│   ├── PL03_Posloupnosti_a_vzory.html
│   ├── PL04_Grafy_pravdive_nepravdive.html
│   ├── PL05_Soustavy_podminek.html
│   ├── PL06_Obvod_a_obsah.html
│   ├── PL07_Vyrazy_a_zavorky.html
│   └── PL08_Jednotky_a_prevody.html
├── pdfs/                   ← PDF k tisku
│   ├── PL01_Geometricka_konstrukce.pdf
│   └── ... (8 PDF souborů)
└── README.md
```

## 🚀 Jak publikovat na GitHub Pages

### 1. Vytvoř GitHub účet a nové repozitory

1. Jdi na [github.com](https://github.com) a přihlas se (nebo si vytvoř účet)
2. Klikni na **"+"** → **"New repository"**
3. Název: `ma5-prijimacky`
4. Nastav jako **Public**
5. **Neklikej** na "Add README" (soubor už máme)
6. Klikni **"Create repository"**

### 2. Nahraj soubory

GitHub nabídne instrukce — použij jednu z variant:

#### Varianta A — přes webový prohlížeč (nejjednodušší)

1. Na stránce repozitory klikni **"uploading an existing file"**
2. Přetáhni **všechny soubory a složky** (index.html, README.md, složku pages/, složku pdfs/)
3. Dole vyplň zprávu např. `první verze` a klikni **"Commit changes"**

#### Varianta B — přes příkazový řádek (Git)

```bash
# Ve složce s projektem:
git init
git add .
git commit -m "první verze pracovních listů"
git branch -M main
git remote add origin https://github.com/TVOJE_JMENO/ma5-prijimacky.git
git push -u origin main
```

### 3. Zapni GitHub Pages

1. V repozitory jdi do **Settings** (ozubené kolečko)
2. V levém menu klikni **"Pages"**
3. Pod "Branch" vyber **main** a složku **/ (root)**
4. Klikni **"Save"**

Za 1–2 minuty bude web dostupný na adrese:  
`https://TVOJE_JMENO.github.io/ma5-prijimacky/`

### 4. Aktualizace (přidání nebo změna souborů)

Přes web: na stránce repozitory klikni na soubor → tužka (Edit) nebo nahraj nové soubory.  
Přes Git: `git add . && git commit -m "popis změn" && git push`

---

## 📖 Zdroje

Zadání státních přijímaček jsou volně dostupná na [statniprijimacky.cz](https://www.statniprijimacky.cz).  
Autorská práva zadání © CZVV (Centrum pro zjišťování výsledků vzdělávání).  
Tento projekt je výhradně pro studijní účely.
