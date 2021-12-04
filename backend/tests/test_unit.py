from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Author, Book, Review

class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        # Will be called before every test
        db.create_all()
        db.session.add(Author(name="Pytest"))
        db.session.add(Book(name="The adventures of Pytest"))
        db.session.add(Review(rating=5, thoughts="Boring book but good for testing"))

        db.session.commit()

    def tearDown(self):
        # Will be called after every test
        db.session.remove()
        db.drop_all()



class TestRead(TestBase):

    def test_viewauthors(self):
        response = self.client.get(url_for('all_authors'))
        authors = {
    "author_list": [
        {
            "Author": "Pytest",
            "Author ID: ": 1,
            "Books": [
                {
                    "ID": 1,
                    "name": "The adventures of Pytest"
                }
            ]
        }
    ]
}
        self.assertEquals(authors, response.json)
    



    def test_viewbooks(self):
        response = self.client.get(url_for('all_books'))
        books = {
    "book_list": [
        {
            "Book": "The adventures of Pytest",
            "Book ID: ": 1,
            "author": "Pytest",
            "author id": 1
        }
    ]
}
        self.assertEquals(books, response.data)
    


    def test_viewreviews(self):
        response = self.client.get(url_for('read_allreviews'))
        reviews = {
    "all reviews": [
        {
            "Author": "Pytest",
            "Book": "The adventures of Pytest",
            "Rating": 5,
            "Review": "Boring book but good for testing",
            "Review ID: ": 1
        }
    ]
}
        self.assertEquals(reviews, response.data)



class TestCreate(TestBase):

    def test_authorcreate(self):
        response = self.client.post(
            url_for('create_author'),
            json={"name": "Pytest"},
            follow_redirects=True
        )
        self.assertEquals(b"The author: Pytest, has been added to the database with id 1", response.data)
   
    def test_bookcreate(self):
        response = self.client.post(
            url_for('create_book'),
            data={"name": "The adventures of Pytest"},
            follow_redirects=True
        )
        self.assertEquals(b"The book: {new_book.name}, written by {new_book.author.name}, has been added to the database under the id {new_book.id}", response.data)
   
    def test_reviewcreate(self):
        response = self.client.post(
            url_for('create_review'),
            data={"rating": 5, "thoughts": "Boring book but good for testing"},
            follow_redirects=True
        )
        self.assertIn(b"Thank you for adding your review and rating to the database, id: 1", response.data)
    
class TestUpdate(TestBase):

    def test_updateauthor(self):
        response = self.client.put(
            url_for('update_author', id=1),
            data={"name": "Pytest"},
            follow_redirects=True
        )
        self.assertIn(b"Updated Author 1, to Pytest", response.data)
    
    def test_updatebook(self):
        response = self.client.put(
            url_for('update_book', id=1),
            data={"name": "The adventures of Pytest"},
            follow_redirects=True
        )
        self.assertIn(b"Updated Book 1, to The adventures of Pytest", response.data)
    
    def test_updatereview(self):
        response = self.client.put(
            url_for('update_review', id=1),
            data={"rating": 5, "thoughts": "Boring book but good for testing"},
            follow_redirects=True
        )
        self.assertIn(b"Updated review of The adventures of Pytest, changed rating to 5 and thoughts to Boring book but good for testing ", response.data)
    
        

class TestDelete(TestBase):

    def test_delete_author(self):
        response = self.client.get(
            url_for('delete_author', id=1),
            follow_redirects=True
        )
        self.assertNotIn("Deleted: Pytest}", response.data)
    
    def test_delete_book(self):
        response = self.client.get(
            url_for('delete_book', id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"The adventures of Pytest} : has been deleted", response.data)
    
    def test_delete_review(self):
        response = self.client.get(
            url_for('delete_review', id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"Deleted review: 1", response.data)
