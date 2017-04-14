from flask import Flask
from flask import request
from flask import render_template
import time
import scrape
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template("home.html")

@app.route('/', methods=['POST'])
def search_for_user(name = None, length = 0, timeF = 0, res = [], startTime = 0):
	startTime = time.time()
	name = request.form['name']
	res = scrape.getVideoSearch(name)
	length = len(res)
	timeF = time.time() - startTime
	return render_template("results.html",name=name,res=res,length=length,timeF=timeF)





if __name__ == '__main__':
	app.run(debug=True)