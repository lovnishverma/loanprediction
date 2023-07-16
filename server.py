from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('loan.html')

@app.route('/predict', methods=['POST'])
def predict():
    gender = int(request.form.get('gender'))
    married = int(request.form.get('married'))
    education = int(request.form.get('education'))
    self_employed = int(request.form.get('self_employed'))
    credit_history = int(request.form.get('credit_history'))
    property_area = int(request.form.get('property_area'))

    # Load the loan dataset
    df = pd.read_csv('loan.csv')

    # Prepare the data
    X = df[['Gender', 'Married', 'Education', 'Self_Employed', 'Credit_History', 'Property_Area']]
    y = df['Loan_Status']

    # Perform label encoding on categorical features
    label_encoder = LabelEncoder()
    X_encoded = X.apply(label_encoder.fit_transform)

    # Create a random forest classifier model
    model = RandomForestClassifier()

    # Train the model on the entire dataset
    model.fit(X_encoded, y)

    # Prepare the input data for prediction
    input_data = pd.DataFrame([[gender, married, education, self_employed, credit_history, property_area]],
                              columns=['Gender', 'Married', 'Education', 'Self_Employed', 'Credit_History', 'Property_Area'])
    input_encoded = input_data.apply(label_encoder.transform)

    # Make prediction on new data
    prediction = model.predict(input_encoded)[0]

    return render_template('loan.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
