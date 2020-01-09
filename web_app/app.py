""" Code for our app """

# Standard imports
import pickle

# 3rd party imports
import numpy as np
import pandas as pd
import xgboost
from flask import Flask, request, jsonify
from flask_cors import CORS

# Local imports
from .data_wrangling import wrangle

def create_app():
    app = Flask(__name__)

    # load pickled model
    model = pickle.load(open('model.pkl','rb'))

    # prevent web errors
    CORS(app)

    # List of features to use in request
    PARAMATERS = [
        'neighbourhood_group_cleansed', 'room_type', 'accommodates',
        'bathrooms', 'bedrooms', 'beds', 'bed_type', 'security_deposit',
        'cleaning_fee', 'minimum_nights', 'amenities'
        ]

    @app.route('/', methods=['GET'])
    def predict():

        # get JSON object from the GET request
        data = request.get_json(force=True)

        # encapsulate value y in a list for each value x
        data.update((x, [y]) for x, y in data.items())

        # convert data into dataframe to be passed through the model
        data_df = pd.DataFrame.from_dict(data)

        # making a prediction by passing a dataframe through the model
        result = model.predict(data_df)

        # storing the result as a dict
        output = {'results': int(result[0])}

        # convert the dict to a JSON object and return it
        return jsonify(output)

    # return the app object to be run
    return app

# if this file is main, run a development server
if __name__ == '__main__':
    create_app().run(debug=True)


