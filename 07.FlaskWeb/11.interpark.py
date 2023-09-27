from flask import Flask, render_template
import util.crawl_util as cu 

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>크롤링</h1>'
       


@app.route('/interpark2')
def interpark2():
    book_list = cu.get_bestseller()
    return render_template('11.interpark.html', book_list=book_list)

if __name__ == '__main__':
    app.run(debug=True)