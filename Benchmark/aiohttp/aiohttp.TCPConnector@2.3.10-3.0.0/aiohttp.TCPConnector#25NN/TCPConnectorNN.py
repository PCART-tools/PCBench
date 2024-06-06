import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    connector = aiohttp.TCPConnector(resolver=None, ssl_context=None, fingerprint=None, ttl_dns_cache=10, keepalive_timeout=30, use_dns_cache=True, family=0, verify_ssl=True, resolve=object(), local_addr=None)
    async with aiohttp.ClientSession(connector=connector) as session:
        html = await fetch(session, 'http://httpbin.org/get')
        print(html)
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
