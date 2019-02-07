from flask import Flask,render_template,request
import requests
from bs4 import BeautifulSoup





app=Flask(__name__)


@app.route('/')


def welcome():



    return render_template('index.html')


@app.route('/second')


def second():
    return "Welcome to the second page"




@app.route('/title')

def title():
    return  render_template('title.html')


@app.route('/show-form')


def show_form():
    return render_template('first-form.html')



@app.route('/data')

def print_name():
    first=request.args.get('first')
    last=request.args.get('last')
    return str("You put "+first+last)



@app.route('/person/<name>/<age>')

def display_name_age(name,age):
    return render_template('display_name_age.html',name=name,age=age)



@app.route('/calculate')

def calculate():
    return render_template('calc.html')


@app.route('/math')

def math():
    first=int(request.args.get('num1'))
    second=int(request.args.get('num2'))
    operation=request.args.get('operation')
    if str(operation)=="add":
        return str(first+second)
    elif str(operation)=="multiply":
        return str(first*second)
    elif str(operation)=="divide":
        return str(first/second)
    elif str(operation)=="substract":
        return str(first-second)



@app.route('/results')

def results():


    r=requests.get("https://www.news.google.com")

    data=r.text
    query=str(request.args.get('query'))
    soup=BeautifulSoup(data)
    result=""
    for my_tag in soup.find_all("article"):

        if query.lower() in str(my_tag).lower() :


            result+=str(my_tag)+'\n'

    return str(result)

if __name__=="__main__":
    app.run()
