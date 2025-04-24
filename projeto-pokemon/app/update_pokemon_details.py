import requests
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Pokemon

def get_details(pokemon_url):
    import requests
    res = requests.get(pokemon_url)
    if res.status_code != 200:
        return {}

    data = res.json()

    height = data.get("height", 0) / 10
    weight = data.get("weight", 0) / 10
    base_experience = data.get("base_experience", 0)

    types = ", ".join(t["type"]["name"] for t in data.get("types", []))
    abilities = ", ".join(
        f"{a['ability']['name']}{' (oculta)' if a['is_hidden'] else ''}"
        for a in data.get("abilities", [])
    )
    forms = ", ".join(f["name"] for f in data.get("forms", []))
    games = ", ".join(v["version"]["name"] for v in data.get("game_indices", []))

    sprite_url = data["sprites"]["front_default"]

    return {
        "height": height,
        "weight": weight,
        "base_experience": base_experience,
        "types": types,
        "abilities": abilities,
        "forms": forms,
        "games": games,
        "sprite_url": sprite_url,
    }


def update_pokemon_data():
    db: Session = SessionLocal()
    pokemons = db.query(Pokemon).all()
    for pokemon in pokemons:
        print(f"Atualizando {pokemon.name}...")
        details = get_details(pokemon.url)
        for key, value in details.items():
            setattr(pokemon, key, value)
        db.add(pokemon)
    db.commit()
    db.close()

if __name__ == "__main__":
    update_pokemon_data()
