from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('loan.html')

@app.route('/predict', methods=['POST'])
def predict():
    gender = request.form.get('gender')
    married = request.form.get('married')
    dependents = request.form.get('dependents')
    education = request.form.get('education')
    self_employed = request.form.get('self_employed')
    applicant_income = int(request.form.get('applicant_income'))
    coapplicant_income = int(request.form.get('coapplicant_income'))
    loan_amount = request.form.get('loan_amount')
    loan_amount_term = request.form.get('loan_amount_term')
    credit_history = request.form.get('credit_history')
    property_area = request.form.get('property_area')

    # Load the loan dataset
    df = pd.read_csv('loan.csv')

    # Prepare the data
    X = df[['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome',
            'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']]
    y = df['Loan_Status']

    # Create a logistic regression model
    model = LogisticRegression()

    # Train the model
    model.fit(X, y)

    # Make prediction on new data
    new_data = [[gender, married, dependents, education, self_employed, applicant_income,
                 coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area]]
    prediction = model.predict(new_data)[0]

    return render_template('loan.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
