from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('model','rb'))

app = Flask(__name__)


@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    PH = request.form['1']
    Hardness = request.form['2']
    Solids = request.form['3']
    Chloramines = request.form['4']
    Sulfate = request.form['5']
    Conductivity = request.form['6']
    Organic_carbon = request.form['7']
    Trihalomethanes = request.form['8']
    Turbidity = request.form['9']
    

    arr = np.array([[PH, Hardness, Solids, Chloramines, Sulfate, Conductivity , Organic_carbon, Trihalomethanes ,Turbidity]])
    pred = model.predict(arr)
    return render_template('after.html', data=pred)



if __name__ == "__main__":
    app.run(debug=True)