import pickle

from flask import Flask, render_template, request
from flask_cors import cross_origin

app = Flask(__name__)


@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return render_template("index.html")


@app.route('/result', methods=['POST', 'GET'])
@cross_origin()
def result():
    if request.method == 'POST':
        try:
            indus = float(request.form['indus'])
            rm = float(request.form['rm'])
            tax = float(request.form['tax'])
            ptratio = float(request.form['ptratio'])
            lstat = float(request.form['lstat'])
            filename = 'model.pickle'
            model = pickle.load(open(filename, 'rb'))
            prediction = model.predict([[indus, rm, tax, ptratio, lstat]])
            return render_template('result.html', prediction=round(prediction[0], 2))
        except Exception as ex:
            print(f"Exception occurred: {ex}")
            return "Some Exception has occurred."
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
