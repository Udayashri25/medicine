from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pandas as pd
from textblob import TextBlob
from gtts import gTTS
import os

from backend.utils import (
    preprocess_text,
    load_word_vectors,
    load_medicine_data,
    suggest_medicine
)

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static directory for audio file
app.mount("/static", StaticFiles(directory="backend/static"), name="static")

# Load word vectors and data
word_vectors = load_word_vectors()
medicine_data = load_medicine_data()
medicine_images_df = pd.read_csv("medicine_images.csv")

class QueryInput(BaseModel):
    text: str
    dataset: str

@app.post("/analyze")
def analyze(query: QueryInput):
    concern = query.text.lower()
    dataset = query.dataset
    symptoms = preprocess_text(concern)
    sentiment = TextBlob(concern).sentiment.polarity
    suggestions = suggest_medicine(symptoms, concern, medicine_data[dataset], word_vectors)

    # Create voice response
    if suggestions:
        response_text = f"Based on your input, the suggested medicines are: {', '.join(suggestions)}."
    else:
        response_text = "Sorry, no medicines were found for your input."

    # Generate audio using gTTS
    tts = gTTS(text=response_text, lang="en")
    audio_path = "backend/static/response.mp3"
    os.makedirs(os.path.dirname(audio_path), exist_ok=True)
    tts.save(audio_path)

    return {
        "sentiment": sentiment,
        "medicines": suggestions,
        "audio_url": "/static/response.mp3"
    }

@app.get("/image")
def image(medicine_name: str = Query(...)):
    row = medicine_images_df.loc[
        medicine_images_df['Medicine'].str.lower() == medicine_name.lower(), 'Image URL']
    return {"url": row.iloc[0] if not row.empty else ""}
