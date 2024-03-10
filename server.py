from flask import Flask, render_template
from typing import Any
import requests



api  = "https://api.npoint.io/c04405b179f322858801"
response = requests.get(url=api)
list__ = response.json()

app = Flask("__main__")
@app.route('/')
def home():
    return render_template("index.html", posts = list__)


@app.route('/contact')
def contact():
    return render_template("contact.html")    

@app.route('/about')
def about():
    return render_template("about.html")   
 
@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template("post.html", posts = list__[post_id-1])    


if __name__ == "__main__":
    app.run(debug=True)



# The following is a sample data of that json file
""" [
  {
    "id": 1,
    "body": "Nori grape silver beet broccoli kombu beet greens fava bean potato quandong celery. Bunya nuts black-eyed pea prairie turnip leek lentil turnip greens parsnip. Sea lettuce lettuce water chestnut eggplant winter purslane fennel azuki bean earthnut pea sierra leone bologi leek soko chicory celtuce parsley jícama salsify.",
    "title": "The Life of Cactus",
    "subtitle": "Who knew that cacti lived such interesting lives."
  },
  {
    "id": 2,
    "body": "Chase ball of string eat plants, meow, and throw up because I ate plants going to catch the red dot today going to catch the red dot today. I could pee on this if I had the energy. Chew iPad power cord steal the warm chair right after you get up for purr for no reason leave hair everywhere, decide to want nothing to do with my owner today.",
    "title": "Top 15 Things to do When You are Bored",
    "subtitle": "Are you bored? Don't know what to do? Try these top 15 activities."
  },
  {
    "id": 3,
    "body": "Cupcake ipsum dolor. Sit amet marshmallow topping cheesecake muffin. Halvah croissant candy canes bonbon candy. Apple pie jelly beans topping carrot cake danish tart cake cheesecake. Muffin danish chocolate soufflé pastry icing bonbon oat cake. Powder cake jujubes oat cake. Lemon drops tootsie roll marshmallow halvah carrot cake.",
    "title": "Introduction to Intermittent Fasting",
    "subtitle": "Learn about the newest health craze."
  }
] """