from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
    <h1='CENTRE'><b>LIST OF PROTOCOLS</b></h1>
        <h2>NAME:AKASH P<br> 
            REF NO: 24900264</h2>

    <title>TCP/IP Protocol Suite</title>
</head>
<body>
    <h1>TCP/IP Protocol Suite</h1>
    <ul>
        <li>HTTP</li>
        <li>FTP</li>
        <li>SMTP</li>
        <li>DNS</li>
        <li>Telnet</li>
        <li>SNMP</li>
    </ul>
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