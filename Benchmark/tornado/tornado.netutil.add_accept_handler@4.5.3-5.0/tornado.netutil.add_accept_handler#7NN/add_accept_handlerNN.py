import tornado.ioloop
import tornado.netutil
import socket

def accept_handler(connection, address):
    print('New connection:', address)
    connection.close()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
tornado.netutil.add_accept_handler(sock=sock, callback=accept_handler, io_loop=None)
