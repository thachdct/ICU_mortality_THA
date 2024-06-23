from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'thachnn'
app.config['MYSQL_DB'] = 'medical_data'

mysql = MySQL(app)


# Rounter hien thi
@app.route('/')
def detailsScreen():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM benhnhan")
        data = cur.fetchall()
        cur.close()
        return str(data)

if __name__ == '__main__':
    app.run(debug=True)
