from flask import Flask,render_template,jsonify,request
from dotenv import load_dotenv
from pymongo import MongoClient
import pymongo
import os

load_dotenv()
app=Flask(__name__)

mongo_uri=os.getenv("MONGO_URI")
client=pymongo.MongoClient(mongo_uri)
db=client.to_do
collection=db.task

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/submittodoitem")
def signup():
    form_data=dict(request.form)
    collection.insert_one(form_data)
    return render_template('success.html')

if __name__=='__main__':
    app.run(debug=True)
