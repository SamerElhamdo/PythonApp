from flask import Flask, render_template, request, redirect, url_for
import models
import stores
from app import *

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
	return render_template(	"index.html", posts = post_store.get_all())

@app.route("/topic/add", methods = ["GET", "POST"])
def topic_add():
	if request.method == "POST":
		new_post = models.Post(request.form["title"], request.form["body"])
		post_store.add(new_post)
		return redirect(url_for("home"))
	else:
		return render_template("topic_add.html")