from flask import Flask, render_template
from Forums import models, stores


app = Flask(__name__)

post_store = stores.PostStore()
member1 = models.Post("Life", "Life is alawys great")
member2 = models.Post("Sunshine", "Sunshine is amazing")
post_store.add(member1)
post_store.add(member2)

@app.route("/")
@app.route("/index")

def home():
    posts = post_store.get_all()
    return render_template('index.html', posts=posts)


app.run()
