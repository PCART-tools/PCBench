import tornado.httpclient
http_client = tornado.httpclient.AsyncHTTPClient(io_loop=None, max_clients=10, force_instance=False)
