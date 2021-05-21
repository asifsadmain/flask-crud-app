from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)

def getUsers():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user")
    users = cur.fetchall()
    cur.close()
    return render_template('index.html', users = users)

@app.route('/', methods=['POST', 'GET'])
def indexPost():
    if request.method == 'POST':
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        email = details['email']
        mobile = details['mobile']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user(firstName, lastName, email, mobile) VALUES (%s, %s, %s, %s)", (firstName, lastName, email, mobile))
        mysql.connection.commit()
        cur.close()
        return getUsers()
    if request.method == 'GET':
        return getUsers()


if __name__ == '__main__':
    app.run()