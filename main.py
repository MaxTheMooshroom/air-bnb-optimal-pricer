# Local imports
from engine import app
from config import debug

if __name__ == '__main__':
    app.run(debug=debug)