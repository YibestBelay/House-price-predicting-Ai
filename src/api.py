import pickle
import uvicorn
import numpy as np
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# Load the trained Ridge model
with open("src/best_model.pkl", "rb") as f:
    model = pickle.load(f)

# Initialize FastAPI app
app = FastAPI(title="House Price Prediction API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change to specific frontend URL in production)
    allow_credentials=True,
    allow_methods=["*"],   # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],   # Allow all headers
)


# Serve static frontend files
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Serve the main index.html file
@app.get("/")
def serve_frontend():
    return FileResponse("frontend/index.html")

# Define input data schema
class HouseFeatures(BaseModel):
    rm: float
    lstat: float
    ptratio: float
    indus: float

# Define API endpoint for predictions
@app.post("/predict/")
async def predict_price(features: HouseFeatures):
    # Convert input to dataframe
    input_data = pd.DataFrame([features.dict()])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    return {"predicted_price": round(prediction[0], 2)} 

# Run the API with uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
