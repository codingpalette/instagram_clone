from typing import Optional
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from routes import user, post
from connection import Base, engine

app = FastAPI()


def create_app():
    Base.metadata.create_all(bind=engine)

    app = FastAPI(docs_url="/docs", redoc_url=None)

    origins = [
        'http://localhost:3000',
    ]

    # app.add_middleware(middleware_class=BaseHTTPMiddleware, dispatch=access_control)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    app.include_router(user.router, tags=["유저"], prefix="/api")
    app.include_router(post.router, tags=["포스트"], prefix="/api")

    return app


app = create_app()