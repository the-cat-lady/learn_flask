from flask import Flask, request, json
import pandas as pd
import os
import sys

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    json_incoming_data = json.loads(request.get_data().decode('utf-8'))
    print('json_incoming_data: ', json_incoming_data)

    return('hihi - this is the output of a function call')

if __name__ == '__main__':
    print('\n', '*'*5, f'Open Insomnia and hit localhost at 0.0.0.0:5000', '*'*5, '\n')
    # listen on all IPs
    app.run(host='0.0.0.0')