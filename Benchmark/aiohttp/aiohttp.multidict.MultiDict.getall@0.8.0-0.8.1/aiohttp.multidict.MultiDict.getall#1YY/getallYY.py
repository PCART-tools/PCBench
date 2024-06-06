from aiohttp.multidict import MultiDict
multi_dict = MultiDict([('key1', 'value1'), ('key2', 'value2'), ('key1', 'value3')])
result = multi_dict.getall('key1')
