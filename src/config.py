from dataclasses import dataclass
import os
@dataclass
class Settings:
    model_id: str = os.getenv("MODEL_ID", "stabilityai/sdxl-turbo")
    device: str = os.getenv("DEVICE", "cuda")
    max_prompt_chars: int = int(os.getenv("MAX_PROMPT_CHARS", "500"))
    output_dir: str = os.getenv("OUTPUT_DIR", "outputs")
    enable_safety_filter: bool = os.getenv("ENABLE_SAFETY_FILTER", "1") == "1"
settings = Settings()
