import cv2
import numpy as np


def preprocess_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Resize the image to 128x128
    image = cv2.resize(image, (128, 128))
    
    # Convert the image to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Normalize pixel values to [0, 1]
    image = image.astype('float32') / 255.0
    
    return image

def augment_image(image):
    # Data augmentation techniques can be applied here
    # For example: rotation, flipping, brightness changes
    # This is a placeholder for augmentation logic
    return image

def preprocess_images(image_paths):
    processed_images = []
    for path in image_paths:
        image = preprocess_image(path)
        processed_images.append(image)
    return np.array(processed_images)