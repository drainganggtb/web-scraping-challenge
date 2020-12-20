# Dependencies and setup
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_mars import scrape
import pymongo

# create Flask instance
app = Flask(__name__)

# Initialize PyMongo
# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
# Define database and collection
db = client.mars_app_db
collection = db.items



#first route corresponds to getting data from MongoDB
@app.route("/")
def home():
    #find items within mars_db
    items=db.items.find()
    for item in items:
        print(item)
    #render data
    return render_template("index.html", headline=item['news_title'], text=item['news_p'], table=item['mars_facts'], image=item['featured_image_url'], hem_img=item['hemispheres_info'])

#route will trigger scraping function
@app.route("/scrape")
def app_scrape():
    #drop collection if present
    collection.drop()
    collection.insert_one(scrape())
    
    #redirect to home page
    return redirect ("/")

if __name__ == "__main__":
    app.run(debug=True)

