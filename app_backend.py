from fastapi import FastAPI, Request
import numpy as np
import joblib

model = joblib.load("model.joblib")

app = FastAPI()


def prediction(SepalLength, SepalWidth, PetalLength, PetalWidth):
    input = np.array([[SepalLength, SepalWidth, PetalLength, PetalWidth]]).astype(
        np.float64
    )
    prediction = model.predict(input)
    return prediction[0]


@app.post("/result")
async def read_root(request: Request):
    data = await request.json()
    SepalLength, SepalWidth, PetalLength, PetalWidth = data.values()
    pred = prediction(SepalLength, SepalWidth, PetalLength, PetalWidth)
    return str(pred)
