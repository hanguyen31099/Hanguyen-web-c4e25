from flask import Flask, render_template,request,redirect
from  class_pymogo import Bike, Register
import mlap
mlap.connect()
app = Flask(__name__)
f_objects = Bike.objects()
k_objects = Register.objects()
@app.route('/',methods=["GET","POST"])
def create_new_register():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        k = Register(username=username,password=password)
        k.save()
        return "OK"
@app.route('/new_bike',methods=["GET","POST"])
def new_bike():
    if request.method == "GET":
        return render_template('add_new_bike.html')
    elif request.method == "POST":
        Model = request.form["Model"]
        Daily_fee = request.form["Daily fee"]
        Image = request.form["Image"]
        Year = request.form["Year"]
        text_description=request.form["text"]
        f = Bike(Model=Model,Daily_fee=Daily_fee,Image=Image,Year=Year,text_description=text_description)
        f.save()
        return render_template("Bike.html",f_objects=f_objects)

if __name__ == '__main__':
  app.run(debug=True)