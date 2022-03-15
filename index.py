from flask import Flask,render_template, request, redirect, url_for
from random import choice
import mysql.connector,string

# db = mysql.connector.connect(
#     host='127.0.0.1',
#     user='root',
#     password='',
#     database='url',
#     port=3306
# )
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

    cursor.execute('select nueva from urls order by id desc limit 1')
    ultima = cursor.fetchone()

    cursor.close()
    return render_template("index.html", ultima = ultima)

@app.get("/shorturl")
def shortUrl():
    return render_template("urls/shorturl.html")

@app.post("/shorturl")
def shortUrlPost():
    nombreurl = request.form.get('url')
    codigo = ''.join(choice(string.ascii_letters+string.digits) for _ in range(4))
    nueva = request.host_url+codigo # http://127.0.0.1:5000/dsWN

    cursor = db.cursor()
    cursor.execute("insert into urls(url,nueva) values(%s,%s)",(
        nombreurl,
        nueva,
    ))

    cursor.close()
    return redirect(url_for('index'))

@app.get("/tabla")
def tablaUrl():
    cursor = db.cursor(dictionary=True)
    cursor.execute('select * from urls')
    urls = cursor.fetchall()

    cursor.close()
    return render_template("tablaurl.html", urls=urls)

@app.get("/<codigo>")
def redirectnueva(codigo):
    shorturl = request.host_url+codigo # http://127.0.0.1:5000/dsWN
    cursor = db.cursor()
    cursor.execute("select url from urls where nueva = %s", (shorturl,))
    url = cursor.fetchone()
    if(url != None): return redirect(url[0])
    return redirect(url_for('index'))

app.run(debug=True)

