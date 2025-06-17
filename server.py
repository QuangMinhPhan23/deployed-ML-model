from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
    
class_names = ['Extrovert', 'Introvert']

app = FastAPI(
    title="Personality Prediction API",
    description="API for predicting personality type (Extrovert/Introvert)",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

class FeatureInput(BaseModel):
    features: list

@app.get("/")
def read_root():
    return {"message": "Welcome to the Personality Prediction API!"}

@app.post("/predict")
def predict(input_data: FeatureInput):
    features = input_data.features
    # Ensure the input is a valid list of numerical features
    if not isinstance(features, list) or not all(isinstance(i, (int, float)) for i in features):
        raise HTTPException(status_code=400, detail="Invalid input format. Please provide a list of numerical features.")
    
    # Reshape the input to match the model's expected input shape
    features = np.array(features).reshape(1, -1)
    
    # Make prediction
    predicted_class = model.predict(features)[0]
    predicted_prob = model.predict_proba(features)[0]
    
    return {
        "class": class_names[predicted_class],
        "probability": predicted_prob.tolist()
    }
