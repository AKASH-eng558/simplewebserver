from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <body>
        <h1='CENTRE'><b>MY LAPTOP CONFIGURATION</b></h1>
        <h2>NAME:AKASH P<br> 
            REF NO: 24900264</h2>
        <ol>
        <li>Device name	AK</li>
        <li>Processor	AMD Ryzen 5 5600H with Radeon Graphics  3.30 GHz</li>         
        <li>Installed RAM	16.0 GB (15.3 GB usable)</li>
        <li>Device ID	9818DC8B-5A92-4B05-BB6D-52B14B013ABD</li>
        <li>Product ID	00342-42692-33914-AAOEM</li>
        <li>System type	64-bit operating system, x64-based processor</li>
        <li>Pen and touch	No pen or touch input is available for this display</li>
            
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()