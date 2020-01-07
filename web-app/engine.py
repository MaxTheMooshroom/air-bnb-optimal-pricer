# Third Party imports
from flask import Flask, render_template
from flask import make_response, request, g as Global

# Local imports
import config
import wrangler

app = Flask(config.title if config.title is not None else __name__)
app.config['SECRET_KEY'] = config.secret_key

@app.route('/')
def index():
    return render_template(f'index.html', 
                           header='Hello!')

@app.route('/api/v2/test-response/', methods=['GET'])
def index_get():
    #headers={'Content-Type': 'application/json'}
    response = wrangler.name(request.args['fname'])
    return make_response(render_template('index.html', header=response), 200)#, headers=headers)
