# 🥦 Food Freshness Detector

An AI-powered application that classifies fruits and vegetables as **Fresh** or **Rotten** using image recognition.  
Built with **TensorFlow/Keras**, **OpenCV**, and integrated with a database for storing detection history.

---

## 📌 Features

- 🖼 **Image Classification** – Detect whether a fruit/vegetable is fresh or spoiled.
- ⚡ **Real-time Prediction** – Works on images from camera or file upload.
- 🗄 **Database Integration** – Stores predictions with confidence scores & timestamps.
- 📊 **User-friendly Output** – Displays results clearly with accuracy percentage.
- 🔄 **Scalable** – Can be extended for more food types and quality levels.

---

## 🛠 Tech Stack

| Category          | Technology Used |
|-------------------|-----------------|
| **Language**      | Python 3.x       |
| **ML Framework**  | TensorFlow / Keras |
| **Image Processing** | OpenCV         |
| **Database**      | SQLite / MySQL   |
| **Frontend (Optional)** | Streamlit / Flask |

---

## 📂 Project Structure
## 📂 Project Structure

```bash
food-freshness-detector/
│
├── 📄 README.md                 # Project documentation
├── 📦 requirements.txt          # Python dependencies
├── 🧠 freshness_model.h5         # Trained ML model
│
├── 📁 src/                      # Source code
│   ├── 🚀 app.py                 # Main application entry point
│   ├── 🧹 data_preprocessing.py  # Data loading & preprocessing
│   ├── 🗄 database.py            # Database connection & queries
│   ├── 🎯 model_training.py      # CNN model training script
│   ├── 🔍 predict.py             # Prediction script
│   │
│   └── 📂 utils/                 # Helper functions
│       └── __init__.py
│
└── ...
```



## ⚙ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Anki2003tha/food-freshness-detector.git
   cd food-freshness-detector


