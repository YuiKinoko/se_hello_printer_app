from hello_world import app
from hello_world.formater import get_formatted
from hello_world.formater import SUPPORTED, PLAIN
from flask import request


msg = "Hello World!"


@app.route('/')
def index():
    output = request.args.get('output')
    imie = request.args.get('name')
    if not output:
        output = PLAIN
    return get_formatted(msg, imie,
                         output.lower())


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)
