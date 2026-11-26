# -*- coding: utf-8 -*-
"""Сервери оддии файлдиҳӣ барои скачат кардани кори курсӣ."""
import os
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))
FILES = {
    "/01_Hajmi-zarbavi_Kursi.docx": "01_Hajmi-zarbavi_Kursi.docx",
    "/kursi/01_Hajmi-zarbavi_Kursi.docx": "01_Hajmi-zarbavi_Kursi.docx",
}
BASE = os.path.dirname(ROOT)  # папка kursi/
DOCX = os.path.join(BASE, "01_Hajmi-zarbavi_Kursi.docx")
DOCX_NAME = "01_Hajmi-zarbavi_Kursi.docx"
MIME = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"

PAGE = """<!doctype html>
<html lang="tg"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Кори курсӣ — скачат</title>
<style>
 :root {{ color-scheme: light; }}
 body {{ margin:0; font-family: -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
        background:#f4f6f8; color:#1d2430; display:flex; min-height:100vh;
        align-items:center; justify-content:center; padding:24px; }}
 .card {{ background:#fff; max-width:640px; width:100%; border-radius:16px; padding:32px;
          box-shadow:0 10px 40px rgba(20,30,50,.12); }}
 h1 {{ font-size:22px; margin:0 0 6px; }}
 p {{ line-height:1.55; color:#43506b; font-size:15px; }}
 .btn {{ display:inline-flex; align-items:center; gap:10px; margin-top:18px;
         background:#2563eb; color:#fff; text-decoration:none; font-weight:600;
         padding:14px 22px; border-radius:12px; font-size:16px; }}
 .btn:hover {{ background:#1d4ed8; }}
 .meta {{ margin-top:22px; font-size:13px; color:#6b7a93; border-top:1px solid #e6eaf1; padding-top:16px; }}
 code {{ background:#eef2f7; padding:2px 6px; border-radius:6px; font-size:13px; }}
 .alt {{ margin-top:10px; font-size:13px; }}
 a.small {{ color:#2563eb; }}
</style></head>
<body><div class="card">
 <h1>Мавзӯи 1. Ҳаҷми зарбавӣ ва дақиқавии дил</h1>
 <p>Кори курсӣ пурра тайёр аст: 38 саҳифаи мазмун, 13 ҷадвал, 2 шакл, 22 манбаъ.
    Формати Word: A4, Times New Roman 14, байни сатрҳо 1,5.</p>
 <a class="btn" href="/download" download="{name}">⬇ Скачат кардани файли Word (.docx)</a>
 <div class="alt">Агар тугма кор накунад: <a class="small" href="/download">/download</a></div>
 <div class="meta">Номи файл: <code>{name}</code> · Ҳаҷм: {size} КБ · Навъ: Microsoft Word (.docx)</div>
</div></body></html>
"""


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def _send(self, code, body=b"", ctype="text/html; charset=utf-8", extra=None, head=False):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        if not head:
            self.wfile.write(body)

    def do_GET(self):
        self._handle(head=False)

    def do_HEAD(self):
        self._handle(head=True)

    def _handle(self, head):
        path = urllib.parse.urlparse(self.path).path
        if path in ("/", "/index.html"):
            size = round(os.path.getsize(DOCX) / 1024)
            body = PAGE.format(name=DOCX_NAME, size=size).encode("utf-8")
            return self._send(200, body, head=head)
        if path in ("/download", "/download.docx") or path in FILES:
            if not os.path.exists(DOCX):
                return self._send(404, b"file not found", head=head)
            with open(DOCX, "rb") as fh:
                data = fh.read()
            extra = {
                "Content-Disposition": 'attachment; filename="%s"; filename*=UTF-8\'\'%s'
                                       % (DOCX_NAME, DOCX_NAME),
                "X-Content-Type-Options": "nosniff",
            }
            return self._send(200, data, ctype=MIME, extra=extra, head=head)
        return self._send(404, b"not found", head=head)

    def log_message(self, fmt, *args):
        print("%s - %s" % (self.address_string(), fmt % args), flush=True)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    srv = ThreadingHTTPServer(("0.0.0.0", port), Handler)
    print("Serving %s on 0.0.0.0:%d" % (DOCX, port), flush=True)
    srv.serve_forever()
