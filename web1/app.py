from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello"

@app.route("/c4e25")
def c4e25():
    return "C4E25"
@app.route("/hi/<name>")
def hi(name):
    return "hi " + name + " Have a nice day"
@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    return str(a+b)
@app.route("/simple_hmtl")
def simple_html():
    return "<h3>Simple</h3>"
@app.route("/html")
def html():
    return render_template("sample.html")
food_list=[
    "bun dau",
    "cơm",
    "bún chả"
]
@app.route("/food/<int:x>") # detail
def food(x):
    return render_template("food.html",title=food_list[x])
@app.route("/menu")
def menu():
    return render_template("menu.html",food_list=food_list)
detail={
    'title' : 'Bún chả',
    'image' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/B%C3%BAn_Ch%E1%BA%A3.jpg/1200px-B%C3%BAn_Ch%E1%BA%A3.jpg'
}
@app.route("/detail")
def details():
    return render_template("food_detail.html",detail=detail)
if __name__ == '__main__':
  app.run(debug=True)
