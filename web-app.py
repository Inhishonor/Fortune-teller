#This is for the Flask Web App
from fortune-teller import main
from flask import Flask

app = Flask(__name__)

@app.route("/")
main()
