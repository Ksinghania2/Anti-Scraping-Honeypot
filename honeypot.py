from http.server import BaseHTTPRequestHandler, HTTPServer

# Set to store banned bot IP addresses
BANNED_IPS = set()

class HoneyPotServer(BaseHTTPRequestHandler):
    
    def do_GET(self):
        client_ip = self.client_address[0]
        
        # 1. Security Check: If the IP is banned, deny access immediately
        if client_ip in BANNED_IPS:
            self.send_response(403) # HTTP 403 Forbidden
            self.end_headers()
            self.wfile.write(b"Access Denied: Your IP has been flagged for malicious activity.")
            return

        # 2. Honey-Pot Trap: If a bot accesses the hidden directory, trap it
        if self.path == "/hidden-admin-login-trap":
            BANNED_IPS.add(client_ip)
            print(f"[SECURITY ALERT] Malicious Bot detected from IP: {client_ip}. IP permanently banned.")
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"Trap sprung. IP banned.")
            return

        # 3. Normal Webpage Route for human users
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            
            # Simple HTML containing a normal link and the invisible bot trap link
            html_content = """
            <html>
                <body>
                    <h1>Welcome to the Secure Portal</h1>
                    <p>This is standard public text visible to users.</p>
                    
                    <a href="/hidden-admin-login-trap" style="display:none; visibility:hidden;">Admin Access</a>
                </body>
            </html>
            """
            self.wfile.write(bytes(html_content, "utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8080), HoneyPotServer)
    print("Secure Honey-Pot Server active on http://localhost:8080...")
    server.serve_forever()