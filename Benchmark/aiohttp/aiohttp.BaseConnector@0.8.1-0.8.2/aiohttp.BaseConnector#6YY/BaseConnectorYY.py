import aiohttp
connector = aiohttp.BaseConnector(reuse_timeout=30, conn_timeout=None)
