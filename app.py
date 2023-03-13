from flask import jsonify, request


@app.route('/books', methods=['POST'])
def add_book():
    title = request.json.get('title')
    author_ids = request.json.get('authors', [])
    book = Book(title=title)
    for author_id in author_ids:
        author = Author.query.get(author_id)
        book.authors.append(author)
    db.session.add(book)
    db.session.commit()
    return jsonify({'success': True, 'message': 'Book added successfully.'}), 201

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify({'success': True, 'data': [{'id': book.id, 'title': book.title, 'is_on_shelf': book.is_on_shelf} for book in books]}), 200

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'success': False, 'message': 'Book not found.'}), 404
    db.session.delete(book)
    db.session.commit()
    return jsonify({'success': True, 'message': 'Book deleted successfully.'}), 200


if __name__ == "__main__":
  app.run(debug=True)
  
