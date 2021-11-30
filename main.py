import os

from flask import Flask, render_template, redirect, request, abort
import sqlite3
from contextlib import closing
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'static/images'
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.jfif', 'gif']
conn = sqlite3.connect("games.db", check_same_thread=False)

@app.route('/')
def home():
   return render_template("home.html")

@app.route('/display')
def display():
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
   return render_template("add.html")

@app.route("/add", methods = ['POST'] )
def getFormData():

    uploaded_file = request.files["image"]
    filename = secure_filename(uploaded_file.filename)
    name = request.form.get("name")

    console = request.form.get("console")
    year = request.form.get("year")
    description = request.form.get("description")
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        sql = '''INSERT INTO Games (name, image, console, year, description)
                    VALUES(?, ?, ?, ?, ?)'''
        with closing(conn.cursor()) as c:
           c.execute(sql, (name, filename, console, year, description))
           conn.commit()
    return redirect("display")


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