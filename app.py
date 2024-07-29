from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('models/model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([data['features']])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True, port=3000)
