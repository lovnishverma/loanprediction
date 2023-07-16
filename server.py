from flask import *
import numpy as  np
import pandas as pd
from sklearn.svm import LinearRegression
app=Flask(__name__)

@app.route('/template')
def first():
  return render_templates("index.html")


@app.route('/lp') # open the form for loan prediction
def loan(): 
  return  render_template('loan.html') 


@app.route('/dp') # open the form for diamond price prediction
def diamond(): 
  return  render_template('diamond.html') 


@app.route('/fp') # open the form for flower prediction
def irisf(): 
  return  render_template('iriss.html') 


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


@app.route('/dp', methods = ['POST']) 
def diamondpricepredict(): 
  carat = eval ( request.form.get ( "carat") )
  cut   = eval ( request.form.get ( "cut") )
  clarity = eval ( request.form.get ( "clarity") )
  color   = eval ( request.form.get ( "color") ) 
  x  = eval ( request.form.get ( "x") )
  y  = eval ( request.form.get ( "y") )
  z  = eval ( request.form.get ( "z") )
  # predict and save the output in result variable
  url   = "diamond.csv"
  dfspf = pd.read_csv(url)
  df1   = dfspf.values
  X = df1[:,[ 1,2,3,4,6,7,8]] 
  Y = df1[:,5]   
  model = LinearRegression ()
  model.fit( X , Y )
  arr   = model.predict([[ carat,cut,color,clarity,x,y,z]] )
  #################
  result = arr[0] 
  return " Diamond Price : "+str(result) 
# render_template("result.html", data = str(result) + " %")


if __name__ == '__main__':
  app.run()
