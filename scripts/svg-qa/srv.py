import http.server,sys
class H(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        n=int(self.headers['Content-Length']);open(sys.argv[1] if len(sys.argv)>1 else 'audit.txt','wb').write(self.rfile.read(n))
        self.send_response(200);self.send_header('Access-Control-Allow-Origin','*');self.end_headers()
    def do_OPTIONS(self):
        self.send_response(200);self.send_header('Access-Control-Allow-Origin','*');self.send_header('Access-Control-Allow-Headers','*');self.end_headers()
    def log_message(self,*a):pass
http.server.HTTPServer(('127.0.0.1',8765),H).serve_forever()
