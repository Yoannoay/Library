from application import app, db
from application.models import Author, Book, Review
from flask import render_template, Response, request, redirect, url_for, jsonify
from os import getenv


@app.route('/create/author', methods=['POST'])

def create_author():
    package = request.json
    new_author = Author(name=package["name"])
    db.session.add(new_author)
    db.session.commit()
    return Response(f"The author: {new_task.description}, has been added to the database", mimetype='text/plain')

@app.route('/create/book', methods=['POST'])

def create_book():
    package = request.json
    new_task = Tasks(description=package["description"])
    db.session.add(new_task)
    db.session.commit()
    return Response(f"Added task with description: {new_task.description}", mimetype='text/plain')
    
@app.route('/create/review', methods=['POST'])

def create_review():
    package = request.json
    new_review = Review(description=package["description"])
    db.session.add(new_task)
    db.session.commit()
    return Response(f"Added task with description: {new_task.description}", mimetype='text/plain')


# @app.route('/read/allTasks', methods=['GET'])
# def read_tasks():
#     all_tasks = Tasks.query.all()
#     tasks_dict = {"tasks": []}
#     for task in all_tasks:
#         tasks_dict["tasks"].append(
#             {
#                 "id": "task.id"
#                 "description": task.description,
#                 "completed": task.completed
#             }
#         )
#     return jsonify(tasks_dict)

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