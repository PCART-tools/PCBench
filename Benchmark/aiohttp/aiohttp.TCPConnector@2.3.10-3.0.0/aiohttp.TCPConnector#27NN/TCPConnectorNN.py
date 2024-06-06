import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    connector = aiohttp.TCPConnector(limit=100, fingerprint=None, force_close=False, keepalive_timeout=30, verify_ssl=True, ttl_dns_cache=10, local_addr=None, resolver=None, family=0, resolve=object(), use_dns_cache=True, ssl_context=None)
    async with aiohttp.ClientSession(connector=connector) as session:
        html = await fetch(session, 'http://httpbin.org/get')
        print(html)
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
