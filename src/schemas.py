from pydantic import BaseModel, Field
class GenerationRequest(BaseModel):
    concept: str = Field(min_length=2, max_length=500)
    audience: str = "adult"
    style: str = "calm, simple, therapeutic illustration"
    negative_prompt: str = "text, watermark, gore, photorealistic injury"
    seed: int = 42
class GenerationResponse(BaseModel):
    image_path: str
    prompt: str
    seed: int
    latency_ms: float
    backend: str
