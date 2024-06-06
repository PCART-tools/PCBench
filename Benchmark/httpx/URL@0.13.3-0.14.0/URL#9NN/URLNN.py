import httpx
url_str = 'https://www.example.com/path/to/resource'
query_params = {'key1': 'value1', 'key2': 'value2'}
url = httpx.URL(url=url_str, allow_relative=False, params=query_params)
