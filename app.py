from flask import Flask, render_template, request
from joblib import load
import numpy as np
from sklearn.preprocessing import OneHotEncoder

app = Flask(__name__)

# Load the pre-trained Random Forest model
model = load('Resources/random_forest_model.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get feature values from the form
    features = [float(request.form[f'feature{i}']) for i in range(1, 10)]

    term_option = float(request.form['term'])
    term_result = [1, 0] if term_option == 0 else [0, 1]

    hm_option = float(request.form['home_mortgages'])
    hm_result = [1, 0, 0] if hm_option == 0 else [0, 1, 0] if hm_option == 1 else [0, 0, 1]

    features += term_result + hm_result

    # Make a prediction
    prediction = model.predict([features])[0]

    # Display the result
    result = 'Bankruptcy Prediction: ' + ('Bankrupt' if prediction == 1 else 'Not Bankrupt')

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)