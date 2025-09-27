from fastapi import FastAPI, HTTPException, Path, Query
from schema_4 import Band, GenreChoice, Bandwithid, BandCreate
from typing import Annotated

app = FastAPI()

# Bands data
Bands = [
    {"id": 1, "name": "The Beatles", "genre": "rock", "albums": []},
    {"id": 2, "name": "Led Zeppelin", "genre": "rock", "albums": []},
    {"id": 3, "name": "Pink Floyd", "genre": "progressive rock", "albums": []},
    {"id": 4, "name": "Queen", "genre": "rock", "albums": []},
    {"id": 5, "name": "The Rolling Stones", "genre": "rock", "albums": []},
    {"id": 6, "name": "Nirvana", "genre": "grunge", "albums": []},
    {
        "id": 7,
        "name": "Metallica",
        "genre": "metal",
        "albums": [
            {"id": 1, "title": "Master of Puppets", "band_id": 7, "year": 1986},
            {"id": 2, "title": "Ride the Lightning", "band_id": 7, "year": 1984},
        ],
    },
    {"id": 8, "name": "U2", "genre": "rock", "albums": []},
]

# -------------------
# Endpoints
# -------------------

@app.get("/bands")
async def get_bands(
    genre: GenreChoice | None = None,
    q: Annotated[str | None, Query(max_length=10)] = None,
) -> list[Bandwithid]:
    
    band_list = [Bandwithid(**band) for band in Bands]

    if genre:
        band_list = [b for b in band_list if b.genre.lower() == genre.value]

    if q:
        band_list = [b for b in band_list if q.lower() in b.name.lower()]

    return band_list

# -------------------

@app.get("/bands/{band_id}")
async def band(band_id: Annotated[int, Path(title="the band id")]) -> Bandwithid:
    band_data = next((b for b in Bands if b["id"] == band_id), None)
    if band_data is None:
        raise HTTPException(status_code=404, detail="Band not found")
    return Bandwithid(**band_data)

# -------------------

@app.get("/bands/genres/{genre}")
async def get_bands_by_genre(genre: GenreChoice) -> list[Bandwithid]:
    return [Bandwithid(**b) for b in Bands if b["genre"].lower() == genre.value]

# -------------------

@app.post("/bands", response_model=Bandwithid)
async def create_band(band_data: BandCreate):
    new_id = Bands[-1]["id"] + 1
    new_band = Bandwithid(id=new_id, **band_data.model_dump())
    Bands.append(new_band.model_dump())
    return new_band
