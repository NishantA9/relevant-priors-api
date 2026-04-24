from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any

app = FastAPI()

def normalize(text):
    return text.lower().replace("cntrst", "contrast")

def is_relevant(current_desc, prior_desc):
    current = normalize(current_desc)
    prior = normalize(prior_desc)

    important_words = ["brain", "head", "chest", "abdomen", "pelvis", "spine", "mri", "ct", "xray", "ultrasound"]

    score = 0
    for word in important_words:
        if word in current and word in prior:
            score += 1

    return score >= 1

@app.post("/predict")
def predict(payload: Dict[str, Any]):
    predictions = []

    for case in payload.get("cases", []):
        case_id = case["case_id"]
        current_desc = case["current_study"]["study_description"]

        for prior in case.get("prior_studies", []):
            predictions.append({
                "case_id": case_id,
                "study_id": prior["study_id"],
                "predicted_is_relevant": is_relevant(
                    current_desc,
                    prior["study_description"]
                )
            })

    return {"predictions": predictions}