import dash_bootstrap_components as dbc
import dash_html_components as html

title = "Dash Template"

external_stylesheets = [
    dbc.themes.BOOTSTRAP, # Bootswatch theme
    'https://use.fontawesome.com/releases/v5.9.0/css/all.css', # for social media icons
]

meta_tags=[
    {'name': 'viewport', 
     'content': 'width=device-width, initial-scale=1', 
     'author': 'Maxie Lawrence'}
]

suppress_callback_exceptions = True

footer_content=html.Div([''])