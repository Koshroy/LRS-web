from flask import Flask, url_for, render_template, session, escape, request, redirect, g, jsonify
from contextlib import closing
from random import choice
import string

import swall

SECRET_KEY = 'Z;t\x02\x9eB\x91\xac\xd3\x98\xd8\xc6\xbc@%\xda\x95\x13\xaeJ\xed"\xcfT'
DEBUG = True


app = Flask(__name__)
app.config.from_object(__name__)

def gen_id():
    return ''.join([choice(string.letters + string.digits) for i in range(20)])

@app.route('/')
def game():
    return render_template('game.html', uid=gen_id())

@app.route('/hello')
def home():
    return 'hello!'

# JSON Dict
# Event: Start | Stop | None
# Wall_arr
# Robot_arr
# Misc_arr

@app.route('/pollstate', methods=['POST'])
def static_walls():
    #todo: get player nums
    board = []
    temp = [[], [], [], [], [],
                     [], [], [], [0], [],
                     [], [], [1,30], [], [],
                     [], [0], [], [], [],
                     [], [], [], [], []]
    _tuple = [swall.get_random_wall(1, 12),swall.get_random_wall(1, 12),temp]
    board.append(_tuple)
    board.append(_tuple)
    board.append(_tuple)
    return jsonify(event='start',pcount=3, sector=board)

@app.route('/clientevent', methods=['POST'])
def client_event():
    return jsonify(resp='ok')



        
if __name__ == "__main__":
    app.run()
