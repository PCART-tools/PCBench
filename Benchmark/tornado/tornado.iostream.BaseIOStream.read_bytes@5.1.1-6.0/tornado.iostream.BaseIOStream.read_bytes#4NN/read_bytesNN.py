import tornado.iostream
import tornado.ioloop
import socket

async def read_bytes_from_stream():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(0)
    stream = tornado.iostream.IOStream(s)
    await stream.connect(('httpbin.org', 80))
    await stream.write(b'GET /get HTTP/1.1\r\nHost: httpbin.org\r\n\r\n')
    data = await stream.read_bytes(10, callback=None)
tornado.ioloop.IOLoop.current().run_sync(read_bytes_from_stream)
