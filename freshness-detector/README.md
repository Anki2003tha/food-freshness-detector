# Freshness Detector

This project aims to detect whether a fruit or vegetable is fresh or spoiled using images. It utilizes deep learning techniques with TensorFlow/Keras for model training and OpenCV for image preprocessing. The results are stored in a database, and an optional web interface is provided for user interaction.

## Project Structure

```
freshness-detector
├── src
│   ├── data_preprocessing.py      # Functions for image preprocessing
│   ├── model_training.py           # CNN model architecture and training
│   ├── predict.py                  # Load model and predict freshness
│   ├── database.py                 # Database operations for storing results
│   ├── app.py                      # Web interface for user interaction
│   └── utils
│       └── __init__.py             # Utility functions (if needed)
├── requirements.txt                # Project dependencies
├── README.md                       # Project documentation
└── freshness_model.h5             # Trained model file
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd freshness-detector
   ```

2. **Install dependencies:**
   Ensure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Prepare your dataset:**
   - You can either download existing datasets from Kaggle or take your own photos of fruits and vegetables.
   - Organize the images into two categories: `Fresh` and `Rotten`.

4. **Preprocess the images:**
   - Use the `data_preprocessing.py` script to preprocess your images before training the model.

5. **Train the model:**
   - Run the `model_training.py` script to build and train the CNN model. The trained model will be saved as `freshness_model.h5`.

6. **Make predictions:**
   - Use the `predict.py` script to load the trained model and predict the freshness of new fruit images.

7. **Database integration:**
   - The `database.py` script handles storing the prediction results in SQLite/MySQL.

8. **Run the web interface (optional):**
   - If you want to use the web interface, run the `app.py` script to start the application.

## Usage

- Upload an image of a fruit or vegetable to the web interface to see the freshness prediction and confidence score.
- View historical predictions stored in the database.

## License

This project is licensed under the MIT License.