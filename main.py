# Imports from 3rd party libraries
from flask import Flask

# Imports from standard libraries
import os

# Imports from this application
import config
from engine import app

def display_page(pathname):
    if os.path.exists(pathname):  # does path exist?
        if os.path.isfile(pathname):  # is path a file?
            # TODO: serve web page at given path
            pass
    else:
        return dcc.Markdown('## Page not found')

if __name__ == '__main__':
    # run the engine
    pass