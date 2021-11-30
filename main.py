from flask import Flask, render_template, redirect, request, abort
import sqlite3
from contextlib import closing
from Objects import Game


app = Flask(__name__)
conn = sqlite3.connect("games.db", check_same_thread=False)

@app.route('/')
def home():
   return render_template("home.html")


@app.route('/display')
def display():
   return render_template("display.html")

@app.route('/display')
def getGameData():
   sql = '''SELECT name, image, console, year, description FROM Games'''
   with closing(conn.cursor()) as c:
      c.execute(sql)
      results = c.fetchall()
      games=[]
      for game in results:
         games.append([game[0], game[1], game[2], game[3], game[4]])
      return render_template("display.html", games=games)



@app.route('/add')
def add():
   getGameData()
   return render_template("add.html")

@app.route('/add', methods=["POST"])
def getAddFormData():
   name = request.form.get("name")
   image = request.form.get("image")
   console = request.form.get("console")
   year = request.form.get("year")
   description = request.form.get("description")
   sql = '''INSERT INTO Games (name, image, console, year, description)
            VALUES(?, ?, ?, ?, ?)'''
   with closing(conn.cursor()) as c:
      c.execute(sql, (name, image, console, year, description))
      conn.commit()
   return render_template("add.html")

@app.route('/remove')
def remove():
   return render_template("remove.html")

@app.route('/remove', methods=["POST"])
def removeGame():
   name = request.form.get("name")
   sql = '''DELETE FROM Games WHERE name = ?'''
   with closing(conn.cursor()) as c:
      c.execute(sql, (name,))
      test = conn.commit()
      print("Test", test)
   return render_template("remove.html")
if __name__ == '__main__':
   app.run()