"""Gera os ícones Android de cada app a partir dos ícones publicados no site.
Uso: python tools/make_icons.py          (todos os apps; precisa de Pillow e internet)
     python tools/make_icons.py canto    (só os apps informados)"""
import io, os, sys, urllib.request
from PIL import Image

APPS = {
    'bateria': 'https://josuenino33.github.io/bateria-do-zero-ao-pro/',
    'guitarra': 'https://josuenino33.github.io/guitarra-do-zero-ao-pro/',
    'treino': 'https://josuenino33.github.io/treino-em-casa-do-zero/',
    'canto': 'https://josuenino33.github.io/canto-do-zero-ao-pro/',
}
LEGACY = {'mdpi': 48, 'hdpi': 72, 'xhdpi': 96, 'xxhdpi': 144, 'xxxhdpi': 192}
ROOT = os.path.join(os.path.dirname(__file__), '..', 'app', 'src')

def get(url):
    with urllib.request.urlopen(url) as r:
        return Image.open(io.BytesIO(r.read())).convert('RGBA')

for app, base in APPS.items():
    if len(sys.argv) > 1 and app not in sys.argv[1:]:
        continue
    res = os.path.join(ROOT, app, 'res')
    anyicon = get(base + 'icons/icon-512.png')
    mask = get(base + 'icons/icon-maskable-512.png')
    # ícone clássico (Android 7 ou mais antigo)
    for d, px in LEGACY.items():
        os.makedirs(f'{res}/mipmap-{d}', exist_ok=True)
        anyicon.resize((px, px), Image.LANCZOS).save(f'{res}/mipmap-{d}/ic_launcher.png')
    # ícone adaptável (Android 8+): o ícone maskable ocupa a área visível de 72 de 108 dp
    for d, px in LEGACY.items():
        size = round(px * 108 / 48)
        inner = round(size * 72 / 108)
        canvas = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        off = (size - inner) // 2
        canvas.paste(mask.resize((inner, inner), Image.LANCZOS), (off, off))
        canvas.save(f'{res}/mipmap-{d}/ic_launcher_foreground.png')
    # cor de fundo do ícone adaptável = cor do canto do ícone maskable
    r, g, b, _ = mask.getpixel((6, 6))
    os.makedirs(f'{res}/values', exist_ok=True)
    with open(f'{res}/values/icon_colors.xml', 'w', encoding='utf-8') as f:
        f.write(f'<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <color name="iconBackground">#{r:02X}{g:02X}{b:02X}</color>\n</resources>\n')
    # imagem da tela de abertura
    os.makedirs(f'{res}/drawable-nodpi', exist_ok=True)
    anyicon.resize((384, 384), Image.LANCZOS).save(f'{res}/drawable-nodpi/splash.png')
    print(app, 'ok, fundo do ícone', f'#{r:02X}{g:02X}{b:02X}')
