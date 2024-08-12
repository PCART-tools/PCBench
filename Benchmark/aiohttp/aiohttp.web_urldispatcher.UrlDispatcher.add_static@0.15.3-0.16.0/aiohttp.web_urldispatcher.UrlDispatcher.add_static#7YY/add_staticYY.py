from aiohttp import web
app = web.Application()
app.router.add_static('/static/', path='./', expect_handler=None)
