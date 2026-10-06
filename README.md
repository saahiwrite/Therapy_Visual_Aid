# Therapy Visual Aid Generator — Production Implementation
A FastAPI text-to-image service designed for therapeutic visual-aid workflows. The repository supports a zero-GPU mock backend for CI and a real Hugging Face Diffusers backend for GPU deployment.

## Architecture
`request -> prompt normalization/guardrails -> backend abstraction -> Diffusers or deterministic mock -> persisted PNG -> API response`

## Features
- FastAPI `/generate` and `/health` endpoints
- SDXL-Turbo-compatible Diffusers backend with seeded generation
- deterministic Pillow backend for local verification and CI
- configurable model/device through environment variables
- Docker + Compose deployment
- API and service-level tests
- prompt guardrails that avoid diagnostic claims or identifiable patient information

## Run locally
```bash
pip install -e .
uvicorn app:app --reload
curl -X POST http://127.0.0.1:8000/generate -H 'content-type: application/json' -d '{"concept":"5-4-3-2-1 grounding exercise"}'
```

## GPU mode
```bash
pip install -r requirements-gpu.txt
BACKEND=diffusers DEVICE=cuda MODEL_ID=stabilityai/sdxl-turbo uvicorn app:app --host 0.0.0.0 --port 8000
```
The model weights are intentionally not committed. First execution downloads the selected model from Hugging Face.

## Results and resume claim
The resume reports deployment in a therapist-office workflow, reducing visual-aid creation from ~15 minutes to under 5 seconds and supporting 50+ therapists. Those are **project-reported operational results** and are not fabricated by the included demo. This repo provides the implementation needed to benchmark latency on your hardware; returned responses include `latency_ms`.

## Production extensions
Add authenticated therapist accounts, object storage/CDN, asynchronous job queues for non-turbo models, audit logging, content moderation, encrypted prompt storage, and human review for clinical deployment.
