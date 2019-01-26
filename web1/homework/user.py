from flask import Flask,render_template
app = Flask(__name__)

@app.route('/user/<username>')
def user_profile(username):
    users = {
    "huy" : {
            "name" : "Nguyen Quang Huy",
            "age" : 29
        },
    "tuananh" : {
            "name" : "Huynh Tuan Anh",
            "age" : 22
        }
    }
    if username.lower() not in users.keys():
        return 'User not found'
    else:
        return render_template("user.html", users=users, username=username.lower())

  

if __name__ == '__main__':
  app.run(debug=True)