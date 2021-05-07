import uvicorn
from starlette.applications import Starlette
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles


def serve():
    routes = [Mount("/", app=StaticFiles(directory="dist"), name="static")]
    app = Starlette(debug=True, routes=routes)
    uvicorn.run(app, host="localhost", port=5600)
