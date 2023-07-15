from flask import *
import pandas as pd
import numpy as np
from  sklearn.linear_model import LinearRegression 


app = Flask(__name__) 

@app.route('/') 
def first(): 
  return render_template('index.html') 

@app.route('/r') # open the form for result prediction  
def second(): 
  return  render_template('result.html') 

@app.route('/d') # open the form for diamond price prediction
def diamond(): 
  return  render_template('diamondp.html') 

@app.route('/hprice') # open the form for diamond price prediction
def hprice(): 
  return  render_template('hprice.html') 

@app.route('/hp', methods = ['POST'] ) 
def housepricepredict(): 
  location='Whitefield'
  sqft  = eval ( request.form.get ( "area") )
  bath  = eval ( request.form.get ( "bath") )
  bhk   = eval ( request.form.get ( "bhk") )
  # predict and save the output in result variable
  url   = "bhp.csv"
  df = pd.read_csv(url)
  X = df.drop(['price'],axis='columns')
  y = df["price"]
  from sklearn.linear_model import LinearRegression
  model = LinearRegression()
  model.fit(X,y)
  loc_index = np.where(X.columns==location)[0][0]

  x = np.zeros(len(X.columns))
  x[0] = sqft
  x[1] = bath
  x[2] = bhk
  if loc_index >= 0:
      x[loc_index] = 1
        
  hp = model.predict([x])[0]
  return " House price predicted as (in lakhs ) "  + str(hp) 


  
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
  url   = "cdiamond.csv"
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

@app.route('/p' , methods=['POST']) 
def predict(): 
  hrsself = int ( request.form.get ( "hrsself") )
  hrstut  = int ( request.form.get ( "hrstut") ) 
  # predict and save the output in result variable
  url   = "https://raw.githubusercontent.com/sarwansingh/Python/master/ClassExamples/data/student-pass-fail-data.csv"
  dfspf = pd.read_csv(url)
  df1   = dfspf.values
  X = df1[:,0:2] # all rows and first two columns  becomes my input ie. X
  Y = df1[:,2]   # all rows and only third column becomes my output ie Y 
  model = LinearRegression ()
  model.fit( X , Y )
  arr   = model.predict([[hrsself,hrstut]] )
  #################
  result = arr[0] *100
  return render_template("result.html", data = str(result) + " %")


if __name__ == '__main__': 
  app.run()