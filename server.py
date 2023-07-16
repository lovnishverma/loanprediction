from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('loan.html')

@app.route('/predict', methods=['POST'])
def predict():
    gender = int(request.form.get('Gender'))
    married = int(request.form.get('Married'))
    education = int(request.form.get('Education'))
    self_employed = int(request.form.get('Self_employed'))
    credit_history = int(request.form.get('credit_history'))
    property_area = int(request.form.get('property_area'))

    # Load the loan dataset
    df = pd.read_csv('loan.csv')

    # Prepare the data
    X = df[['Gender', 'Married', 'Education', 'Self_Employed', 'Credit_History', 'Property_Area']]
    y = df['Loan_Status']

    # Create a logistic regression model
    model = LogisticRegression()

    # Train the model
    model.fit(X, y)

    # Make prediction on new data
    new_data = [[gender, married, education, self_employed, credit_history, property_area]]
    prediction = int(model.predict(new_data)[0])

    return render_template('loan.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
