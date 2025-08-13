from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import os

def create_model():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(2, activation='softmax'))  # 2 classes: fresh, rotten
    return model

def train_model(train_data_dir, validation_data_dir, epochs=10):
    model = create_model()
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    train_datagen = ImageDataGenerator(rescale=1.0/255)
    validation_datagen = ImageDataGenerator(rescale=1.0/255)

    train_generator = train_datagen.flow_from_directory(
        train_data_dir,
        target_size=(128, 128),
        batch_size=32,
        class_mode='sparse'
    )

    validation_generator = validation_datagen.flow_from_directory(
        validation_data_dir,
        target_size=(128, 128),
        batch_size=32,
        class_mode='sparse'
    )

    model.fit(train_generator, validation_data=validation_generator, epochs=epochs)

    model.save('freshness_model.h5')

if __name__ == "__main__":
    train_data_dir = 'path/to/train_data'  # Update with your training data path
    validation_data_dir = 'path/to/validation_data'  # Update with your validation data path
    train_model(train_data_dir, validation_data_dir, epochs=10)