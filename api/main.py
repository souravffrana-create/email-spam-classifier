from fastapi import FastAPI
from fastapi.responses import JSONResponse
from api.data_validation import User_input
from model.prediction import output_data

app = FastAPI()

@app.get("/")
def Home():
    return{"message":"Spam_and_Ham_Classification API"}

@app.get("/health")
def health():
    status = "OK"
    return JSONResponse(status_code=200,content={"Status":status})

@app.post("/predict")
def predict (data:User_input):
    text = data.Text
    try:
      output = output_data(text)
      return JSONResponse(status_code=200,content={"Response":output})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))