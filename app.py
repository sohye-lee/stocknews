from flask import Flask, render_template

app = Flask('StockNews')

@app.route('/')
def home():
    return render_template('index.html')

app.run(host="127.0.0.1", port=8080)