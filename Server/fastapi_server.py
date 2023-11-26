
import os
import io
from threading import Thread
import numpy as np
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, StreamingResponse, FileResponse
from pymongo import MongoClient
from bson.objectid import ObjectId
from generator import generate, get_conditioning_latents, load as generator_load
from translator import translate, get_languages, load as translator_load
from langdetector import detect, load as langdetector_load

app = FastAPI()

def inserttestaudio():
    audio = "/home/owen/projects/Voice Translator/Server/audio/chinese.mp3"
    audio_id = db.audios.id
    result = db.audios.insert_one({"audio_path": audio})
    db.audios.find_one({"_id": result.inserted_id})
    return str(result.inserted_id)
    

@app.get("/Generate")
async def Generate(text, audio_id, src_lang, tar_lang):
    '''Save data point and class label to database
    '''
    record = db.audios.find_one({"audio_id": audio_id})
    audio = record["audio_path"]
    translatedText, res = translate(text, src_lang, tar_lang)
    if not res:
        return
    
    gpt_cond_latent, speaker_embedding = get_conditioning_latents(audio)
    output = io.BytesIO()
    generate(translatedText, tar_lang, gpt_cond_latent, speaker_embedding, output)
    return StreamingResponse(output, media_type="audio/wav")



if __name__ == "__main__":
    # t1 = Thread(target=generator_load)
    # t1.start()
    
    # t2 = Thread(target=translator_load)
    # t2.start()
    
    # t3 = Thread(target=langdetector_load)
    # t3.start()
    
    # t1.join()
    # t2.join()
    # t3.join()
    
    client = MongoClient(serverSelectionTimeoutMS=100)
    db = client.audios
    inserttestaudio()
    uvicorn.run(app, host="0.0.0.0", port=8080)