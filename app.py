from flask import Flask

app = Flask(__name__,
            static_folder="static",
            template_folder="templates")

@app.route("/")
def index():
  return "Hello Flask"

@app.route('/users/<username>')
def show_user_profile(username):
    return f'User : {username}'

app.run(host="0.0.0.0", port=3050, debug=True)
