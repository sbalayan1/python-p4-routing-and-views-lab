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

@app.route('/count/<int:num>')
def count(num):
    res = ""
    for n in range(0, num):
        res += str(n) + "\n"
    
    return res

@app.route('/math/<int:num1><string:op><int:num2>')
def math(num1, op, num2):
    if op == "div":
        return str(num1/num2)
    if op == "+":
        return str(num1 + num2)
    if op == "-":
        return str(num1 - num2)
    if op == "%":
        return str(num1 % num2)
    
    if op == "*":
        return str(num1 * num2)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
