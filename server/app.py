#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/hello')
def print_route():
    print("hello")
    return "hello"

@app.route('/count/<num>')
def count(num):
    res = ""
    for n in range(0, int(num)):
        res += str(n) + "\n"
    
    return res

@app.route('/math/<op>')
def math(op):
    if "div" in op:
        nums = op.split('div')
        res = int(nums[0]) / int(nums[1])
        return str(res)
    
    return str(eval(op))

if __name__ == '__main__':
    app.run(port=5555, debug=True)
