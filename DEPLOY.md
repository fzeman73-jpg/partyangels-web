# Nasazení na GitHub Pages

## 1. Repozitář

Vytvořit prázdné repo na účtu `fzeman73-jpg`, např. `partyangels-web` (veřejné —
GitHub Pages na free účtu funguje jen z veřejného repa).

Nahrát obsah této složky do kořene repa (drag & drop ve webovém rozhraní
GitHubu nebo přes GitHub Desktop). Do repa patří i skrytý soubor `.nojekyll`.

## 2. Zapnout Pages

Settings → Pages → Source: **Deploy from a branch** → Branch `main`, složka `/ (root)` → Save.

Za minutu web běží na `https://fzeman73-jpg.github.io/partyangels-web/`.

> Pozn.: na této adrese budou obrázky a styly rozbité, protože odkazy v HTML
> vedou od kořene domény (`/assets/...`). Jakmile se připojí vlastní doména,
> vše sedí. Pokud chcete korektní náhled i na github.io, použijte repo
> pojmenované `fzeman73-jpg.github.io`.

## 3. Vlastní doména

**Než se sáhne na DNS, ověřit dvě věci:**

1. Kde je registrovaná doména `partyangels.cz`. Pokud u Webnode, převod
   k jinému registrátorovi trvá dny — začít tím.
2. Kde běží e-mail `angels@partyangels.cz`. GitHub Pages e-mail neumí.
   Přepnutím DNS bez připravených MX záznamů schránka přestane fungovat.

Postup:

1. Přejmenovat `CNAME.example` na `CNAME` a commitnout.
2. U registrátora nastavit:
   - `www` → CNAME → `fzeman73-jpg.github.io`
   - apex `partyangels.cz` → A záznamy:
     `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - MX záznamy ponechat / přesměrovat na nového poskytovatele pošty
3. Settings → Pages → Custom domain → `www.partyangels.cz` → Save
4. Počkat na ověření, pak zaškrtnout **Enforce HTTPS**

## 4. Kontrola po překlopení

- [ ] `https://www.partyangels.cz/` i `/kontakt/` se načtou
- [ ] `http://` redirectuje na `https://`
- [ ] apex `partyangels.cz` redirectuje na `www`
- [ ] e-mail `angels@partyangels.cz` chodí
- [ ] Google Search Console: odeslat `sitemap.xml`
