import uvicorn
from starlette.applications import Starlette
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles

routes = [Mount("/", app=StaticFiles(directory="public"), name="static")]
app = Starlette(debug=True, routes=routes)


def serve():
    uvicorn.run(app, host="localhost", port=5600)
