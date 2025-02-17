from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
from http.cookies import SimpleCookie
import cgi

class WebServer(BaseHTTPRequestHandler):
    @property
    def parsed_url(self):
        return urlparse(self.path)

    @property
    def query_data(self):
        return parse_qs(self.parsed_url.query)

    def read_post_data(self):
        ctype, pdict = cgi.parse_header(self.headers.get('Content-Type'))
        content_length = self.headers.get('Content-Length')
        if ctype == 'multipart/form-data':
            if content_length:
                pdict['CONTENT-LENGTH'] = int(content_length)
            # ensure the 'boundary' byte-string is correctly formatted for Python 3
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            post_vars = cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers.get('Content-Length', 0))
            post_vars = parse_qs(self.rfile.read(length).decode('utf-8'), keep_blank_values=True)
        else:
            post_vars = {}
        return post_vars

    def cookies(self):
        if "Cookie" in self.headers:
            return SimpleCookie(self.headers["Cookie"])
        else:
            return SimpleCookie()

    def do_GET(self):
        # Set a cookie
        cookie = SimpleCookie()
        cookie["session"] = "test_session"
        cookie["session"]["path"] = "/"
        cookie["session"]["httponly"] = True
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        # Include the cookie in the response headers
        for morsel in cookie.values():
            self.send_header("Set-Cookie", morsel.OutputString())
        self.end_headers()
        message = "Cookie set!"
        self.wfile.write(message.encode("utf-8"))

    def do_POST(self):
        # Attempt to read the cookie
        cookies = self.cookies()
        session_cookie = cookies["session"].value if "session" in cookies else "No cookie"

        # Prepare the response
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        message = f"Handling POST request! Found cookie: {session_cookie}"
        self.wfile.write(message.encode("utf-8"))


# you can change the server port here in this method
def run(server_class=HTTPServer, handler_class=WebServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()