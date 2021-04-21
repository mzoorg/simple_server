import time
from http.server import HTTPServer, BaseHTTPRequestHandler

HOST_NAME = '127.0.0.1'
PORT_NUMBER = 53210


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        if s.path.strip('/?') == 'ping':
            s.wfile.write(b"Pong")
        else:
            s.wfile.write(b"Please send ping.")


if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))