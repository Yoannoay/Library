from application import app, db
from application.models import Author, Book, Review
from flask import render_template, Response, request, redirect, url_for, jsonify
from os import getenv
import json

# CREATE ROUTES FOR ALL CLASSES

@app.route('/create/author', methods=['POST'])

def create_author():
    package = request.json
    new_author = Author(name=package["name"])
    db.session.add(new_author)
    db.session.commit()
    return Response(f"The author: {new_author.name}, has been added to the database with id {new_author.id}", mimetype='text/plain')


@app.route('/create/book/<int:id>', methods=['POST'])

def create_book(id):
    package = request.json

    new_book = Book(name=package["name"], author_id=id)
    db.session.add(new_book)
    db.session.commit()
    return Response(f"The book: {new_book.name}, written by {new_book.author.name}, has been added to the database under the id {new_book.id}", mimetype='text/plain')

    
@app.route('/create/review', methods=['POST'])

def create_review():
    package = request.json

    new_review = Review(rating=package["rating"], thoughts=package["thoughts"], book_id=package["book_id"])
    db.session.add(new_review)
    db.session.commit()
    return Response(f"Thank you for adding your review and rating to the database, id: {new_review.id}", mimetype='text/plain')




# READ ROUTES FOR ALL CLASSES




@app.route('/allauthors', methods=['GET'])
def all_authors():

    author_list = Author.query.all()
    authors = {"author_list": []}

    for writer in author_list:

        books = []

        for book in writer.books:

            books.append(book.name)

        authors["author_list"].append(
            {
                "Author ID: ": writer.id,
                "Author": writer.name,
                "Books": books
                
            }
        )
    
    return jsonify(authors)


@app.route('/allbooks', methods=['GET'])
def all_books():
    book_list = Book.query.all()
    books = {"book_list": []}
    for book in book_list:
        books["book_list"].append(
            {
                "Book": book.name,
                "Book ID: ": book.id,
                "author": book.author.name,
                "author id": book.author.id 
            }
        )
      
    return jsonify(books)

            
@app.route('/allreviews', methods=['GET'])
def read_allreviews():
    all_reviews = Review.query.all()
    review_dict = {"all reviews": []}
    for review in all_reviews:
        review_dict["all reviews"].append(
            {
                "Book": review.book.name,
                "Author": review.book.author.name,
                "Rating": review.rating,
                "Review": review.thoughts,
                "Review ID: ": review.id

            }
        )
    return jsonify(review_dict)



# UPDATE ROUTES FOR ALL CLASSES



@app.route('/update/author/<int:id>', methods=['PUT'])
def update_author(id):
    package= request.json
    author = Author.query.get(id)

    author.name = package["name"]
    db.session.commit()
    return Response(f"Updated Author {id}, to {author.name}", mimetype='test/plain')


@app.route('/update/book/<int:id>', methods=['PUT'])
def update_book(id):
    package= request.json
    book = Book.query.get(id)

    book.name = package["name"]
    db.session.commit()
    return Response(f"Updated Book {id}, to {book.name}", mimetype='test/plain')


@app.route('/update/review/<int:id>', methods=['PUT'])
def update_review(id):
    package= request.json
    review = Review.query.get(id)
    
    review.thoughts = package["thoughts"]
    review.rating = package["rating"]
    db.session.commit()
    return Response(f"Updated review of  \"{review.book.name}\", changed rating to \"{review.rating}\" and thoughts to \"{review.thoughts}\" ", mimetype='test/plain')



# DELETE ROUTES FOR ALL CLASSES



@app.route('/delete/author/<int:id>', methods=['DELETE'])
def delete_author(id):
    author = Author.query.get(id)
    # for books in author.books:
    #     db.session.delete(books.name)

    # for review in author.book:
    #     db.session.delete(review.thoughts)
    #     db.session.delete(review.rating)
   
    db.session.delete(author)
    db.session.commit()
    return Response(f"Deleted: {author.name}")

@app.route('/delete/book/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return Response(f"{book.name} : has been deleted")


@app.route('/delete/review/<int:id>', methods=['DELETE'])
def delete_review(id):
    review = Review.query.get(id)
    db.session.delete(review)
    db.session.commit()
    return Response(f"Deleted review: {review.id}")


