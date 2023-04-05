from flask import Flask, url_for, render_template, request, jsonify # jsonify to return a json response
import logging
from chatbot.chatbot import chatbot_response

# Setup flask app
app = Flask(__name__, template_folder='templates', static_folder='static') # underscore __ is just conventional way of naming
logging.basicConfig(filename='error.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

# Define 2 routes

@app.get("/") # Define GET request for each route (put the respective requests above the functions) # new syntax in Flask # if we go to our home page (/) then we go to index.html
def index(): # route 1 for home page
    return render_template("index.html")

@app.post('/predict') # Predict route will be POST request; the route her is "/predict"
def predict(): # route 2 to get predictions
    app.logger.info('Info level log')
    app.logger.warning('Warning level log')
    text = request.get_json().get("message") # in our json file we get the "message" which will be defined in a (not yet created) json file
    response = chatbot_response(text)
    message = {"answer": response} # create a dictionary called message and define a key called "answer"
    return jsonify(message) # jsonify the response

# Run the app
if(__name__ == "__main__"):
    app.run(debug = True, host='0.0.0.0', port=8000) # debug = true for testing
    app.config['TEMPLATES_AUTO_RELOAD'] = True