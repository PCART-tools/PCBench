from aiohttp import web
app = web.Application()
app.router.add_static('/static/', expect_handler=None, path='./', name='static')
