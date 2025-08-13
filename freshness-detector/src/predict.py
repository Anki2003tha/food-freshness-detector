from tensorflow.keras.models import load_model
import numpy as np
import cv2
import os

# Load the trained model
model = load_model('freshness_model.h5')


def preprocess_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    # Resize the image to 128x128
    image = cv2.resize(image, (128, 128))
    # Convert the image to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Normalize pixel values to [0, 1]
    image = image / 255.0
    # Expand dimensions to match model input shape
    image = np.expand_dims(image, axis=0)
    return image


def predict_freshness(image_path):
    # Preprocess the image
    processed_image = preprocess_image(image_path)
    # Make a prediction
    predictions = model.predict(processed_image)
    # Get the predicted class and confidence
    class_index = np.argmax(predictions, axis=1)[0]
    confidence = np.max(predictions) * 100  # Convert to percentage
    # Map class index to label
    label = 'Fresh' if class_index == 0 else 'Rotten'
    return label, confidence



if __name__ == "__main__":
    # Example usage
    test_image_path = 'path/to/your/test/image.jpg'  # Replace with your image path
    prediction, confidence = predict_freshness(test_image_path)
    print(f"Prediction: {prediction}, Confidence: {confidence:.2f}%")