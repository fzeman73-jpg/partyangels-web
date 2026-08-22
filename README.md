# partyangels.cz

Statický web Party Angels. Bez frameworku, bez build kroku — čisté HTML, CSS a ~30 řádků JS.

## Struktura

```
index.html            úvodní stránka
kontakt/index.html    /kontakt/
404.html              chybová stránka
assets/css/style.css  veškerý styl
assets/js/site.js     sticky hlavička + mobilní menu
assets/img/           obrázky (webp + jpg/png fallback, 3 velikosti)
assets/fonts/         Metropolis (woff2)
CNAME                 vlastní doména pro GitHub Pages
```

## Provoz

GitHub Pages, větev `main`, kořen repozitáře. Soubor `.nojekyll` vypíná Jekyll.

## Úpravy textu

Texty jsou přímo v HTML. Změna = editace souboru, commit, do minuty je to živé.

## Obrázky

Zdrojové soubory v plném rozlišení jsou ve složce `_source/` (mimo web).
Varianty se generují skriptem `tools/build-images.py`.
