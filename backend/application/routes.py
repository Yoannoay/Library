from application import app, db
from application.models import Author, Book, Review
from flask import render_template, Response, request, redirect, url_for, jsonify
from os import getenv
import json



@app.route('/create/author', methods=['POST'])

def create_author():
    package = request.json
    new_author = Author(name=package["name"])
    db.session.add(new_author)
    db.session.commit()
    return Response(f"The author: {new_author.name}, has been added to the database", mimetype='text/plain')

@app.route('/<int:id>/create/book', methods=['POST'])

def create_book(id):
    package = request.json
    author = Author.query.get(id)

    new_book = Book(name=package["name"], author_id=package["author_id"])
    db.session.add(new_book)
    db.session.commit()
    return Response(f"The book: {new_book.name}, has been added to the database", mimetype='text/plain')

    #     package= request.json
    # task = Tasks.query.get(id)


    # task.description = package["description"]
    # db.session.commit()
    # return Response(f"Updated task (ID: {id}): {task.description}", mimetype='text/plain')
    
@app.route('/create/review/<int:authorid>/<int:bookid>', methods=['POST'])

def create_review(authorid, bookid):
    package = request.json
    # writer = Author.query author 
    # book getter 
    new_review = Review(rating=package["rating"], thoughts=package["thoughts"], author_id=package["author_id"], book_id=package["book_id"])
    db.session.add(new_review)
    db.session.commit()
    return Response("Thank you for adding your review and rating to the database", mimetype='text/plain')

@app.route('/allauthors', methods=['GET'])
def all_authors():

    author_list = Author.query.all()
    authors = {"author_list": []}
    for author in author_list:
        books = []
        # data = Books.query.filter_by(id=author[1]).all())
        # books["has written"].append(data)
        authors["author_list"].append(
            {
                "Author": author.name,
                "Books": author.books.id.name.all()
            }
        )
    # if author.id 
    # books = []
    #     book = author.books
    return jsonify(authors)


@app.route('/allbooks', methods=['GET'])
def all_books():
    book_list = Book.query.all()
    books = {"book_list": []}
    for book in book_list:
        books["book_list"].append(
            {
                "Book": book.name,
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
                "Author": review.author.name,
                "Rating": review.rating,
                "Review": review.thoughts

            }
        )
    return jsonify(review_dict)

# @app.route('/update/task/<int:id>', methods=['PUT'])
# def update_task(id):
#     package= request.json
#     task = Tasks.query.get(id)


#     task.description = package["description"]
#     db.session.commit()
#     return Response(f"Updated task (ID: {id}): {task.description}", mimetype='text/plain')


# @app.route('/delete/task/<int:id>', methods= ['DELETE'])
# def delete_task(id):
#     task = Tasks.query.get(id)
#     db.session.delete(task)
#     db.session.commit()
#     return Response(f"Deleted task with ID: {id}")

# @app.route('/complete/task/<int:id>', methods=['PUT'])
# def complete_task(id):
#     task = Tasks.query.get(id)
#     task.completed = True
#     db.session.commit()
#     return Response(f"Task with ID: {id} set to complete")

# @app.route('/incomplete/task/<int:id>', methods=['PUT'])
# def incomplete_task(id):
#     task = Tasks.query.get(id)
#     task.completed = False
#     db.session.commit()
#     return Response(f"Task with ID: {id} set to incomplete")