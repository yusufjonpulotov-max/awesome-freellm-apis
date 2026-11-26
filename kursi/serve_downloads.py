# -*- coding: utf-8 -*-
"""Сервери оддии файлдиҳӣ барои скачат кардани корҳои курсӣ."""
import os
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

BASE = os.path.dirname(os.path.abspath(__file__))
MIME = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
PORT = int(os.environ.get("PORT", "8001"))

FILES = [
    ("01_Hajmi-zarbavi_Kursi.docx", "Мавзӯи 1. Ҳаҷми зарбавӣ ва дақиқавии дил"),
    ("02_Frank-Starling_Kursi.docx", "Мавзӯи 2. Қонуни Франк–Старлинг"),
    ("03_Koronar_Kursi.docx", "Мавзӯи 3. Гардиши хуни коронарӣ"),
    ("04_Bozgashti-venagi_Kursi.docx", "Мавзӯи 6. Бозгашти венагӣ ва омилҳои он"),
    ("05_Mubodilai-moe_Kursi.docx", "Мавзӯи 10. Мубодилаи моеъ байни капиллярҳо ва бофтаҳо"),    ("06_Surfaktanti-shush_Kursi.docx", "Мавзӯи 13. Сурфактанти шуш ва механизми таъсири он"),
    ("07_Baroreceptor_Kursi.docx", "Мавзӯи 7. Рефлекси барорецепторӣ ва танзими фишор"),
    ("08_Hemoreceptor_Kursi.docx", "Мавзӯи 8. Рефлексҳои хеморесепторӣ ва танзими нафаскашӣ"),
    ("09_Reflexi-dili_Kursi.docx", "Мавзӯи 9. Рефлексҳои дилӣ ва нақши онҳо дар танзими кори дил"),
    ("10_Mikrotsirkulyatsiya_Kursi.docx", "Мавзӯи 11. Микроциркуляция ва танзими маҳаллии ҷараёни хун"),
    ("11_Gumoral_Kursi.docx", "Мавзӯи 12. Танзими гуморалии гардиши хун"),
    ("12_Nagruzka_Kursi.docx", "Мавзӯи 14. Танзими гардиши хун ҳангоми кори ҷисмонӣ"),
    ("13_Gardishi-mayna_Kursi.docx", "Мавзӯи 15. Гардиши хуни майна ва танзими он"),
    ("14_Gurda_Kursi.docx", "Мавзӯи 16. Гардиши хуни гурда ва танзими он"),
    ("15_Jigar_Kursi.docx", "Мавзӯи 17. Гардиши хуни ҷигар ва танзими он"),
]

PAGE = """<!doctype html>
<html lang="tg"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Корҳои курсӣ — скачат</title>
<style>
 body {{ margin:0; font-family:-apple-system,"Segoe UI",Roboto,Arial,sans-serif;
        background:#f4f6f8; color:#1d2430; display:flex; min-height:100vh;
        align-items:center; justify-content:center; padding:24px; }}
 .card {{ background:#fff; max-width:680px; width:100%; border-radius:16px; padding:32px;
          box-shadow:0 10px 40px rgba(20,30,50,.12); }}
 h1 {{ font-size:22px; margin:0 0 6px; }}
 p.sub {{ color:#43506b; font-size:15px; margin:0 0 18px; }}
 .item {{ display:flex; align-items:center; justify-content:space-between; gap:16px;
          border:1px solid #e6eaf1; border-radius:12px; padding:16px; margin-bottom:12px; }}
 .item .t {{ font-size:15px; font-weight:600; }}
 .item .s {{ font-size:13px; color:#6b7a93; margin-top:4px; }}
 .btn {{ background:#2563eb; color:#fff; text-decoration:none; font-weight:600;
         padding:12px 18px; border-radius:10px; font-size:15px; white-space:nowrap; }}
 .btn:hover {{ background:#1d4ed8; }}
 .meta {{ margin-top:20px; font-size:13px; color:#6b7a93; border-top:1px solid #e6eaf1; padding-top:14px; }}
</style></head>
<body><div class="card">
 <h1>Корҳои курсӣ — физиологияи инсон</h1>
 <p class="sub">Файлҳо дар формати Word (.docx) тайёр ҳастанд. Барои скачат тугмаро зер кунед.</p>
 <p class="sub" style="font-size:13px;background:#eef2ff;border-radius:10px;padding:10px 12px">
 Агар тугмаи «Скачат» дар дохили саҳифа кор накунад, тугмаро бо зеркунии рости муш
 кушоед ва «Open link in new tab»-ро интихоб кунед. Ё файлро аз панели
 «Files» дар тарафи чап кушоед — он ҷо тугмаи скачат ҳамеша кор мекунад.</p>
 {items}
 <div class="meta">Донишкадаи илмҳои дақиқ ва технологияи Тоҷикистон дар шаҳри Хуҷанд ·
 Факултети фанҳои дақиқ ва технологияи инноватсионӣ</div>
</div></body></html>
"""

ITEM = """ <div class="item">
  <div><div class="t">{title}</div><div class="s">{name} · {size} КБ</div></div>
  <a class="btn" href="/download/{name}" target="_blank" rel="noopener">Скачат</a>
 </div>"""


def render():
    parts = []
    for name, title in FILES:
        path = os.path.join(BASE, name)
        size = round(os.path.getsize(path) / 1024) if os.path.exists(path) else 0
        parts.append(ITEM.format(title=title, name=name, size=size))
    return PAGE.format(items="\n".join(parts)).encode("utf-8")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urllib.parse.unquote(self.path.split("?")[0])
        if path in ("/", "/index.html"):
            body = render()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        name = path.rsplit("/", 1)[-1]
        allowed = {n for n, _ in FILES}
        if path.startswith("/download/") and name in allowed:
            full = os.path.join(BASE, name)
            data = open(full, "rb").read()
            self.send_response(200)
            self.send_header("Content-Type", MIME)
            ascii_name = name.encode("ascii", "ignore").decode() or "kursi.docx"
            self.send_header(
                "Content-Disposition",
                'attachment; filename="%s"; filename*=UTF-8\'\'%s'
                % (ascii_name, urllib.parse.quote(name)))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return
        self.send_error(404)

    def do_HEAD(self):
        """Браузерҳо ва проксиҳо пеш аз скачат сарлавҳаҳоро мепурсанд."""
        path = urllib.parse.unquote(self.path.split("?")[0])
        name = path.rsplit("/", 1)[-1]
        allowed = {n for n, _ in FILES}
        if path.startswith("/download/") and name in allowed:
            full = os.path.join(BASE, name)
            self.send_response(200)
            self.send_header("Content-Type", MIME)
            self.send_header("Content-Disposition", 'attachment; filename="%s"' % name)
            self.send_header("Content-Length", str(os.path.getsize(full)))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            return
        if path in ("/", "/index.html"):
            body = render()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            return
        self.send_error(404)

    def log_message(self, fmt, *args):
        pass


if __name__ == "__main__":
    srv = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print("Сервер: http://0.0.0.0:%d" % PORT)
    srv.serve_forever()
