from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///home_library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/book/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        publication_date = request.form['publication_date']
        book = Book(title=title, publication_date=publication_date)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/author/add', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        name = request.form['name']
        author = Author(name=name)
        db.session.add(author)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_author.html')

@app.route('/book/<int:id>/edit', methods=['GET', 'POST'])
def edit_book(id):
    book = Book.query.get(id)
    if request.method == 'POST':
        book.title = request.form['title']
        book.publication_date = request.form['publication_date']
        db.session.commit()
        return redirect(url_for('index '))


if __name__ == "__main__":
  app.run(debug=True)
  
