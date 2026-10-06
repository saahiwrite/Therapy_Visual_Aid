THERAPY_GUARDRAILS = "non-graphic, emotionally safe, no diagnostic claims, no identifiable patient"
def build_prompt(concept: str, audience: str, style: str) -> str:
    concept=" ".join(concept.strip().split())
    return f"Therapeutic visual aid for {audience}: {concept}. Style: {style}. {THERAPY_GUARDRAILS}."
