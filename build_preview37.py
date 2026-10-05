#!/usr/bin/env python3
"""Build preview page: alerts + widget dummy DOM matching production markup."""
from pathlib import Path

ROOT = Path(__file__).parent

def css(path):
    return (ROOT / path).read_text(encoding="utf-8")

def alert_html(platform):
    """Inline full alert (HTML + external CSS) inside an iframe-friendly box."""
    inner = (ROOT / f"{platform}-alert.html").read_text(encoding="utf-8")
    style = css(f"{platform}-alert.css")
    # Replace tokens with dummy data
    inner = inner.replace('{amount}', 'Rp 50.000').replace('{donator}', 'Sample Donator').replace('{supporter}', 'Sample Supporter').replace('{from_text}', 'dari').replace('{message}', 'Terima kasih atas dukungannya!')
    return inner.replace("</html>", f"<style>{style}</style></html>")

PREVIEW = """<!doctype html><html lang="id"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Preview - Simple Elegant Gentleman</title><style>
body{margin:0;padding:28px;background:#0d1013;color:#eee;font:15px/1.5 system-ui}
h1{font:600 24px/1.2 Georgia,serif;color:#d9b878;text-align:center;margin:0 0 4px}
h1+p{text-align:center;color:#9aa;margin:0 0 26px}
h2{font:600 14px/1 system-ui;letter-spacing:2px;text-transform:uppercase;color:#d9b878;margin:30px 0 12px}
.frame{border:0;display:block;border-radius:14px;background:#15191d;margin:0 auto}
.w{background:#15191dee;border:1px solid #d9b87880;border-radius:12px;padding:16px;color:#f8f6f0}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:14px}
.sub_timer{display:flex;justify-content:center;gap:10px;flex-wrap:nowrap}
.sub_timer span{font:700 44px/1 Georgia,serif;color:#d9b878;min-width:34px;text-align:center}
table.show_donate{width:100%;border-collapse:separate;border-spacing:0 5px;table-layout:fixed}
td{padding:7px 8px;vertical-align:middle}td:first-child{width:32px;text-align:center;color:#d9b878;font-weight:700}
td:last-child{width:42%;text-align:right;color:#d9b878}
.progress{height:8px;background:#000000a0;border:1px solid #d9b87850;border-radius:999px;overflow:hidden}
.progress-bar{height:100%;width:64%;background:linear-gradient(90deg,#b89b5e,#f0d49b)}
</style></head><body>
<h1>Simple Elegant Gentleman</h1><p>Theme 37 - Sociabuzz &amp; Saweria custom alert + widgets</p>

<h2>Alert Sociabuzz</h2>
<iframe class="frame" width="560" height="150" scrolling="no" srcdoc="__SB__"></iframe>
<h2>Alert Saweria</h2>
<iframe class="frame" width="560" height="150" scrolling="no" srcdoc="__SW__"></iframe>

<h2>Widget preview (dummy production DOM)</h2>
<div class="grid">
  <div class="w"><div class="sub_judul"><strong>Subathon Timer</strong></div>
    <div class="sub_timer"><span>0</span><span>2</span><span>:</span><span>3</span><span>4</span><span>:</span><span>5</span><span>6</span></div></div>
  <div class="w"><div class="card-header">Leaderboard</div>
    <table class="show_donate"><tr><td>1</td><td class="text-limit">Mas Ajie Panjang Banget Namanya</td><td class="text-limit text-limit-r">Rp 500.000</td></tr>
    <tr><td>2</td><td class="text-limit">Sri Wahyuni</td><td class="text-limit text-limit-r">Rp 250.000</td></tr></table></div>
  <div class="w"><div class="card-header">Target Donasi</div>
    <div class="progress"><div class="progress-bar"></div></div></div>
  <div class="w"><div class="card-header">Antrean Mabar</div>
    <table class="show_donate"><tr><td>1</td><td class="text-limit">Budi</td><td class="text-limit text-limit-r">VIP</td></tr></table></div>
</div>
</body></html>"""

def main():
    html = (PREVIEW
            .replace("__SB__", alert_html("sociabuzz").replace('"', "&quot;"))
            .replace("__SW__", alert_html("saweria").replace('"', "&quot;")))
    out = ROOT / "preview-simple-elegant-gentleman.html"
    out.write_text(html, encoding="utf-8")
    assert "__SB__" not in html and "__SW__" not in html
    print(f"Built {out.name} ({out.stat().st_size} bytes)")

if __name__ == "__main__":
    main()
