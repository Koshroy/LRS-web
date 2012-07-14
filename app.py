from flask import Flask, url_for, render_template, session, escape, request, redirect, g, jsonify
from contextlib import closing
from random import choice

SECRET_KEY = 'Z;t\x02\x9eB\x91\xac\xd3\x98\xd8\xc6\xbc@%\xda\x95\x13\xaeJ\xed"\xcfT'
DEBUG = True


app = Flask(__name__)
app.config.from_object(__name__)

def gen_id():
    return ''.join([choice(string.letters + string.digits) for i in range(20)])

@app.route('/')
def home():
    return 'hello!'



        
if __name__ == "__main__":
    app.run()
