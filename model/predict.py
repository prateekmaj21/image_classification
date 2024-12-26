
import joblib
import numpy as np
import cv2

class ModelPredictor:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def predict(self, image_path):
        img = cv2.imread(image_path)
        img = cv2.resize(img, (64, 64))  # Resize image
        img = img.reshape(1, -1)  # Flatten image
        prediction = self.model.predict(img)
        probability = self.model.predict_proba(img)
        return {"prediction": prediction[0], "probability": probability.tolist()[0]}
