#!/usr/bin/env python3
"""Build compact Sociabuzz and Saweria alert assets."""
from pathlib import Path

ROOT = Path(__file__).parent
BASE = "https://raw.githubusercontent.com/MasAjie12/simple-elegant-gentleman-alert-assets/main"
COMMON = f"""@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=DM+Sans:wght@400;600&display=swap');
*{{box-sizing:border-box}}html,body{{margin:0;width:560px;height:150px;overflow:hidden;background:transparent}}
.card{{--gold:#d9b878;position:relative;isolation:isolate;display:flex;align-items:center;justify-content:center;width:560px;height:150px;overflow:hidden;border:1px solid #d9b87888;border-radius:14px;background:linear-gradient(110deg,#15191de8,#24282be8 48%,#15191de8),url('{BASE}/bg.jpg') center 46%/cover;color:#f8f6f0;box-shadow:0 12px 36px #0006;animation:arrive .65s cubic-bezier(.2,.75,.25,1) both}}
.card:before{{content:"";position:absolute;top:7px;left:7px;right:7px;bottom:7px;border:1px solid #d9b87835;border-radius:9px;pointer-events:none}}
.token{{position:relative;z-index:2;width:330px;text-align:center;padding:5px 0;text-shadow:0 2px 8px #0009}}
.amount{{font:700 28px/1.1 'Playfair Display',serif;color:#f0d49b;letter-spacing:.4px;animation:glow 3s ease-in-out infinite}}
.meta{{margin-top:4px;font:600 12px/1.3 'DM Sans',sans-serif;letter-spacing:2px;text-transform:uppercase;color:#e4d5bb}}
.name{{margin-top:3px;font:600 22px/1.2 'Playfair Display',serif;color:#fff}}
.message{{margin:5px auto 0;max-width:300px;font:400 12px/1.4 'DM Sans',sans-serif;color:#e6e2dc;white-space:pre-wrap;overflow-wrap:anywhere}}
.chibi{{position:absolute;z-index:3;bottom:-3px;width:88px;height:132px;background:url('{BASE}/chibi.png') center bottom/contain no-repeat;pointer-events:none;animation:rise .7s cubic-bezier(.2,.8,.2,1) both,hover 4s ease-in-out .7s infinite}}
.left{{left:7px;transform-origin:bottom left}}.right{{right:7px;transform-origin:bottom right;animation-name:rise-right,hover-right}}
@keyframes arrive{{from{{opacity:0;transform:translateY(16px) scale(.98)}}to{{opacity:1;transform:translateY(0) scale(1)}}}}
@keyframes glow{{50%{{text-shadow:0 0 13px #d9b87870}}}}
@keyframes rise{{from{{opacity:0;transform:translate(-12px,14px)}}to{{opacity:1;transform:translate(0,0)}}}}
@keyframes rise-right{{from{{opacity:0;transform:translate(-12px,14px)}}to{{opacity:1;transform:translate(0,0)}}}}
@keyframes hover{{50%{{transform:translateY(-3px)}}}}
@keyframes hover-right{{50%{{transform:translateY(-3px)}}}}
@media(prefers-reduced-motion:reduce){{*,*:before{{animation-duration:.01ms!important;animation-iteration-count:1!important}}}}
"""

def html(platform):
    if platform == "sociabuzz":
        fields = '<div class="amount">{amount}</div><div class="meta">{from_text}</div><div class="name">{supporter}</div><div class="message">{message}</div>'
    else:
        fields = '<div class="amount">{amount}</div><div class="name">{donator}</div><div class="message">{message}</div>'
    return f'<!doctype html><html lang="id"><meta charset="utf-8"><div class="card"><div class="chibi left"></div><div class="token">{fields}</div><div class="chibi right"></div></div></html>'

def main():
    for platform in ("sociabuzz", "saweria"):
        (ROOT / f"{platform}-alert.html").write_text(html(platform), encoding="utf-8")
        (ROOT / f"{platform}-alert.css").write_text(COMMON, encoding="utf-8")
    assert len(html("sociabuzz")) < 1000 and len(html("saweria")) < 1000
    print("Built two alerts with external CSS and live GitHub assets.")

if __name__ == "__main__":
    main()
