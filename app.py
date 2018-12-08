from flask import Flask, render_template
# from flask_mysqldb import MySQL

app = Flask(__name__)

# app.comfig['MYSQL_HOST'] = "localhost"
# app.comfig['MYSQL_USER'] = "localhost"
# app.comfig['MYSQL_PASSWORD'] = "jay"
# app.comfig['MYSQL_DB'] = "habs"
# app.comfig['MYSQL_CURSORCLASS'] = "DictCursor"

# myslq = MySQL(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register", methods=['POST', 'GET'])
def register():

    return render_template('registration.html')

@app.route("/signin", methods=['POST', 'GET'])
def signin():

    return render_template('signin.html')

@app.route("/admin", methods=['POST', 'GET'])
def admin():

    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)
 