import os
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')  # localhost:5000/ 을 서비스하기 위한 코드
def index():
    return '<h1>Static Resource</h2>'

@app.route('/static')
def static_resource():
    print(app.root_path)                 #D:/WorkSpace/02.DataAnalysis/07.FlaskWeb
    img_file = os.path.join(app.root_path, 'static/img/cat.jpg')
    return render_template('04.static.html')


if __name__ == '__main__':
    app.run(debug=True)