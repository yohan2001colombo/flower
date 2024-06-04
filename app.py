from flask import Flask,render_template,request
import pickle
import numpy as np


app = Flask(__name__)

def prediction(feature_list):
    filename = 'model/predictor.pickle'
    with open(filename,"rb") as file:
         model = pickle.load(file)
    predict_flower = model.predict([feature_list])
    return predict_flower


@app.route('/',methods=["POST","GET"])
 
def index():
    pred = [3]
    if request.method == "POST":
        sepal_length = request.form["sepal_length"]
        sepal_width = request.form["sepal_width"]
        petal_length = request.form["petal_length"]
        petal_width = request.form["petal_width"]

        lst = []
        lst.append(float(sepal_length))
        lst.append(float(sepal_width))
        lst.append(float(petal_length))
        lst.append(float(petal_width))

       
        pred = prediction(lst)
        print(pred)
    return render_template("index.html",pred = pred[0])

if __name__ == "__main__":
    app.run(debug=True)



