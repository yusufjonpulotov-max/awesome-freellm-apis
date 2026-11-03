# -*- coding: utf-8 -*-
"""Сервери соддаи боргирӣ бо сарлавҳаҳои дурусти .docx."""
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
ROOT = os.path.dirname(os.path.abspath(__file__))


class H(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def guess_type(self, path):
        if path.lower().endswith(".docx"):
            return DOCX
        return super().guess_type(path)

    def send_head(self):
        path = self.translate_path(self.path)
        if path.lower().endswith(".docx") and os.path.isfile(path):
            name = os.path.basename(path)
            try:
                f = open(path, "rb")
            except OSError:
                self.send_error(404, "File not found")
                return None
            size = os.path.getsize(path)
            self.send_response(200)
            self.send_header("Content-Type", DOCX)
            self.send_header("Content-Disposition", 'attachment; filename="%s"' % name)
            self.send_header("Content-Length", str(size))
            self.end_headers()
            return f
        return super().send_head()

    def log_message(self, fmt, *args):
        print("%s - %s" % (self.address_string(), fmt % args), flush=True)


if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 8080), H).serve_forever()
