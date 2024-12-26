
import os
import cv2
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load images from dataset
def load_images_from_folder(folder):
    images = []
    labels = []
    for label, subfolder in enumerate(os.listdir(folder)):
        subfolder_path = os.path.join(folder, subfolder)
        if os.path.isdir(subfolder_path):
            for filename in os.listdir(subfolder_path):
                img_path = os.path.join(subfolder_path, filename)
                img = cv2.imread(img_path)
                if img is not None:
                    img = cv2.resize(img, (64, 64))  # Resize image
                    images.append(img)
                    labels.append(label)
    return np.array(images), np.array(labels)

# Train the model
def train_model(dataset_path, model_path):
    # Load images and labels
    images, labels = load_images_from_folder(dataset_path)
    images = images.reshape(images.shape[0], -1)  # Flatten images
    X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)

    # Train an SVM model
    clf = svm.SVC(kernel='linear', probability=True)
    clf.fit(X_train, y_train)

    # Test the model
    y_pred = clf.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

    # Save the model
    joblib.dump(clf, model_path)
    print(f"Model saved at {model_path}")

if __name__ == "__main__":
    train_model('dataset_images', 'svm_image_model.pkl')
