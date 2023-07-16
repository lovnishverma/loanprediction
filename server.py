from flask import *
import numpy as  np
import pandas as pd
from sklearn.svm import LinearRegression
app=Flask(__name__)

@app.route('/')
def loan():
  return render_templates("index.html")

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
  arr=model.predict([[Gender,Married,Educated,Self-Employed,Credit_History,Property_IN]])
  result=arr[0]
  return render_template("loan.html",data = str(result))
if __name__ == '__main__':
  app.run()
