from flask import Flask,render_template,request


app=Flask(__name__)


@app.route('/')


def welcome():
    names_of_instructors=["ELlie","Tim","Matt"]
    random_name="Tom"

    return render_template('index.html',names=names_of_instructors,name=random_name)


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


if __name__=="__main__":
    app.run()
