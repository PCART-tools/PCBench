from aiohttp import web
app = web.Application()
app.router.add_static(path='./', prefix='/static/', name='static')
