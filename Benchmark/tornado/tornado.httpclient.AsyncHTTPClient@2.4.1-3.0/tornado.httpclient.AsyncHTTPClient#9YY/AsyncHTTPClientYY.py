import tornado.httpclient
http_client = tornado.httpclient.AsyncHTTPClient(None, max_clients=10, force_instance=False)
