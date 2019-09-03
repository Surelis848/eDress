import os
from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for, session, flash, abort
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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

@app.route('/')

#Login/register functionality

#@app.route('/login', methods=['POST', 'GET'])
#def login():
    #if request.method == 'POST':
        #users = mongo.db.users
       # login_user = users.find_one({'name': request.form['username']})
        
 #       password = request.form['password']
 #       password = bytes(password, 'utf-8')
 #       hashed = login_user['password']
            
 #       if login_user:
  #          if bcrypt.checkpw(password, hashed):
 #               session['username'] = request.form['username']
 #               return redirect(url_for('get_clothes'))
  #      return 'Invalid username/password combination'
#    return render_template("login.html")
        
#@app.route('/register', methods=['POST', 'GET'])
#def register():
  #  if request.method == 'POST':
    #    users = mongo.db.users
    #    existing_user = users.find_one({'name': request.form['username']})
   #     if existing_user is None:
   #         password = request.form['password']
   #         password = bytes(password, 'utf-8')
   #         hashpass = bcrypt.hashpw(password, bcrypt.gensalt())
   #         users.insert({'name': request.form['username'], 'password' : hashpass})
    #        session['username'] = request.form['username']
     #       return redirect(url_for('get_clothes'))
      #  return 'That username already exists!'
#    return render_template('register.html')
    
# Get the clothes from database and display them in the main page
#Receive types, colors and sizes from mongodb for filters
    
@app.route('/get_clothes')
def get_clothes():
    return render_template("getclothes.html", 
                                            clothes=mongo.db.clothes.find().sort('date', -1),
                                            types=mongo.db.types.find(),
                                            sizes=mongo.db.sizes.find(),
                                            colors=mongo.db.colors.find())

        
#@app.route("/logout")
#def logout():
    #session['logged_in'] = False
    #return render_template('')
    
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