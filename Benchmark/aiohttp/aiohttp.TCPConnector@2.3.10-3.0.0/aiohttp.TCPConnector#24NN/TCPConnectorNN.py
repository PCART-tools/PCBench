import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    connector = aiohttp.TCPConnector(fingerprint=None, local_addr=None, resolve=object(), verify_ssl=True, use_dns_cache=True, ttl_dns_cache=10, resolver=None, family=0, ssl_context=None)
    async with aiohttp.ClientSession(connector=connector) as session:
        html = await fetch(session, 'http://httpbin.org/get')
        print(html)
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
