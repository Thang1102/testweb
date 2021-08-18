import SimpleHTTPServer
import SocketServer


PORT = 8082

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_POST(self):
      content_len = int(self.headers.getheader('content-length', 0))
      post_body = self.rfile.read(content_len)
      file_down = open("Orc.jpg","w")
      file_down.write(post_body)
      file_down.close()

      

Handler = ServerHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
