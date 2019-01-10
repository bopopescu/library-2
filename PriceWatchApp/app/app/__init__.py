from flask import Flask, jsonify, render_template, request
from dbconnect import *
#from flask_cors import CORS
from web_price import UpdateThread
import time

app = Flask(__name__)
#CORS(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/addretailer/', methods=['GET', 'POST'])
def addretailer():
    if request.method == 'POST':
        link = request.form['link']
        name = request.form['name']
        update = add_retail_link(name, link)
        if update:
            return "Success"
        else:
            return "Failed"

    else:
        return render_template('index.html')


@app.route("/price")
def price():
    items = select_retailer()
    print(items)
    item_list = {"price": []}
    myprice = UpdateThread()

    for item in items:
        company = {
            "name": item[1],
            "link": item[2],
            "price": myprice.downloadValue()
        }

        item_list['price'].append(company)

    return jsonify(item_list)


@app.route("/show/")
def show():
    return render_template('show.html')


@app.route("/trackprice/")
def trackprice():
    myThread = UpdateThread()
    myThread.start()
    for i in range(100):
        time.sleep(10)
        return myThread.downloadValue()


if __name__ == "__main__":
    app.run(debug=True)
