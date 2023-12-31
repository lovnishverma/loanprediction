from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('loan.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the form
    gender = int(request.form.get('gender'))
    married = int(request.form.get('married'))
    education = int(request.form.get('education'))
    self_employed = int(request.form.get('self_employed'))
    credit_history = int(request.form.get('credit_history'))
    property_area = int(request.form.get('property_area'))

    # Load the loan dataset
    df = pd.read_csv('loan.csv')

    # Prepare the data
    X = df[['gender', 'married', 'education', 'self_employed', 'credit_history', 'property_area']]
    y = df['loan_status']

    # Create a random forest classifier model
    model = RandomForestClassifier()

    # Train the model on the entire dataset
    model.fit(X, y)

    # Make prediction on new data
    new_data = [[gender, married, education, self_employed, credit_history, property_area]]
    prediction = int(model.predict(new_data)[0])

    return render_template('loan.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)