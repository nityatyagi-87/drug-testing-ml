from fastapi import FastAPI, Form
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Drug Testing ML API is running!"}

@app.post("/predict")
def predict(drug_name: str = Form(...)):
    # Here you’ll later load your model and make predictions
    result = f"Predicted safe dosage range for {drug_name} generated successfully."
    return {"drug": drug_name, "result": result}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
