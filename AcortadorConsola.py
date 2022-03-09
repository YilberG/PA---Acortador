import pyshorteners

url = input("ingresar el link >>>")

shrt = pyshorteners.Shortener()

nurl = shrt.tinyurl.short(url)

print(nurl)