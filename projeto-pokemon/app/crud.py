
import requests
from sqlalchemy.orm import Session
from .models import Pokemon

def populate_pokemon_data(db: Session):
    if db.query(Pokemon).count() == 0:
        response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=100")
        response.raise_for_status()
        pokemons = response.json().get("results", [])

        for p in pokemons:
            detail = requests.get(p["url"]).json()
            types = ", ".join(t["type"]["name"] for t in detail["types"])

            db.add(Pokemon(
                name=detail["name"],
                url=p["url"],
                base_experience=detail.get("base_experience"),
                height=detail.get("height"),
                weight=detail.get("weight"),
                types=types,
                sprite_url=detail["sprites"]["front_default"]
            ))

        db.commit()
