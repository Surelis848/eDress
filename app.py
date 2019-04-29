import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'eDress'
app.config['MONGO_URI'] = 'mongodb+srv://surelis:rootUser@myfirstcluster-1cswe.mongodb.net/eDress?retryWrites=true'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_clothes')
def get_clothes():
    return render_template("getclothes.html", clothes=mongo.db.clothes.find())
    
@app.route('/get_about')
def get_about():
    return render_template("about.html")
    
@app.route('/add_clothes')
def add_clothes():
    return render_template("addclothes.html")

@app.route('/insert_clothes', methods=['POST'])
def insert_clothes():
    clothes =  mongo.db.clothes
    clothes.insert_one(request.form.to_dict())
    return redirect(url_for('get_clothes'))
    
if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)