from flask import Flask, render_template, redirect
import pymongo
import BCMmarsscrape
import os

# Create MongoDB connection; Create database and collection if it does not exist.
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client["mars_db"]
collection = db["marsdata"]

app = Flask(__name__)

# mongo = pymongo(app, url="mongodb://localhost:27017/marsinfo_db")

@app.route('/')
def index():
    mars_info = db.collection.find_one()
    return render_template('index.html', marsinfo=mars_info)


@app.route('/scrape')
def scrape():
    mars = db.collection
    data = BCMmarsscrape.scrape()
    mars.update(
        {},
        data,
        insert=True)
    
    return redirect('/', code=302)


if __name__ == "__main__":
    app.run(debug=True)

