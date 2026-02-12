from flask import Flask 
from threading import Thread
app= Flask('')

@app.route ('/')
def home():
    return "server running"
def run():
    app.run('0.0.0.0',port=8080)
def server_on():
    t= Thread(target=run)
    t.start