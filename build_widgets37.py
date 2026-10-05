#!/usr/bin/env python3
"""Build simple-elegant-gentleman widget CSS: production (-obs) + preview variants."""
from pathlib import Path

ROOT = Path(__file__).parent / "widgets"
ACCENT = "#d9b878"
BORDER = "#d9b87880"
DARK = "#15191dee"

BASE = f"""html,body{{overflow:hidden!important;margin:0;padding:0;background:transparent}}
.card,.subathon-container,#ms_container,#__next>div{{background:{DARK}!important;border:1px solid {BORDER}!important;border-radius:12px!important;box-shadow:0 8px 24px #0006!important;color:#f8f6f0!important;font-family:'DM Sans',sans-serif!important;overflow:hidden!important}}
.sub_judul,.sub_judul strong,.card-header,#__next>div>.chakra-heading{{font-family:'Playfair Display',serif!important;color:{ACCENT}!important;font-size:22px!important;letter-spacing:1px!important;text-shadow:0 2px 8px #0009!important;border-bottom:1px solid {BORDER}!important;padding-bottom:8px!important;margin-bottom:12px!important;display:block!important}}
"""

MS_VIDEO = f"""#ms_container .media-container{{display:flex!important;flex-direction:column!important;align-items:center!important;gap:12px!important;margin:0!important;padding:0!important;width:100%!important;text-align:center!important}}
#ms_container .media-container iframe.media,#ms_container .video-preview,#ms_container .thumbnail{{width:min(880px,96%,calc((100vh - 215px) * 16 / 9))!important;height:auto!important;aspect-ratio:16/9!important;max-width:100%!important;min-height:0!important;margin:14px auto 0!important;border:1px solid {BORDER}!important;border-radius:12px!important;overflow:hidden!important;background:#000!important;box-shadow:0 0 18px #d9b87840!important;display:block!important}}
#ms_container .loadingbar{{display:block!important;position:relative;z-index:6;width:min(880px,96%,calc((100vh - 215px) * 16 / 9))!important;max-width:100%!important;height:5px!important;margin:12px auto 14px!important;background:#000000b8!important;border:1px solid {BORDER}!important;border-radius:999px!important;opacity:1!important;visibility:visible!important;overflow:hidden}}
#ms_container .loadingbar svg path:first-child{{stroke:#0000!important}}
#ms_container .loadingbar svg path:last-child{{stroke:{ACCENT}!important;filter:drop-shadow(0 0 5px {ACCENT})!important}}
.style-1.text-container,#sender,#nominal,#message{{display:block!important;visibility:visible!important;opacity:1!important}}
#ms_container .wrapper.hide,#ms_container.hide,#ms_container .hide{{opacity:0!important;visibility:hidden!important}}
@media(max-height:260px){{#ms_container{{padding:10px!important}}#ms_container .media-container iframe.media,#ms_container .video-preview,#ms_container .thumbnail{{min-height:90px!important;height:110px!important;aspect-ratio:auto!important}}}}
"""

MS_TEXT = f""".media-container,.video-preview,video{{display:none!important}}
#ms_container .loadingbar{{display:block!important;position:relative;z-index:6;width:min(460px,90%)!important;height:5px!important;margin:16px auto 8px!important;background:#000000b8!important;border:1px solid {BORDER}!important;border-radius:999px!important;opacity:1!important;visibility:visible!important;overflow:hidden}}
#ms_container .loadingbar svg path:first-child{{stroke:#0000!important}}
#ms_container .loadingbar svg path:last-child{{stroke:{ACCENT}!important;filter:drop-shadow(0 0 6px {ACCENT})!important}}
.style-1.text-container,#sender,#nominal,#message{{display:block!important;visibility:visible!important;opacity:1!important}}
#ms_container .wrapper.hide,#ms_container.hide,#ms_container .hide{{opacity:0!important;visibility:hidden!important}}
"""

TOP = f""".show_donate{{table-layout:fixed!important;width:100%!important;border-collapse:separate!important;border-spacing:0 5px!important}}
.show_donate td{{vertical-align:middle!important;padding:7px 8px!important}}
.show_donate td:first-child{{width:32px!important;text-align:center!important;color:{ACCENT}!important;font-weight:bold!important}}
.show_donate td:nth-child(2){{width:auto!important}}
.show_donate td:last-child{{width:42%!important;max-width:42%!important;text-align:right!important}}
.show_donate .text-limit{{overflow:visible!important;text-overflow:clip!important;white-space:normal!important;word-break:break-word!important;line-height:1.25!important;text-align:left!important}}
.show_donate .text-limit-r{{font-size:12.5px!important;line-height:1.25!important;color:{ACCENT}!important}}
"""

SUBATHON = """.sub_timer{display:flex!important;justify-content:center!important;flex-wrap:nowrap!important;line-height:1!important;gap:10px!important}
.sub_timer span{flex:0 0 auto;white-space:nowrap;min-width:34px;font-family:'Playfair Display',serif!important;font-size:44px!important;font-weight:700!important;color:#d9b878!important;text-shadow:0 2px 10px #d9b87850!important}
"""

MILE = """.progress{height:8px!important;background:#000000a0!important;border:1px solid #d9b87850!important;border-radius:999px!important;overflow:hidden!important}
.progress-bar{background:linear-gradient(90deg,#b89b5e,#f0d49b)!important;box-shadow:0 0 10px #d9b87870!important}
"""

# Queue shares top-donator DOM for rows; milestone/queue use .card root.
VARIANTS = {
    "mediashare": MS_TEXT, "mediashare-video": MS_VIDEO,
    "top-donator": TOP, "queue": TOP, "subathon": SUBATHON, "milestone": MILE,
}

def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    count = 0
    for platform in ("sociabuzz", "saweria"):
        for widget, extra in VARIANTS.items():
            css = BASE + extra
            if platform == "saweria":
                # Saweria MediaShare root differs; keep shared text rules only.
                pass
            for suffix in ("", "-obs"):
                (ROOT / f"{platform}-{widget}{suffix}.css").write_text(css, encoding="utf-8")
                count += 1
    # No shorthand `inset:` (OBS Chromium) anywhere.
    for f in ROOT.glob("*.css"):
        assert "inset:" not in f.read_text(encoding="utf-8")
    print(f"Built {count} widget files, no inset shorthand.")

if __name__ == "__main__":
    main()
