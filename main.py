import ast
import requests
import configparser
from flask import Flask, request, jsonify, render_template
from flask import Flask, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)



a = 5.0
b = 5.0
c = 5.0
d = 5.0
e = 5.0
f = 5.0
g = 5.0
h = 5.0
i = 5.0
j = 5.0
k = 5.0
l = 5.0
m = 5.0
n = 5.0
o = 5.0
p = 5.0
q = 5.0
r = 5.0
av = 0.0


def refresh_average():
    global av
    av = (a + b + c + d + e + f + g + h +
          i + j + k + l + m + n + o + p +
          q + r) / 18 / 10
    if av > 1:
        av = 1.0
        return av
    elif av < 0:
        av = 0
    else:
        return av


def parse_webhook(webhook_data):
    data = ast.literal_eval(webhook_data)
    return data


@app.route('/', methods=['GET'])
@cross_origin()
def index():
    if request.method == 'GET':
        print('Here is the current av')
        return jsonify({'_result': str(refresh_average())})
    else:
        return {"code": "success"}


@app.route('/rsi_h', methods=['POST'])
@cross_origin()
def rsi_h():
    if request.method == 'POST':
        print('rsi sell alert received')
        global a
        global c
        a = 10
        c = 5
        refresh_average()
        print(refresh_average())
        return {"code": "success"}
    else:
        return {"code": "success"}


@app.route('/rsi_l', methods=['POST'])
@cross_origin()
def rsi_l():
    if request.method == 'POST':
        print('rsi buy alert received')
        global c
        global a
        c = 0
        a = 5
        refresh_average()
        return {"code": "success"}
    else:
        return {"code": "success"}


@app.route('/rsi_mfi_h', methods=['POST'])
@cross_origin()
def api_rsi_mfi_h_trigger():
    if request.method == 'POST':
        print('rsi sell alert received')
        global d
        global e
        d = 15
        e = 5
        refresh_average()
        return {"code": "success"}
    else:
        print('do nothing')
        return {"code": "success"}


@app.route('/rsi_mfi_l', methods=['POST'])
@cross_origin()
def api_rsi_mfi_l_trigger():
    if request.method == 'POST':
        print('rsi buy alert received')
        global e
        global d
        d = 5
        e = -5
        refresh_average()
        return {"code": "success"}
    else:
        print('do nothing')
        return {"code": "success"}


@app.route('/stoch_k_h', methods=['POST'])
@cross_origin()
def api_rsi_stoch_k_h_trigger():
    if request.method == 'POST':
        print('stoch sell alert received')
        global f
        global g
        g = 5
        f = 20
        refresh_average()
        return {"code": "success"}
    else:
        print('do nothing')
        return {"code": "success"}

@app.route('/stoch_k_l', methods=['POST'])
@cross_origin()
def api_rsi_stoch_k_l_trigger():
    if request.method == 'POST':
        print('stoch buy alert received')
        global g
        global f
        f = 5
        g = -10
        refresh_average()
        print(refresh_average())
        return {"code": "success"}
    else:
        print('do nothing')
        return {"code": "success"}


@app.route('/stoch_k_mu', methods=['POST'])
@cross_origin()
def api_rsi_stoch_k_mu_trigger():
    if request.method == 'POST':
        print('stoch buy alert received')
        global h
        global i
        i = 5
        h = 0
        refresh_average()
        print(refresh_average())
        return {"code": "success"}
    else:
        print('do nothing')
        return {"code": "success"}

@app.route('/stoch_k_md', methods=['POST'])
def api_rsi_stoch_k_md_trigger():
    if request.method == 'POST':
        print('stoch sell alert received')
        global i
        global h
        h = 5
        i = 10
        refresh_average()
        print(refresh_average())
        return {"code": "success"}
    else:
        print('do nothing')
        return {"code": "success"}

@app.route('/sell_diamond', methods=['POST'])
def api_rsi_sell_diamond_trigger():
    if request.method == 'POST':
        print('sell diamond alert received')
        global j
        global k
        k = 5
        j = 30
        refresh_average()
        print(refresh_average())
        return {"code": "success"}
    else:
        print('do nothing')
        return {"code": "success"}

@app.route('/buy_diamond', methods=['POST'])
def api_rsi_buy_diamond_trigger():
    if request.method == 'POST':
        print('buy diamond alert received')
        global k
        global j
        global r
        r = 5
        j = 5
        k = -20
        refresh_average()
        print(refresh_average())
        return {"code": "success"}
    else:
        print('do nothing')
        return {"code": "success"}

@app.route('/sell_red_circle', methods=['POST'])
def api_rsi_sell_red_circle_trigger():
    if request.method == 'POST':
        print('sell alert recieved')
        global l
        global k
        global n
        k = 5
        n = 5
        l = 12
        refresh_average()
        print(refresh_average())
        return {"code": "success"}
    else:
        print('do nothing')
        return {"code": "success"}

@app.route('/sell_red_circle_5m', methods=['POST'])
def api_rsi_sell_red_circle_5_trigger():
    if request.method == 'POST':
        print('sell alert recieved')
        global m
        global o
        o = 5
        m = 10
        refresh_average()
        print(refresh_average())
        return {"code": "success"}
    else:
        print('do nothing')
        return {"code": "success"}

@app.route('/buy_green_circle', methods=['POST'])
def api_rsi_buy_green_circle_trigger():
    if request.method == 'POST':
        print('buy alert recieved')
        global n
        global l
        global j
        j = 5
        l = 5
        n = -2
        refresh_average()
        print(refresh_average())
        return {"code": "success"}
    else:
        print('do nothing')
        return {"code": "success"}

@app.route('/buy_green_circle_5', methods=['POST'])
def api_rsi_buy_green_circle_5_trigger():
    if request.method == 'POST':
        print('buy alert recieved')
        global o
        global m
        m = 5
        o = 0
        refresh_average()
        print(refresh_average())
        return {"code": "success"}
    else:
        print('do nothing')
        return {"code": "success"}


@app.route('/sell_red_circle_div', methods=['POST'])
def api_rsi_sell_red_circle_div_trigger():
    if request.method == 'POST':
        print('sell alert recieved')
        global p
        global q
        q = 5
        p = 30
        refresh_average()
        print(refresh_average())
        return {"code": "success"}
    else:
        print('do nothing')
        return {"code": "success"}

@app.route('/buy_green_circle_div', methods=['POST'])
def api_rsi_buy_green_circle_div_trigger():
    if request.method == 'POST':
        print('buy alert recieved')
        global q
        global p
        global r
        p = 5
        q = -20
        refresh_average()
        print(refresh_average())
        return {"code": "success"}
    else:
        print('do nothing')
        return {"code": "success"}

@app.route('/gold_buy', methods=['POST'])
def api_rsi_gold_buy_trigger():
    if request.method == 'POST':
        print('gold alert recieved')
        global r
        global q
        global k
        q = 5
        k = 5
        r = 35
        refresh_average()
        print(refresh_average())
        return {"code": "success"}
    else:
        print('do nothing')
        return {"code": "success"}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
