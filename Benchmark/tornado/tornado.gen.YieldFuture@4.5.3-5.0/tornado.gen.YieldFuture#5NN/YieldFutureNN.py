import tornado.ioloop
import tornado.gen
import tornado.concurrent
future = tornado.concurrent.Future()
result = tornado.gen.YieldFuture(future=future, io_loop=None)
