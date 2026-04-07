# MA5 Prijimacky

## Repozitar
```
docs/          <- GitHub Pages (Settings>Pages>/docs)
  index.html, pages/PL01-08.html, pdfs/PL01-08.pdf
zadani_pdf/    <- PDF zadani 2015-2025
zadani_txt/    <- OCR texty (20r1 ... 25r2)
gen_html.py    <- generator (python3 gen_html.py)
hints_data.py  <- hinty, SVG, kvizy
quiz_backup.py <- kvizy (exec() v hints_data.py)
```

## Konvence zadani_txt
zadani_txt/{YY}{r|n}{N}/{page}.txt
Priklad: zadani_txt/25r1/9.txt = 2025, 1.radny, str9 (uloha 13)

## Technika
- hints_data.py: f-stringy, {calc_row()} inline
- PDF ZIP-based: zipfile.ZipFile(pdf).extractall(dir)

## Pedagogika
- Zak 5.tridy, bez rovnic, vizualni metody
- Posledni hint = Nejcastejsi chyby (tabulka)

Verze 7. 4. 2026