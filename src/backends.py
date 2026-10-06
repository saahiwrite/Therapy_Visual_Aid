from __future__ import annotations
from pathlib import Path
from PIL import Image, ImageDraw

class MockBackend:
    name = "mock-pillow"

    def generate(self, prompt: str, negative_prompt: str, seed: int, output_path: Path):
        img = Image.new("RGB", (768, 512), (245, 245, 240))
        d = ImageDraw.Draw(img)
        d.rounded_rectangle((40, 40, 728, 472), radius=24, outline=(80, 80, 80), width=3)
        text = "Therapy Visual Aid\n\n" + prompt[:220]
        d.text((70, 80), text, fill=(30, 30, 30))
        img.save(output_path)
        return output_path

class DiffusersBackend:
    name = "diffusers"

    def __init__(self, model_id: str, device: str = "cuda"):
        import torch
        from diffusers import AutoPipelineForText2Image
        dtype = torch.float16 if device.startswith("cuda") else torch.float32
        self.pipe = AutoPipelineForText2Image.from_pretrained(model_id, torch_dtype=dtype)
        self.pipe = self.pipe.to(device)
        self.device = device
        self.torch = torch

    def generate(self, prompt, negative_prompt, seed, output_path):
        g = self.torch.Generator(device=self.device).manual_seed(seed)
        image = self.pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            generator=g,
            num_inference_steps=4,
            guidance_scale=0.0,
        ).images[0]
        image.save(output_path)
        return output_path
