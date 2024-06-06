import tornado.escape
value_to_escape = 'hello world'
escaped_value = tornado.escape.url_escape(value_to_escape)
print(escaped_value)
