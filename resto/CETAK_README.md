# File cetak menu (siap percetakan)

| File | Isi |
|---|---|
| `menu-sarapan/CETAK_Menu_Sarapan_SunaRi.pdf` | Menu sarapan, dengan bleed 3 mm |
| `menu-sarapan/CETAK_Menu_Sarapan_SunaRi_crop-marks.pdf` | Sama, + tanda potong (crop marks) |
| `menu-bajoy-wa/CETAK_Menu_Bajoy_Beach_Resto.pdf` | Menu Bajoy Beach Resto, dengan bleed 3 mm |
| `menu-bajoy-wa/CETAK_Menu_Bajoy_Beach_Resto_crop-marks.pdf` | Sama, + tanda potong (crop marks) |

## Spesifikasi untuk percetakan
- Ukuran jadi (trim): **180 x 320 mm** (proporsi 9:16, sama dengan desain)
- Bleed: **3 mm** tiap sisi (file 186 x 326 mm); versi crop marks 206 x 346 mm
- Teks: **vektor**, font tertanam (Playfair Display, Montserrat), tajam di ukuran berapa pun
- Logo: ±1.700–2.250 ppi pada ukuran cetak; bayangan kartu ±300 ppi
- Warna: RGB (latar krem #FBF4EC). Minta percetakan mengonversi ke CMYK dan **cetak proof dulu** untuk cek warna krem & cokelat.
- Saran bahan: art carton / fancy paper 260–310 gsm, laminasi doff, atau dimasukkan ke akrilik/menu holder.

Membuat ulang: `node resto/render_print.js` (setelah build.py masing-masing menu).
