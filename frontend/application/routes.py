from application import app

from application.forms import CreateAuthor, NewBook, NewReview

from flask import render_template, request, redirect, url_for, jsonify
import requests

backend_host = "library_backend:5000"


# ALL READ ROUTES

@app.route('/', methods= ['GET'])
@app.route('/home', methods= ['GET'])
def home():
    all_authors = requests.get(f"http://library_backend:5000/allauthors").json()["author_list"]
    return render_template('index.html', title="Home", all_authors=all_authors)


@app.route('/allreviews', methods= ['GET'])
def allreviews():
    all_reviews = requests.get(f"http://library_backend:5000/allreviews").json()["all reviews"]
    i = 0
    return render_template('allreviews.html', title="Home of Reviews", all_reviews=all_reviews)



# ALL CREATE ROUTES


@app.route('/create/author', methods=["GET", "POST"])
def create_author():
    form = CreateAuthor()
    

    if request.method == "POST":
        response = requests.post(
            f"http://library_backend:5000/create/author",
            json={
                "name": form.name.data,
            }
        )
        
        return redirect(url_for("home"))

    return render_template("create_author.html", title="Add Author", form=form)


@app.route('/create/book/<int:id>', methods=["GET", "POST"])
def create_book(id):
    form = NewBook()
    

    if request.method == "POST":
        response = requests.post(
            f"http://library_backend:5000/create/book",
            json={
                "name": form.name.data,
                "author_id": id
                } 
        )
        return redirect(url_for("home"))

    return render_template("create_book.html", title="New Book", form=form, id=id)


@app.route('/create/review/<int:id>', methods=["GET", "POST"])
def create_review(id):
    form = NewReview()
    book_id = id

    if request.method == "POST":
        response = requests.post(
            f"http://library_backend:5000/create/review",
            json={
                "rating": form.rating.data,
                "thoughts": form.thoughts.data,
                "book_id": book_id
                 } 
        )
        return redirect(url_for("allreviews"))

    return render_template("create_review.html", title="New Review", form=form, id=id)


@app.route('/update/review/<int:id>', methods=["GET", "PUT"])
def update_review(id):
    form = NewReview()
  

    if request.method == "PUT":
        response = requests.put(
            f"http://library_backend:5000/create/review",
            json={
                "rating": form.rating.data,
                "thoughts": form.thoughts.data,
                "review_id": id
                 } 
        )
        return redirect(url_for("allreviews"))

    return render_template("create_review.html", title="New Review", form=form, id=id)






# @app.route('/update/author/<int:id>', methods=['GET','POST'])
# def update_task(id):
#     form = TaskForm()
#     task = requests.get(f"http://{backend_host}/read/task/{id}").json()
#     app.logger.info(f"Task: {task}")

#     if request.method == "POST":
#         response = requests.put(
#             f"http://{backend_host}/update/task/{id}",
#             json={"description": form.description.data}
#         )
#         return redirect(url_for('home'))

#     return render_template('update_task.html', task=task, form=form)

# @app.route('/delete/task/<int:id>')
# def delete_task(id):
#     task = Tasks.query.get(id)
#     db.session.delete(task)
#     db.session.commit()
#     return redirect(url_for('home'))

# @app.route('/complete/task/<int:id>')
# def complete_task(id):
#     task = Tasks.query.get(id)
#     task.completed = True
#     db.session.commit()
#     return redirect(url_for('home'))

# @app.route('/incomplete/task/<int:id>')
# def incomplete_task(id):
#     task = Tasks.query.get(id)
#     task.completed = False
#     db.session.commit()
#     return redirect(url_for('home'))