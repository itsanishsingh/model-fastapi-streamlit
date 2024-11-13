from fastapi import FastAPI, Request
import numpy as np
import joblib

class_model = joblib.load("classification_model.joblib")
reg_model = joblib.load("regression_model.joblib")

app = FastAPI()


def class_prediction(SepalLength, SepalWidth, PetalLength, PetalWidth):
    input = np.array([[SepalLength, SepalWidth, PetalLength, PetalWidth]]).astype(
        np.float64
    )
    prediction = class_model.predict(input)
    return prediction[0]


def reg_prediction(hours, prev_score):
    input = np.array([[hours, prev_score]]).astype(np.float64)
    prediction = reg_model.predict(input)
    return prediction[0]


@app.post("/classification")
async def read_root(request: Request):
    data = await request.json()
    SepalLength, SepalWidth, PetalLength, PetalWidth = data.values()
    pred = class_prediction(SepalLength, SepalWidth, PetalLength, PetalWidth)
    return str(pred)


@app.post("/regression")
async def read_root(request: Request):
    data = await request.json()
    hours, prev_score = data.values()
    pred = reg_prediction(hours, prev_score)
    return str(pred)
