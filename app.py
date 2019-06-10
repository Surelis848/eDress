import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
if "MONGO_DBNAME" in os.environ:
    app.config["MONGO_DBNAME"] = os.getenv('MONGO_DBNAME')
    app.config["MONGO_URI"] = os.getenv('MONGO_URI')
else:
    import config
    app.config["MONGO_DBNAME"] = config.DB_CONFIG["MONGO_DBNAME"]
    app.config["MONGO_URI"] = config.DB_CONFIG["MONGO_URI"]

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_clothes')
def get_clothes():
    return render_template("getclothes.html", 
                                            clothes=mongo.db.clothes.find(),
                                            types=mongo.db.types.find(),
                                            sizes=mongo.db.sizes.find(),
                                            colors=mongo.db.colors.find())
    
@app.route('/get_about')
def get_about():
    return render_template("about.html")
    
@app.route('/add_clothes')
def add_clothes():
    return render_template("addclothes.html", 
                                types=mongo.db.types.find(),
                                conditions=mongo.db.conditions.find(),
                                sizes=mongo.db.sizes.find(),
                                colors=mongo.db.colors.find())

@app.route('/insert_clothes', methods=['POST'])
def insert_clothes():
    clothes =  mongo.db.clothes
    clothes.insert_one(request.form.to_dict())
    return redirect(url_for('get_clothes'))
    
@app.route('/edit_clothes/<clo_id>')
def edit_clothes(clo_id):
    the_clo =  mongo.db.clothes.find_one({"_id": ObjectId(clo_id)})
    return render_template('editclothes.html', clothes=the_clo,
                                            types=mongo.db.types.find(),
                                            conditions=mongo.db.conditions.find(),
                                            sizes=mongo.db.sizes.find(),
                                            colors=mongo.db.colors.find())
    
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
        'season':request.form.get('season'),
        'description':request.form.get('description'),
        'picture':request.form.get('picture')
    })
    return redirect(url_for('get_clothes'))
    
@app.route('/delete_clothes/<clo_id>')
def delete_clothes(clo_id):
    mongo.db.clothes.remove({'_id': ObjectId(clo_id)})
    return redirect(url_for('get_clothes'))
    
if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)