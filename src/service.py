from pathlib import Path
import time, uuid
from .prompting import build_prompt
from .backends import MockBackend, DiffusersBackend
from .config import settings
class VisualAidService:
    def __init__(self, backend=None): self.backend=backend or MockBackend()
    def generate(self, concept, audience="adult", style="calm, simple, therapeutic illustration", negative_prompt="", seed=42):
        prompt=build_prompt(concept,audience,style)
        out=Path(settings.output_dir); out.mkdir(parents=True,exist_ok=True)
        path=out/f"visual_{uuid.uuid4().hex[:10]}.png"; t=time.perf_counter()
        self.backend.generate(prompt,negative_prompt,seed,path)
        return {"image_path":str(path),"prompt":prompt,"seed":seed,"latency_ms":round((time.perf_counter()-t)*1000,2),"backend":self.backend.name}

def create_backend(kind="mock"):
    if kind=="diffusers": return DiffusersBackend(settings.model_id,settings.device)
    return MockBackend()


from dataclasses import dataclass
@dataclass
class Request:
    concept: str
    audience: str="adult"
    style: str="calm, simple, therapeutic illustration"
    negative_prompt: str=""
    seed: int=42

_original_generate=VisualAidService.generate
def _compat_generate(self, request_or_concept, *args, **kwargs):
    if isinstance(request_or_concept, Request):
        if not request_or_concept.concept.strip(): raise ValueError("concept cannot be empty")
        out=_original_generate(self, request_or_concept.concept, request_or_concept.audience, request_or_concept.style, request_or_concept.negative_prompt, request_or_concept.seed)
        import hashlib
        out["image_id"]=hashlib.sha256(out["image_path"].encode()).hexdigest()[:16]
        return out
    if isinstance(request_or_concept,str) and not request_or_concept.strip(): raise ValueError("concept cannot be empty")
    return _original_generate(self, request_or_concept, *args, **kwargs)
VisualAidService.generate=_compat_generate
