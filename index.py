from flask import Flask,render_template, request, redirect, url_for
import mysql.connector
import pyshorteners

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='url',
    port=3306
)
db.autocommit = True

app = Flask(__name__)

@app.get("/")
def index():
    cursor = db.cursor(dictionary=True)


    cursor.execute('select * from urls')

    urls = cursor.fetchall()
    cursor.close()
    return render_template("index.html",urls=urls)

@app.get("/shorturl")
def shortUrl():
    return render_template("urls/shorturl.html")

@app.post("/shorturl")
def shortUrlPost():
    nombreurl = request.form.get('url')

    cursor = db.cursor()

    cursor.execute("insert into urls(url, nueva) values(%s, %s)",(
        nombreurl,
    ))
    cursor.close()
    return redirect(url_for('index'))

app.run(debug=True)

