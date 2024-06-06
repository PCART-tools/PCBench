import tornado.ioloop

def my_callback():
    print('Hello, Tornado!')
tornado.ioloop.PeriodicCallback(callback=my_callback, callback_time=1000)
