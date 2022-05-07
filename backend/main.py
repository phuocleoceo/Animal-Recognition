from fastapi.middleware.cors import CORSMiddleware
from recognition import predict
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AnimalImage(BaseModel):
    uri: str


@app.post("/predict")
async def predict_animal(image: AnimalImage):
    animal, confidence = predict(image.uri)
    # Mock predict
    return {"animal": animal, "confidence": confidence}


if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level="info", reload=True)
    print("running")
