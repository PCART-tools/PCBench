import tornado.escape
value_to_unescape = 'hello world'
unescaped_value = tornado.escape.url_unescape(value_to_unescape, encoding='utf-8')
print(unescaped_value)
