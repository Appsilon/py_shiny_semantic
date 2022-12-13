from starlette.applications import Starlette
from starlette.responses import FileResponse
from starlette.routing import Mount, Route

from apps import app_buttons


async def home(request):
    return FileResponse("static/index.html")


routes = [
    Route("/", home),
    Mount("/buttons", app=app_buttons),
]

app = Starlette(routes=routes)
