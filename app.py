from flask import Flask,render_template,redirect,request,url_for
from snacks import Snack
from flask_modus import Modus

app=Flask(__name__)


modus=Modus(app)



cikolata=Snack("çikolata","Tatlı")

borek=Snack("Börek","Tuzlu")

muz=Snack("Muz","Tatlı")

snacks=[cikolata,borek,muz]



@app.route('/')

def index():


    return render_template("index.html",snacks=snacks)


@app.route('/create',methods=["GET","POST"])


def create():

    if request.method=="POST":
        snacks.append(Snack(request.form["name"],request.form["kind"]))


        return redirect(url_for('index'))
    return render_template("create.html",snacks=snacks)


@app.route('/edit/<int:id>',methods=["GET","PATCH"])

def edit(id):
    found_snack=next(snack for  snack in snacks)

    return  render_template('edit.html',snack=found_snack)


@app.route('/delete/<int:id>',methods=["GET","PATCH","DELETE"])

def delete(id):
    found_snack=next(snack for snack in snacks if snack.id==id)

    if request.method==b"DELETE":
        snacks.remove(found_snack)
        return redirect(url_for('index'))
    return render_template('delete.html',snack=found_snack)






