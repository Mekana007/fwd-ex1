from http.server import HTTPServer, BaseHTTPRequestHandler
content = """


<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Protocol Suite</title>
</head>
<body>

    <h2 align="center">TCP/IP Protocol Suite</h2>

    <p>
        The TCP/IP Protocol Suite is a collection of protocols
        used for communication between devices over a network.
    </p>

    <table border="1" cellpadding="8" cellspacing="0" width="100%">
        <tr>
            <th>Layer</th>
            <th>Protocol</th>
            <th>Function</th>
        </tr>

        <tr>
            <td rowspan="8">Application Layer</td>
            <td>HTTP</td>
            <td>Transfers web pages.</td>
        </tr>
        <tr><td>HTTPS</td><td>Provides secure web communication.</td></tr>
        <tr><td>FTP</td><td>Transfers files between devices.</td></tr>
        <tr><td>SMTP</td><td>Sends emails.</td></tr>
        <tr><td>DNS</td><td>Converts domain names into IP addresses.</td></tr>
        <tr><td>DHCP</td><td>Automatically assigns IP addresses.</td></tr>
        <tr><td>POP3 / IMAP</td><td>Retrieves and manages emails.</td></tr>
        <tr><td>SSH</td><td>Provides secure remote access.</td></tr>

        <tr>
            <td rowspan="3">Transport Layer</td>
            <td>TCP</td>
            <td>Ensures reliable data delivery.</td>
        </tr>
        <tr><td>UDP</td><td>Provides fast, connectionless delivery.</td></tr>
        <tr><td>SCTP</td><td>Supports multiple data streams.</td></tr>

        <tr>
            <td rowspan="4">Internet Layer</td>
            <td>IP</td>
            <td>Handles addressing and packet routing.</td>
        </tr>
        <tr><td>ICMP</td><td>Reports network errors.</td></tr>
        <tr><td>IGMP</td><td>Manages multicast groups.</td></tr>
        <tr><td>ARP</td><td>Maps IPv4 addresses to MAC addresses.</td></tr>

        <tr>
            <td rowspan="4">Network Access Layer</td>
            <td>Ethernet</td>
            <td>Supports wired communication.</td>
        </tr>
        <tr><td>Wi-Fi</td><td>Enables wireless communication.</td></tr>
        <tr><td>PPP</td><td>Connects two network devices.</td></tr>
        <tr><td>HDLC</td><td>Supports data-link transmission.</td></tr>
    </table>

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
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()