from pydantic import BaseModel
from enum import Enum

class GenreChoice(str, Enum):
    ROCK = "rock"
    POP = "pop"
    JAZZ = "jazz"
    CLASSICAL = "classical"
    HIPHOP = "hip-hop"
    COUNTRY = "country"
    ELECTRONIC = "electronic"
    REGGAE = "reggae"
    BLUES = "blues"
    METAL = "metal"

class Album(BaseModel):
    id: int
    title: str
    band_id: int
    year: int

class Band(BaseModel):
    id: int
    name: str
    genre: str
    albums: list[Album] | None = None   

    class Config:
        orm_mode = True
