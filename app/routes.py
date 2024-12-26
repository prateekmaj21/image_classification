
from fastapi import APIRouter, HTTPException
from model.predict import ModelPredictor

router = APIRouter()
predictor = ModelPredictor("model/svm_image_model.pkl")

@router.post("/predict/")
def predict(image_path: str):
    try:
        result = predictor.predict(image_path)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
