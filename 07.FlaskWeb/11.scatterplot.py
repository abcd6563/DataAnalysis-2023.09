from flask import Flask, render_template,request
import numpy as np
import matplotlib.pyplot as plt
import os


app = Flask(__name__)


@app.route('/')  # localhost:5000/ 을 서비스하기 위한 코드
def index():
    return '<h1>scatterplot</h1>'


@app.route('/scatterplot', methods=['GET','POST'])
def scatterplot():
    if request.method == 'GET':
        return render_template('11.scatterplot.html')
    else:
        max = int(request.values['max'])
        min = int(request.values['min'])
        avg = int(request.values['avg'])
        standard = int(request.values['standard'])
        num = int(request.values['num'])
        X = np.random.normal(avg, standard, num)
        Y = np.random.uniform(min, max, num)
        plt.scatter(X,Y)
        img_file = os.path.join(app.root_path, 'static/img/scatter.png')
        plt.savefig(img_file)
        return render_template('11.scatterplot.res.html')
    


@app.route('/scatterplot.res')
def static_resource():
    print(app.root_path)                 #D:/WorkSpace/02.DataAnalysis/07.FlaskWeb
    img_file = os.path.join(app.root_path, 'static/img/scatter.png')
    return render_template('11.scatterplot.res.html')

if __name__ == '__main__':
    app.run(debug=True)