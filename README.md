# Relevant Priors API

## Getting Started

1. Clone the Repository
```bash
git clone https://github.com/NishantA9/relevant-priors-api.git
cd relevant-priors-api

2. Install Dependencies
pip install -r requirements.txt


3. Run the FastAPI Server
python -m uvicorn app:app --reload

The API should now be running locally at: 
http://127.0.0.1:8000


4. Open the Swagger UI documentation in your browser:
http://127.0.0.1:8000/docs
Test the /predict Endpoint

Inside Swagger UI:

    Open the POST /predict endpoint
    Click Try it out
    Paste the following JSON payload:

{
  "challenge_id": "relevant-priors-v1",
  "schema_version": 1,
  "generated_at": "2026-04-16T12:00:00.000Z",
  "cases": [
    {
      "case_id": "1001016",
      "patient_id": "606707",
      "patient_name": "Andrews, Michael",
      "current_study": {
        "study_id": "3100042",
        "study_description": "MRI BRAIN STROKE LIMITED WITHOUT CONTRAST",
        "study_date": "2026-03-08"
      },
      "prior_studies": [
        {
          "study_id": "2453245",
          "study_description": "MRI BRAIN STROKE LIMITED WITHOUT CONTRAST",
          "study_date": "2020-03-08"
        },
        {
          "study_id": "992654",
          "study_description": "CT HEAD WITHOUT CNTRST",
          "study_date": "2021-03-08"
        }
      ]
    }
  ]
}

Click Execute


5. Hosted API (Render Deployment)

Swagger Docs:
https://relevant-priors-api-srlx.onrender.com/docs

Predict Endpoint:
https://relevant-priors-api-srlx.onrender.com/predict


Expected Response Example
{
  "predictions": [
    {
      "case_id": "1001016",
      "study_id": "2453245",
      "predicted_is_relevant": true
    },
    {
      "case_id": "1001016",
      "study_id": "992654",
      "predicted_is_relevant": false
    }
  ]
}

## Nishant Acharekar