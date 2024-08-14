from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf

app = Flask(__name__)

model = tf.keras.models.load_model('best_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        features = np.array(data['data'])
        features = features.reshape(1, 28, 28, 1)
        
        prediction = model.predict(features)
        predicted_class = np.argmax(prediction, axis=1)
        
        return jsonify({'prediction': int(predicted_class[0])})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)