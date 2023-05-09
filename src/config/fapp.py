import os
from importlib.util import find_spec

from django.conf import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.staticfiles import StaticFiles

from config.wsgi import application

app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/admin", WSGIMiddleware(application))
app.mount(
    "/_static",
    StaticFiles(directory=os.path.normpath(os.path.join(find_spec("django.contrib.admin").origin, "..", "static"))),
    name="static",
)


def init(fastapi: FastAPI):
    from app.routers import register_routers

    register_routers(fastapi)


init(app)
