# Third Party imports
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

# Standard imports
import pickle

# Local imports
import config
from wrangler import wrangle

model = pickle.load(open(config.model_dir, 'rb'))

app = Flask(config.title if config.title is not None else __name__)
CORS(app)

@app.route('/', methods=['GET'])
def get():
    data = {}

    for param in config.model_params:
        data[param] = request.args.get(param)

    df = pd.Dataframe(data)

    wrangled = wrangle(data)

    result = model.predict(wrangled)

    data['estimated_price'] = result

    return jsonify(data)
