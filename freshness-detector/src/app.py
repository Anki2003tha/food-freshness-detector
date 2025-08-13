from flask import Flask, request, jsonify # type: ignore
from predict import predict_freshness
from database import save_prediction

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Predict freshness
    prediction, confidence = predict_freshness(file)
    
    # Save to database
    save_prediction(file.filename, prediction, confidence)
    
    return jsonify({
        'filename': file.filename,
        'prediction': prediction,
        'confidence': confidence
    })

def get_history():
    raise NotImplementedError

@app.route('/history', methods=['GET'])
def history():
    # Retrieve historical data from the database
    # This function should be implemented in database.py
    records = get_history()
    return jsonify(records)

if __name__ == '__main__':
    app.run(debug=True)