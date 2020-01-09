"""Code for our app"""
​
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
​
from .data_wrangling import wrangle
​
def create_app():
    app = Flask(__name__)
​
    # load pickled model
    model = pickle.load(open('model.pkl','rb'))
​
    # prevent web errors
    CORS(app)
​
    # List of features to use in request
    PARAMETERS = [
        'neighbourhood_group_cleansed', 'room_type', 'accommodates',
        'bathrooms', 'bedrooms', 'beds', 'bed_type', 'security_deposit',
        'cleaning_fee', 'minimum_nights', 'amenities'
    ]
​
    # called when the landing page is requested, expects a GET request.
    @app.route('/', methods=['GET'])
    def predict():
​
        # get json object from the get request
        data = request.get_json(force=True)
        # Have you verified with web that a json will be received?
        # Have you shared this info? Just something to consider in the future :)
		# ANSWER: I know they were using it because I'm following when they share screen and I heard they talking. 
		# Also I saw it when Gurpreet shared the screen. And I got the code from some tutorials and I'm not sure if there are other json methods or alternatives
​
        # encapsulate value y in a list for each key x
        data.update((x, [y]) for x, y in data.items())
​
        # convert data into dataframe object to be passed through the model
        data_df = pd.DataFrame.from_dict(data)
​
        # making a prediction by passing a dataframe through it
        result = model.predict(data_df)
​
        # not needed since you aren't updating a dict
        output = {'results': int(result[0])}
​
        #return jsonify(results=output)
        # this would return a json that looks like this: 
        # {'results': {'results': int(result[0])}}
​
        # return data in the form of a json object
        #return jsonify(results=int(result[0]))
        # another valid solution would be:
        return jsonify(output)
		# ANSWER: if you want we can keep your solution
​
    # return the app object to be run
    return app
​
if __name__ == '__main__':
    # app does not exist in this scope, you have to create it first.
	# ANSWER: So, we create the main or we delete this part?
	
    create_app().run(port = 5000, debug=True)
    # why set the port? There's nothing wrong with that, but I'm curious
    # about your reason(s). 
	# ANSWER: I found it in code example, in tutorials. Who should set it? I don't make idea, Gurpreet? FE? 