from fastapi import FastAPI, HTTPException
from enum import Enum

app = FastAPI()

# Genre Enum (values lowercase for case-insensitive matching)
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

# Bands data (genre in lowercase for consistency)
Bands = [
    {"id": 1, "name": "The Beatles", "genre": "rock"},
    {"id": 2, "name": "Led Zeppelin", "genre": "rock"},
    {"id": 3, "name": "Pink Floyd", "genre": "progressive rock"},
    {"id": 4, "name": "Queen", "genre": "rock"},
    {"id": 5, "name": "The Rolling Stones", "genre": "rock"},
    {"id": 6, "name": "Nirvana", "genre": "grunge"},
    {"id": 7, "name": "Metallica", "genre": "metal"},
    {"id": 8, "name": "U2", "genre": "rock"},
    {"id": 9, "name": "Radiohead", "genre": "alternative rock"},
    {"id": 10, "name": "Coldplay", "genre": "alternative rock"},
    {"id": 11, "name": "Adele", "genre": "pop"},
    {"id": 12, "name": "Beyoncé", "genre": "pop"},
    {"id": 13, "name": "Taylor Swift", "genre": "pop"},
    {"id": 14, "name": "Drake", "genre": "hip-hop"},
    {"id": 15, "name": "Kendrick Lamar", "genre": "hip-hop"},
    {"id": 16, "name": "Eminem", "genre": "hip-hop"},
    {"id": 17, "name": "Miles Davis", "genre": "jazz"},
    {"id": 18, "name": "John Coltrane", "genre": "jazz"},
    {"id": 19, "name": "Ella Fitzgerald", "genre": "jazz"},
    {"id": 20, "name": "Ludwig van Beethoven", "genre": "classical"},
    {"id": 21, "name": "Wolfgang Amadeus Mozart", "genre": "classical"},
    {"id": 22, "name": "Johann Sebastian Bach", "genre": "classical"},
    {"id": 23, "name": "Bob Marley", "genre": "reggae"},
    {"id": 24, "name": "Peter Tosh", "genre": "reggae"},
    {"id": 25, "name": "Jimmy Cliff", "genre": "reggae"},
    {"id": 26, "name": "B.B. King", "genre": "blues"},
    {"id": 27, "name": "Muddy Waters", "genre": "blues"},
    {"id": 28, "name": "Robert Johnson", "genre": "blues"},
    {"id": 29, "name": "Taylor Swift", "genre": "country"},
    {"id": 30, "name": "Johnny Cash", "genre": "country"},
    {"id": 31, "name": "Dolly Parton", "genre": "country"},
    {"id": 32, "name": "Daft Punk", "genre": "electronic"},
    {"id": 33, "name": "Deadmau5", "genre": "electronic"},
]

# -------------------
# Bands Endpoints
# -------------------

@app.get('/bands', summary="Get all bands", description="Returns a list of all bands.")
async def get_bands():
    return Bands

@app.get('/bands/{band_id}', summary="Get band by ID", description="Returns a band by its ID.")
async def get_band(band_id: int):
    band = next((b for b in Bands if b["id"] == band_id), None)
    if not band:
        raise HTTPException(status_code=404, detail="Band not found")
    return band

@app.get('/bands/name/{band_name}', summary="Search bands by name", description="Search bands by partial name match (case-insensitive).")
async def get_band_by_name(band_name: str):
    matched = [b for b in Bands if band_name.lower() in b["name"].lower()]
    if not matched:
        raise HTTPException(status_code=404, detail="No bands found with this name")
    return matched

@app.get('/bands/genre/{genre_name}', summary="Get bands by genre", description="Returns bands of a specific genre (case-insensitive).")
async def get_bands_by_genre(genre_name: str):
    matched = [b for b in Bands if b["genre"].lower() == genre_name.lower()]
    if not matched:
        raise HTTPException(status_code=404, detail="No bands found for this genre")
    return matched

# -------------------
# General Endpoints
# -------------------

@app.get('/', summary="Root endpoint", description="Welcome message.")
async def root():
    return {"message": "Hello World!"}

@app.get('/status', summary="Server status", description="Returns the status of the server.")
async def status():
    return {"status": "ok"}

@app.get('/about', summary="About this API", description="Returns information about this API.")
async def about():
    return "This is a sample FastAPI application."


