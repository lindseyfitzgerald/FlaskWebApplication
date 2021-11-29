from flask import Flask, render_template, redirect, request, abort
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
   return render_template("index.html")


@app.route('/display')
def display():
   return render_template("display.html")


@app.route('/add')
def add():
   return render_template("add.html")


@app.route('/remove')
def remove():
   return render_template("remove.html")


if __name__ == '__main__':
   app.run()