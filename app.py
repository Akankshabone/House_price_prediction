from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# Absolute path to model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "trained_model.pkl")

# Load model once
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('predict_price.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_price_view():

    if request.method == 'GET':
        return render_template('predict_price.html')

    try:
        size = float(request.form['size'])
        bedrooms = float(request.form['bedrooms'])
        bathrooms = float(request.form['bathrooms'])
        age = float(request.form['age'])
        distance = float(request.form['distance'])

        prediction = model.predict(
            [[size, bedrooms, bathrooms, age, distance]]
        )

        price = round(prediction[0], 2)

        return render_template('result.html', price=price)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)