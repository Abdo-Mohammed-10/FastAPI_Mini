from fastapi import FastAPI, HTTPException
from schema_4 import Band, GenreChoice, Bandwithid, BandCreate

app = FastAPI()

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
    {"id": 9, "name": "Radiohead", "genre": "alternative rock", "albums": []},
    {"id": 10, "name": "Coldplay", "genre": "alternative rock", "albums": []},
    {"id": 11, "name": "Adele", "genre": "pop", "albums": []},
    {"id": 12, "name": "Beyoncé", "genre": "pop", "albums": []},
    {"id": 13, "name": "Taylor Swift", "genre": "pop", "albums": []},
    {"id": 14, "name": "Drake", "genre": "hip-hop", "albums": []},
    {"id": 15, "name": "Kendrick Lamar", "genre": "hip-hop", "albums": []},
    {"id": 16, "name": "Eminem", "genre": "hip-hop", "albums": []},
    {"id": 17, "name": "Miles Davis", "genre": "jazz", "albums": []},
    {"id": 18, "name": "John Coltrane", "genre": "jazz", "albums": []},
    {"id": 19, "name": "Ella Fitzgerald", "genre": "jazz", "albums": []},
    {"id": 20, "name": "Ludwig van Beethoven", "genre": "classical", "albums": []},
    {"id": 21, "name": "Wolfgang Amadeus Mozart", "genre": "classical", "albums": []},
    {"id": 22, "name": "Johann Sebastian Bach", "genre": "classical", "albums": []},
    {"id": 23, "name": "Bob Marley", "genre": "reggae", "albums": []},
    {"id": 24, "name": "Peter Tosh", "genre": "reggae", "albums": []},
    {"id": 25, "name": "Jimmy Cliff", "genre": "reggae", "albums": []},
    {"id": 26, "name": "B.B. King", "genre": "blues", "albums": []},
    {"id": 27, "name": "Muddy Waters", "genre": "blues", "albums": []},
    {"id": 28, "name": "Robert Johnson", "genre": "blues", "albums": []},
    {"id": 29, "name": "Taylor Swift", "genre": "country", "albums": []},
    {"id": 30, "name": "Johnny Cash", "genre": "country", "albums": []},
    {"id": 31, "name": "Dolly Parton", "genre": "country", "albums": []},
    {"id": 32, "name": "Daft Punk", "genre": "electronic", "albums": []},
    {"id": 33, "name": "Deadmau5", "genre": "electronic", "albums": []},
]

# -------------------
# Bands Endpoints
# -------------------

@app.get("/bands")
async def get_bands(
    genre: GenreChoice | None = None, has_albums: bool = False
) -> list[Bandwithid]:
    
    band_list = [Bandwithid(**band) for band in Bands]

    if genre:
        band_list = [b for b in band_list if b.genre.lower() == genre.value]

    if has_albums:
        band_list = [b for b in band_list if b.albums and len(b.albums) > 0]
    return band_list

# -------------------

@app.get("/bands/{band_id}")
async def band(band_id: int) -> Bandwithid:
    band = next((Bandwithid for band in Bands if band["id"] == band_id), None)
    if band is None:
        raise HTTPException(status_code=404, detail="Band not found")
    return band

# -------------------

@app.get("/bands/genres/{genre}")
async def get_bands_by_genre(genre: GenreChoice) -> list[dict]:
    return [b for b in Bands if band["genre"].lower() == genre.value]

# -------------------

@app.post("/bands", response_model=Bandwithid)
async def create_band(band_data: BandCreate):
    new_id = Bands[-1]["id"] + 1
    new_band = Bandwithid(id=new_id, **band_data.model_dump())
    Bands.append(new_band.model_dump())
    return new_band

