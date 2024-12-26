
# Image Classification Project

## Project Structure
- `dataset/images/`: Contains subdirectories for each class of images (e.g., `cat`, `dog`).
- `app/`: Contains FastAPI app files.
  - `main.py`: FastAPI app entry point.
  - `routes.py`: API routes for image classification.
- `model/`: Contains model training and prediction logic.
  - `train.py`: Script to train the image classification model.
  - `predict.py`: Script for making predictions using the trained model.
- `requirements.txt`: Dependencies for the project.

## Instructions
1. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Train the Model:
   ```bash
   python model/train.py
   ```
3. Run FastAPI:
   ```bash
   uvicorn app.main:app --reload
   ```
