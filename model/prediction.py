import joblib
from pathlib import Path
#Load model
model_path = Path(__file__).parent / "spam_email_classification.pkl"
pipeline = joblib.load(model_path)

def output_data(input:str):
    result = int(pipeline.predict([input])[0])
    if result == 0:
        message = "Ham"
    else:
        message = "Spam"
    return {"Prediction":result,
            "Message":message}