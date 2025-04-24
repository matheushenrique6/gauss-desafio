
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Pokemon
from ..schemas import PokemonBase
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/pokemons", response_model=List[PokemonBase])
def get_pokemons(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Pokemon).offset(skip).limit(limit).all()

@router.get("/pokemons/{pokemon_id}", response_model=PokemonBase)
def get_pokemon_by_id(pokemon_id: int, db: Session = Depends(get_db)):
    pokemon = db.query(Pokemon).get(pokemon_id)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokémon não encontrado")
    return pokemon

@router.get("/letter-count")
def letter_count(letter: str, db: Session = Depends(get_db)):
    count = db.query(Pokemon).filter(Pokemon.name.like(f"{letter.lower()}%")).count()
    return {"letter": letter, "count": count}
