import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    connector = aiohttp.TCPConnector(family=0, local_addr=None, ssl_context=None, resolve=object(), fingerprint=None, use_dns_cache=True, ttl_dns_cache=10, verify_ssl=True)
    async with aiohttp.ClientSession(connector=connector) as session:
        html = await fetch(session, 'http://httpbin.org/get')
        print(html)
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
