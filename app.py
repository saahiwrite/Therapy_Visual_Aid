from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from src.schemas import GenerationRequest, GenerationResponse
from src.service import VisualAidService, create_backend
import os
app=FastAPI(title="Therapy Visual Aid Generator",version="2.0.0")
service=VisualAidService(create_backend(os.getenv("BACKEND","mock")))
@app.get("/health")
def health(): return {"status":"ok","backend":service.backend.name}
@app.post("/generate",response_model=GenerationResponse)
def generate(req:GenerationRequest):
    try: return service.generate(req.concept,req.audience,req.style,req.negative_prompt,req.seed)
    except Exception as e: raise HTTPException(status_code=500,detail=str(e))
@app.get("/images/{name}")
def image(name:str): return FileResponse(f"outputs/{name}")
