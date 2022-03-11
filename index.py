from flask import Flask,render_template, request, redirect, url_for
import mysql.connector
import pyshorteners

db = mysql.connector.connect(
    host='academia.c1mebdhdxytu.us-east-1.rds.amazonaws.com',
    user='p3',
    password='ALrUBIaLYcHR',
    database='p3',
    port=3306
)
db.autocommit = True

app = Flask(__name__)

@app.get("/")
def index():
    cursor = db.cursor(dictionary=True)


    cursor.execute('select * from urls')

    urls = cursor.fetchall()

    cursor.execute('SELECT MAX(nueva) AS nueva FROM urls')
    ultima = cursor.fetchall()
    cursor.close()
    return render_template("index.html", urls=urls, ultima = ultima)

@app.get("/shorturl")
def shortUrl():
    return render_template("urls/shorturl.html")

@app.post("/shorturl")
def shortUrlPost():
    nombreurl = request.form.get('url')

    shrt = pyshorteners.Shortener()

    nurl = shrt.tinyurl.short(nombreurl)

    cursor = db.cursor()

    cursor.execute("insert into urls(url, nueva) values(%s, %s)",(
        nombreurl,
        nurl
    ))
    cursor.close()
    return redirect(url_for('index'))

@app.get("/tablaurl")
def tablaurl():

    cursor = db.cursor(dictionary=True)


    cursor.execute('select * from urls')

    urls = cursor.fetchall()

    cursor.execute('SELECT MAX(nueva) AS nueva FROM urls')
    ultima = cursor.fetchall()
    cursor.close()
    return render_template("tablaurl.html", urls=urls, ultima = ultima)


app.run(debug=True)

