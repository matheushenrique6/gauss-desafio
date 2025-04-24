
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine, SessionLocal
from .crud import populate_pokemon_data
from .routers import pokemon as pokemon_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Preencher o banco ao iniciar (apenas se vazio)
with SessionLocal() as db:
    populate_pokemon_data(db)

app.include_router(pokemon_router.router)
