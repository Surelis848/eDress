import os
from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for, session, flash, abort
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_paginate import Pagination, get_page_args
import bcrypt


app = Flask(__name__)
if "MONGO_DBNAME" in os.environ:
    app.config["MONGO_DBNAME"] = os.getenv('MONGO_DBNAME')
    app.config["MONGO_URI"] = os.getenv('MONGO_URI')
else:
    import config
    app.config["MONGO_DBNAME"] = config.DB_CONFIG["MONGO_DBNAME"]
    app.config["MONGO_URI"] = config.DB_CONFIG["MONGO_URI"]

mongo = PyMongo(app)
theclothes = mongo.db.clothes.find()

def get_clothing(offset=0, per_page=10):
    return theclothes[offset: offset + per_page]

@app.route('/')
@app.route('/get_clothes')
def get_clothes():
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = theclothes.count()
    pagination_clothes = get_clothing(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template("getclothes.html", 
                                            clothes=mongo.db.clothes.find().sort('date', -1),
                                            types=mongo.db.types.find(),
                                            clothing=pagination_clothes,
                                            page=page,
                                            per_page=per_page,
                                            pagination=pagination,
                                            sizes=mongo.db.sizes.find(),
                                            colors=mongo.db.colors.find())

#Get About page    
    
@app.route('/get_about')
def get_about():
    return render_template("about.html")
    
#Get 'Add Clothes' form 
#Receive types, conditions, sizes and colors from mongodb
    
@app.route('/add_clothes')
def add_clothes():
    return render_template("addclothes.html", 
                                types=mongo.db.types.find(),
                                conditions=mongo.db.conditions.find(),
                                sizes=mongo.db.sizes.find(),
                                colors=mongo.db.colors.find()
                                )

#Take elements from the filled form and insert them into mongodb

@app.route('/insert_clothes', methods=['POST'])
def insert_clothes():
    clothes =  mongo.db.clothes
    add_item = {
        'date':"{:%b, %d %Y}".format(datetime.now()),
        'username':request.form.get('username'),
        'title':request.form.get('title'),
        'type': request.form.get('type'),
        'condition': request.form.get('condition'),
        'size':request.form.get('size'),
        'brand':request.form.get('brand'),
        'composition':request.form.get('composition'),
        'color':request.form.get('color'),
        'description':request.form.get('description'),
        'picture':request.form.get('picture')
    }
    clothes.insert(add_item)
    return redirect(url_for('get_clothes'))
    
#Get edit clothes form with filled elements from mongob    
    
@app.route('/edit_clothes/<clo_id>')
def edit_clothes(clo_id):
    the_clo =  mongo.db.clothes.find_one({"_id": ObjectId(clo_id)})
    return render_template('editclothes.html', clothes=the_clo,
                                            types=mongo.db.types.find(),
                                            conditions=mongo.db.conditions.find(),
                                            sizes=mongo.db.sizes.find(),
                                            colors=mongo.db.colors.find())

#Take elements from the filled form and update them in mongodb
    
@app.route('/update_clothes/<clo_id>', methods=["POST"])
def update_clothes(clo_id):
    clothes = mongo.db.clothes
    clothes.update( {'_id': ObjectId(clo_id)},
    {
        'username':request.form.get('username'),
        'title':request.form.get('title'),
        'type': request.form.get('type'),
        'condition': request.form.get('condition'),
        'size':request.form.get('size'),
        'brand':request.form.get('brand'),
        'composition':request.form.get('composition'),
        'color':request.form.get('color'),
        'description':request.form.get('description'),
        'picture':request.form.get('picture')
    })
    return redirect(url_for('get_clothes'))
    
#Delete clothes element from the database    
    
@app.route('/delete_clothes/<clo_id>')
def delete_clothes(clo_id):
    mongo.db.clothes.remove({'_id': ObjectId(clo_id)})
    return redirect(url_for('get_clothes'))
    
#Render template for a separate piece of clothing    
    
@app.route('/get_a_piece/<clo_id>')
def get_a_piece(clo_id):
    the_clo =  mongo.db.clothes.find_one({"_id": ObjectId(clo_id)})
    return render_template("apiece.html", clothes=the_clo)
    
#Main function for running the app    
    
if __name__ == "__main__":
        app.secret_key = 'mysecret',
        app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)