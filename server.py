from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer

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
    loan_amount = int(request.form.get('loan_amount'))
    loan_amount_term = int(request.form.get('loan_amount_term'))
    credit_history = int(request.form.get('credit_history'))
    property_area = request.form.get('property_area')

    # Load the loan dataset
    df = pd.read_csv('loan.csv')

    # Prepare the data
    X = df[['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome',
            'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']]
    y = df['Loan_Status']

    # Perform one-hot encoding on categorical features
    enc = OneHotEncoder(handle_unknown='ignore')
    X_encoded = enc.fit_transform(X)

    # Handle missing values
    imputer = SimpleImputer(strategy='mean')
    X_encoded_filled = imputer.fit_transform(X_encoded)

    # Create a random forest classifier model
    model = RandomForestClassifier()

    # Train the model on the entire dataset
    model.fit(X_encoded_filled, y)

    # Prepare the input data for prediction
    input_data = [[gender, married, dependents, education, self_employed, applicant_income,
                   coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area]]
    input_encoded = enc.transform(input_data)

    # Make prediction on new data
    prediction = model.predict(input_encoded)[0]

    return render_template('loan.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
