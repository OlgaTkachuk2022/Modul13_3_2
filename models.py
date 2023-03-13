# app/models.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///home_library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

authors_books = db.Table('authors_books',
    db.Column('author_id', db.Integer, db.ForeignKey('author.id')),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'))
)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    books = db.relationship('Book', secondary=authors_books, backref=db.backref('authors', lazy='dynamic'))

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    is_on_shelf = db.Column(db.Boolean, default=True, nullable=False)
