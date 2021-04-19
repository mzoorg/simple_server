import socket
import time
from http.server import HTTPServer, BaseHTTPRequestHandler

HOST_NAME = '127.0.0.1' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 53210 # Maybe set this to 9000.


class MyHandler(BaseHTTPRequestHandler):
    # def do_HEAD(s):
    #     s.send_response(200)
    #     s.send_header("Content-type", "text/html")
    #     s.end_headers()

    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        if s.path.strip('/?') == 'ping':
            s.wfile.write(b"Pong")
        else:
            s.wfile.write(b"Please send ping.")
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".


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