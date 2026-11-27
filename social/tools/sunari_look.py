"""Tampilan foto seragam tema SunaRi untuk konten Hari Jadi Selayar (feed & story).
1) resep dasar social/grade_photos.py (kekuatan 0.8)
2) penyeimbang suhu warna: foto dingin (laut toska, langit biru) dihangatkan, foto senja yang terlalu panas diredam,
   sehingga semua foto mendekati satu "kehangatan" yang sama
3) lapisan pemersatu: sentuhan Sandy Shore (#E6C89B) di highlight + bayangan Driftwood Deep (#5A3E31), saturasi sedikit turun
Run: python3 social/tools/sunari_look.py"""
import pathlib
import numpy as np
from PIL import Image
ROOT = pathlib.Path(__file__).resolve().parents[2]
p = ROOT / "social" / "grade_photos.py"
g = {"__file__": str(p), "__name__": "grade"}
exec(p.read_text().split("JOBS =")[0], g)
R = g["R"]
OUT = ROOT / "social" / "hari-jadi-selayar-feed" / "foto"
TARGET = 28          # kehangatan rata-rata (R-B) yang dituju
SRCS = ["senja/85-siluet-tirai-senja-persegi-lurus.jpg", "pantai/06-nelayan-hasil-laut-kerang.jpg", "resto/06-bakar-ikan-tuna-bara.jpg",
        "bahuluang/21-laut-toska-dari-kapal.jpg", "bahuluang/29-snorkeling-masker-penuh.jpg", "bahuluang/51-pantai-barat-teluk-pasir-putih.jpg",
        "pantai/03-pulau-di-seberang.jpg", "polassi-tambolongan/07-punggung-bukit-nane-dan-teluk.jpg", "bahuluang/12-berjalan-di-pasir-timbul.jpg",
        "bahuluang/47-dalam-gua-lipang-stalaktit-rombongan.jpg", "senja/86-matahari-merah-dua-perahu.jpg", "malam/30-ayunan-kelapa-bintang.jpg",
        "taman/05-meja-taman-view-laut-gazebo.jpg"]
def warmth(a): return float((a[..., 0] - a[..., 2]).mean() * 255)
def look(src):
    g["grade"](src, "_look_tmp.jpg", 0.8)
    im = Image.open(R / "graded" / "_look_tmp.jpg").convert("RGB"); im.thumbnail((1800, 1800))
    a = np.asarray(im, float) / 255
    w = warmth(a)
    L = (0.299 * a[..., 0] + 0.587 * a[..., 1] + 0.114 * a[..., 2])[..., None]
    if w < TARGET:      # dingin -> hangatkan (foto sangat biru dihangatkan lebih kuat), sambil turunkan saturasi agar biru tidak "menyala"
        k = min((TARGET - w) / 80, 1.5)
        a = a * (1 + k * np.array([0.10, 0.02, -0.14]))
        a = L + (a - L) * (1 - min(0.30 * k, 0.45))
    elif w > TARGET + 50:   # senja terlalu panas -> redam sedikit
        k = min((w - TARGET - 50) / 120, 0.6)
        a = L + (a - L) * (1 - 0.30 * k)
    # bara/lampu magenta -> jingga: kurangi biru di piksel magenta (R & B jauh di atas G)
    m = np.clip((np.minimum(a[..., 0], a[..., 2]) - a[..., 1]) / 0.25, 0, 1)[..., None]
    a = a.copy(); a[..., 2:3] = a[..., 2:3] - m * (a[..., 2:3] - a[..., 1:2]) * 0.8
    a = np.clip(a, 0, 1); L = (0.299 * a[..., 0] + 0.587 * a[..., 1] + 0.114 * a[..., 2])[..., None]
    hi = np.clip((L - 0.55) / 0.45, 0, 1); sh = np.clip((0.35 - L) / 0.35, 0, 1)
    a = a * (1 - 0.10 * hi) + np.array([0xE6, 0xC8, 0x9B]) / 255 * 0.10 * hi     # highlight Sandy Shore
    a = a * (1 - 0.12 * sh) + np.array([0x5A, 0x3E, 0x31]) / 255 * 0.12 * sh     # bayangan Driftwood Deep
    a = L + (a - L) * 0.92                                                         # saturasi pemersatu
    out = Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8))
    out.save(OUT / src.replace("/", "__"), quality=90, optimize=True)
    return w, warmth(np.asarray(out, float) / 255)
if __name__ == "__main__":
    for s in SRCS:
        b, a = look(s); print(f"{s:60s} {b:6.0f} -> {a:6.0f}")
    (R / "graded" / "_look_tmp.jpg").unlink()
