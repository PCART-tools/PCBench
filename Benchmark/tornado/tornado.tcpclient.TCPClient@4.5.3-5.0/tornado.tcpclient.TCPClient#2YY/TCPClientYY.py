import tornado.ioloop
import tornado.tcpclient
import tornado.gen

@tornado.gen.coroutine
def connect_to_host():
    client = tornado.tcpclient.TCPClient(None)
    stream = (yield client.connect('example.com', 80))
    yield stream.write(b'GET / HTTP/1.0\r\n\r\n')
    data = (yield stream.read_until(b'\r\n\r\n'))
    stream.close()
io_loop = tornado.ioloop.IOLoop.current()
io_loop.run_sync(connect_to_host)
