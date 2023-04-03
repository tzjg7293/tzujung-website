from flask import Flask, render_template, request, jsonify, send_file # jsonify to return a json response

from chatbot.chatbot import chatbot_response

# Setup flask app
app = Flask(__name__, template_folder='templates', static_folder='static') # underscore __ is just conventional way of naming

# Define 2 routes

@app.get("/") # Define GET request for each route (put the respective requests above the functions) # new syntax in Flask # if we go to our home page (/) then we go to index.html
def index_get_routes(): # route 1 for home page
    return render_template("index.html")

@app.post("/predict") # Predict route will be POST request; the route her is "/predict"
def predict(): # route 2 to get predictions
    text = request.get_json().get("message") # in our json file we get the "message" which will be defined in a (not yet created) json file
    # TODO: Check if text is valid
    response = chatbot_response(text)
    message = {"answer": response} # create a dictionary called message and define a key called "answer"
    return jsonify(message) # jsonify the response

@app.route('/download')
def download():
    path = 'static/pdf/sydney-resume.pdf'
    return send_file(path, as_attachment=True)

# Run the app
if(__name__ == "__main__"):
    app.run(debug = True) # debug = true for testing