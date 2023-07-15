from flask import *
import numpy as  np
import pandas as pd
from sklearn.svm import SVC
app=Flask(__name__)

@app.route('/')
def loan():
  return render_template("index.html")

@app.route("/loan",methods=["POST"])
def page():
  Gender=eval(request.form.get("Gender"))
  Married=eval(request.form.get("Married"))
  Educated=eval(request.form.get("Educated"))
  Self-Employed=eval(request.form.get("Self-Employed"))
  Credit_History=eval(request.form.get("Credit_History"))
  Property_IN=eval(request.form.get("Property_IN"))
  
  url="Loan.csv"
  data=pd.read_csv(url, header=None)
  loan=data.values
  x=loan[:,1:6]
  y=loan[:,6]
  
  model=LinearRegression()
  model.fit(x,y)
  result=arr[0]
  
  arr=model.predict([[Gender,Married,Educated,Self-Employed,Credit_History,Property_IN]])
  return render_template("index.html",result=arr[5])
if __name__ == '__main__':
  app.run()
