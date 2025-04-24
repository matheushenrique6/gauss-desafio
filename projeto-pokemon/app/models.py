
from sqlalchemy import Column, Integer, String
from .database import Base

class Pokemon(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    url = Column(String)
    base_experience = Column(Integer)
    height = Column(Integer)
    weight = Column(Integer)
    types = Column(String)
    sprite_url = Column(String)
    abilities = Column(String)   
    forms = Column(String)
    games = Column(String)
    sprite_url = Column(String, nullable=True)