# Dependencies and setup
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_mars import scrape
import pymongo

# create Flask instance
app = Flask(__name__)

# Initialize PyMongo
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")


#first route corresponds to getting data from MongoDB
@app.route("/")
def home():
    #find items within mars_db
    items=mongo.db.collection.find()
    for item in items:
        print(item)
    #render data
    return render_template("index.html", mars_mongo=items)

#route will trigger scraping function
@app.route("/scrape")
def app_scrape():
    #drop collection if present
    collection.drop()
    mars_data = scrape_mars.scrape_info()

    #update collection
    mongo.db.collection.update({}, mars_data, upsert=True)
    
    #redirect to home page
    return redirect ("/")

if __name__ == "__main__":
    app.run(debug=True)

