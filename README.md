# EX01 Developing a Simple Webserver
## Date:19-03-2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.


## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000


HTML_CONTENT = """
<!DOCTYPE html>
<html>
<head>
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


class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(HTML_CONTENT.encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer(("", PORT), CustomHandler)
    print(f"Server started at http://localhost:{PORT}")
    server.serve_forever()
```


## OUTPUT:
![alt text](<Screenshot (5).png>)
![alt text](<Screenshot (4).png>)



## RESULT:
The program for implementing simple webserver is executed successfully.
