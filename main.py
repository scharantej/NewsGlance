
# Import the necessary modules.

import os
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy

# Create a Flask app.
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or "you-will-never-guess"

# Configure the database.
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL") or "sqlite:///db.sqlite"
db = SQLAlchemy(app)

# Define the NewsArticle model.
class NewsArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    publication_date = db.Column(db.Date, nullable=False)
    content = db.Column(db.Text, nullable=False)

# Define the home route.
@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")

# Define the route to get the news articles.
@app.route("/news")
def get_news_articles():
    """Get the news articles from the database and render the index page."""
    news_articles = NewsArticle.query.all()
    return render_template("index.html", news_articles=news_articles)

# Define the route to get a specific news article.
@app.route("/news/<int:news_article_id>")
def get_news_article(news_article_id):
    """Get a specific news article from the database and render the article page."""
    news_article = NewsArticle.query.get_or_404(news_article_id)
    return render_template("article.html", news_article=news_article)

# Start the app.
if __name__ == "__main__":
    app.run(debug=True)
