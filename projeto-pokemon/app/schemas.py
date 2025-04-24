
from pydantic import BaseModel

class PokemonBase(BaseModel):
    id: int
    name: str
    url: str
    base_experience: int | None = None
    height: int | None = None
    weight: int | None = None
    types: str | None = None
    sprite_url: str | None = None
    abilities: str | None = None
    forms: str | None = None
    games: str | None = None
    
    class Config:
        orm_mode = True
