import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>서울시 구별 CCTV/인구 현황 시각화</h2>'

@app.route('/cctv2')
def cctv2():
    return render_template('11.cctv.html')   
    

if __name__ == '__main__':
    app.run(debug=True)