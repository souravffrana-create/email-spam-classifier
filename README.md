# Email Spam Classifier

A machine learning project to classify emails as spam or not spam.

## What I built

- Trained a LinearSVC model on email data using TF-IDF vectorization
- Built a REST API using FastAPI to serve predictions
- Created a simple frontend using Streamlit

## Accuracy

98.5% on test data

## Tech used

- Python
- scikit-learn
- FastAPI
- Streamlit
- joblib

## How to run

1. Install dependencies
```
pip install -r requirements.txt
```

2. Start the API
```
uvicorn api.main:app --reload
```

3. Start the frontend (new terminal)
```
streamlit run frontend/app.py
```

## Project structure

```
├── api/          # FastAPI backend
├── model/        # Trained model
├── frontend/     # Streamlit UI
├── src/          # Training script
├── data/         # Dataset
└── requirements.txt
```


