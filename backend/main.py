from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File
from recognition import predict
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


@app.post("/predict")
async def predict_animal(image: UploadFile = File(...)):
    animal, confidence = predict(await image.read())
    # Mock predict
    return {"animal": animal, "confidence": confidence}


if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level="info", reload=True)
    print("running")
