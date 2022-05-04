from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def home(request):
    return render(request,'home.html')

def predict(request):
    return render(request,'predict.html')
def result(request):
    df = pd.read_csv(r'D:\Diabetes\DiabetesPredictor\templates\diabetes.csv')
    from sklearn.linear_model import LinearRegression, LogisticRegression

    x = df.drop('Outcome', axis='columns')
    y = df.Outcome
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    model = LogisticRegression()
    model.fit(x_train,y_train)

    var1 = float(request.GET['n1'])
    var2 = float(request.GET['n2'])
    var3 = float(request.GET['n3'])
    var4 = float(request.GET['n4'])
    var5 = float(request.GET['n5'])
    var6 = float(request.GET['n6'])
    var7 = float(request.GET['n7'])
    var8 = float(request.GET['n8'])

    pred = model.predict([[var1,var2,var3,var4,var5,var6,var7,var8]])

    result1 = ""
    if pred == [1]:
        result1 = "Positive"
    else:
        result1 = "Negative"

    return render(request,'predict.html',{"result2" :result1})