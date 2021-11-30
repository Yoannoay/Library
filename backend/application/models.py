from application import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    books = db.relationship('Book', backref='author')
    reviews =db.relationship('Review', backref='author')

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    reviews =db.relationship('Review', backref='book')
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    rating = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(500), nullable=True)

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
