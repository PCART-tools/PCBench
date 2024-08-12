from aiohttp import web
app = web.Application()
app.router.add_static(prefix='/static/', name='static', path='./', expect_handler=None)
