#!/usr/bin/env python3
"""
Лексияи «Камхуниҳои гемолитикии модарзодӣ»-ро аз Markdown ба HTML табдил медиҳад.
Истифода:  python3 build_html.py
(талаб мекунад: pip install markdown)
"""
import pathlib
import re

import markdown

HERE = pathlib.Path(__file__).parent
SRC = HERE / "kamkhunii-hemolitikii-modarzodi.md"
OUT = HERE / "kamkhunii-hemolitikii-modarzodi.html"

TITLE = "Камхуниҳои гемолитикии модарзодӣ (ирсӣ)"
SUBTITLE = "Лексияи 3-соата · Патофизиология, ташхис ва табобат"

CSS = """
:root{
  --ink:#16202b; --muted:#5b6b7c; --line:#dfe6ee; --accent:#0f6f8c;
  --accent-soft:#eaf4f8; --warn:#a8571b; --warn-soft:#fdf4e7;
  --ok:#1c6b4a; --ok-soft:#eaf6f0; --danger:#a1202b; --danger-soft:#fdeced;
  --bg:#f6f8fa; --card:#ffffff;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  margin:0; background:var(--bg); color:var(--ink);
  font-family:"Segoe UI","Noto Sans","PT Sans",Arial,sans-serif;
  font-size:16.5px; line-height:1.62;
}
.wrap{max-width:1080px;margin:0 auto;padding:28px 22px 80px}
header.hero{
  background:linear-gradient(135deg,#0f6f8c,#123b52); color:#fff;
  border-radius:16px; padding:30px 32px; margin-bottom:26px;
  box-shadow:0 10px 30px rgba(15,60,90,.18);
}
header.hero h1{margin:0 0 6px;font-size:30px;line-height:1.25}
header.hero .sub{opacity:.92;font-size:17px}
header.hero .meta{margin-top:14px;font-size:13.5px;opacity:.85}
article{
  background:var(--card); border:1px solid var(--line); border-radius:14px;
  padding:34px 38px; box-shadow:0 4px 18px rgba(20,40,60,.06);
}
h1,h2,h3,h4{line-height:1.3;font-weight:700}
h2{
  font-size:23px;margin:42px 0 14px;padding:10px 0 10px 14px;
  border-left:6px solid var(--accent);background:var(--accent-soft);
  border-radius:0 10px 10px 0;
}
h3{font-size:19.5px;margin:30px 0 10px;color:#12405a;border-bottom:1px solid var(--line);padding-bottom:6px}
h4{font-size:17px;margin:22px 0 8px;color:#1b4e69}
p{margin:10px 0}
ul,ol{margin:10px 0 10px 22px;padding:0}
li{margin:5px 0}
hr{border:0;border-top:1px solid var(--line);margin:36px 0}
a{color:var(--accent)}
code,pre{font-family:"JetBrains Mono","Consolas","Courier New",monospace}
code{background:#eef3f7;padding:1px 5px;border-radius:5px;font-size:.92em}
pre{
  background:#0f2231;color:#e8f1f7;padding:16px 18px;border-radius:12px;
  overflow:auto;font-size:13.2px;line-height:1.5;
}
pre code{background:none;color:inherit;padding:0}
table{
  border-collapse:collapse;width:100%;margin:16px 0;font-size:14.6px;
  display:table;overflow:hidden;border-radius:10px;
}
th,td{border:1px solid var(--line);padding:8px 11px;vertical-align:top;text-align:left}
th{background:#eef4f9;font-weight:700;color:#12405a}
tbody tr:nth-child(even){background:#fafcfe}
blockquote{
  margin:16px 0;padding:12px 16px;border-left:5px solid var(--accent);
  background:var(--accent-soft);border-radius:0 10px 10px 0;
}
blockquote p{margin:6px 0}
strong{color:#0d3a52}
/* ахборҳои хос */
blockquote:has(> p > strong:first-child){}
.toc{
  background:#fbfdff;border:1px solid var(--line);border-radius:12px;
  padding:16px 22px;margin:22px 0 30px;font-size:15px;
}
.toc>ul{margin-left:14px}
.toc ul{list-style:none;margin:6px 0 6px 14px}
.toc a{text-decoration:none}
.toc a:hover{text-decoration:underline}
.badge{display:inline-block;background:#fff;color:#0f6f8c;border-radius:20px;padding:2px 12px;font-size:13px;font-weight:600}
footer.note{color:var(--muted);font-size:13.5px;text-align:center;margin-top:26px}
img{max-width:100%;height:auto;display:block;margin:22px auto;border:1px solid var(--line);border-radius:12px;background:#fff;padding:6px}
p>em{display:block;text-align:center;color:var(--muted);font-size:13.6px;margin:-8px 0 22px}
@media print{
  body{background:#fff;font-size:11.5pt}
  .wrap{max-width:none;padding:0}
  header.hero{box-shadow:none;border-radius:0;padding:18px 0;background:#fff;color:#000;border-bottom:3px solid #0f6f8c}
  header.hero h1{font-size:20pt}
  article{border:0;box-shadow:none;padding:0}
  h2{background:#eaf4f8;page-break-after:avoid}
  table,pre,blockquote{page-break-inside:avoid}
  pre{background:#f2f5f8;color:#12202c}
  a{color:#000;text-decoration:none}
  @page{margin:14mm}
}
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="tg">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — лексия</title>
<style>{css}</style>
</head>
<body>
<div class="wrap">
  <header class="hero">
    <span class="badge">Лексияи академӣ</span>
    <h1>{title}</h1>
    <div class="sub">{subtitle}</div>
    <div class="meta">Мембранопатияҳо · Ферментопатияҳо (G6PD, PK) · Талассемия · Камхунии ҳуҷайраҳои досма<br>
    Ташхис ва табобат — барои донишҷӯёни тиб, 3 соати академӣ</div>
  </header>
  <article>
    {toc}
    {body}
  </article>
  <footer class="note">Маводи таълимӣ. Дар амалияи клиникӣ протоколҳои миллӣ ва дастурамалҳои расмиро истифода баред.</footer>
</div>
</body>
</html>
"""


def inline_svg_images(html: str) -> str:
    """Расмҳои SVG-ро ҳамчун data-URI ворид мекунад, то санад комилан мустақил бошад."""
    import base64

    def repl(match: "re.Match[str]") -> str:
        src = match.group(1)
        path = HERE / src
        if not path.exists():
            return match.group(0)
        data = base64.b64encode(path.read_bytes()).decode("ascii")
        return f'src="data:image/svg+xml;base64,{data}"'

    return re.sub(r'src="([^"]+?\.svg)"', repl, html)


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    # сарлавҳаи аввали санадро ба сарлавҳаи hero мегузаронем
    text = re.sub(r"\A#\s+[^\n]+\n", "", text, count=1)

    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "toc", "sane_lists", "attr_list"],
        extension_configs={"toc": {"title": "Мундариҷа", "toc_depth": "2-3"}},
    )
    body = md.convert(text)
    toc = md.toc

    html = TEMPLATE.format(title=TITLE, subtitle=SUBTITLE, css=CSS, toc=toc, body=body)
    html = inline_svg_images(html)
    OUT.write_text(html, encoding="utf-8")
    print(f"навишта шуд: {OUT} ({OUT.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
