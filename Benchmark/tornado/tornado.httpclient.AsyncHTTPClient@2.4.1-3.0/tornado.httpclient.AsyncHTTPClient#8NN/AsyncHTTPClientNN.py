import tornado.httpclient
http_client = tornado.httpclient.AsyncHTTPClient(None,  10, force_instance=False)
