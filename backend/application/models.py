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

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=True)
    

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    rating = db.Column(db.Integer, nullable=True)
    thoughts = db.Column(db.String(150), nullable=True)

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=True)
