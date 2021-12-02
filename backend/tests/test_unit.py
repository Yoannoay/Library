from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Author, Book, Review

class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            SQLALCHEMY_DATABASE_URI={DATABASE_URI},
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

class TestViews(TestBase):
    # Test whether we get a successful response from our routes
    def test_authorcreate_get(self):
        response = self.client.get(url_for('create_author'))
        self.assert200(response)
    
    def test_bookcreate_get(self):
        response = self.client.get(url_for('create_book'))
        self.assert200(response)

    def test_reviewcreate_get(self):
        response = self.client.get(url_for('create_review'))
        self.assert200(response)

    def test_viewauthors_get(self):
        response = self.client.get(url_for('all_authors'))
        self.assert200(response)
    
    def test_viewbooks_get(self):
        response = self.client.get(url_for('all_books'))
        self.assert200(response)

    def test_viewreviews_get(self):
        response = self.client.get(url_for('read_allreviews'))
        self.assert200(response)

    def test_update_author_get(self):
        response = self.client.get(url_for('update_author'))
        self.assert200(response)

    def test_update_book_get(self):
        response = self.client.get(url_for('update_book'))
        self.assert200(response)

    def test_update_review_get(self):
        response = self.client.get(url_for('update_review'))
        self.assert200(response)

    def test_authordelete_get(self):
        response = self.client.get(url_for('delete_author'))
        self.assert200(response)

    def test_bookdelete_get(self):
        response = self.client.get(url_for('delete_book'))
        self.assert200(response)

    def test_reviewdelete_get(self):
        response = self.client.get(url_for('delete_review'))
        self.assert200(response)




class TestRead(TestBase):

    def test_viewauthors(self):
        response = self.client.get(url_for('all_authors'))
        self.assertIn(b"Run unit tests", response.data)
    
    def test_viewbooks(self):
        response = self.client.get(url_for('all_books'))
        self.assertIn(b"Run unit tests", response.data)
    
    def test_viewreviews(self):
        response = self.client.get(url_for('read_allreviews'))
        self.assertIn(b"Run unit tests", response.data)

class TestCreate(TestBase):

    def test_authorcreate(self):
        response = self.client.post(
            url_for('create_author'),
            data={"description": "Testing create functionality"},
            follow_redirects=True
        )
        self.assertIn(b"Testing create functionality", response.data)
   
    def test_bookcreate(self):
        response = self.client.post(
            url_for('create_book'),
            data={"description": "Testing create functionality"},
            follow_redirects=True
        )
        self.assertIn(b"Testing create functionality", response.data)
   
    def test_reviewcreate(self):
        response = self.client.post(
            url_for('create_review'),
            data={"description": "Testing create functionality"},
            follow_redirects=True
        )
        self.assertIn(b"Testing create functionality", response.data)
    
class TestUpdate(TestBase):

    def test_updateauthor(self):
        response = self.client.post(
            url_for('update_author', id=1),
            data={"description": "Testing update functionality"},
            follow_redirects=True
        )
        self.assertIn(b"Testing update functionality", response.data)
    
    def test_updatebook(self):
        response = self.client.post(
            url_for('update_book', id=1),
            data={"description": "Testing update functionality"},
            follow_redirects=True
        )
        self.assertIn(b"Testing update functionality", response.data)
    
    def test_updatereview(self):
        response = self.client.post(
            url_for('update_review', id=1),
            data={"description": "Testing update functionality"},
            follow_redirects=True
        )
        self.assertIn(b"Testing update functionality", response.data)
    
        

class TestDelete(TestBase):

    def test_delete_author(self):
        response = self.client.get(
            url_for('delete_author', id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"Run unit tests", response.data)
    
    def test_delete_book(self):
        response = self.client.get(
            url_for('delete_book', id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"Run unit tests", response.data)
    
    def test_delete_review(self):
        response = self.client.get(
            url_for('delete_review', id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"Run unit tests", response.data)
