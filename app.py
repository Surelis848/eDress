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
    
if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)