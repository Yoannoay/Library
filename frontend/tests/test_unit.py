from flask import url_for
from flask_testing import TestCase
from application import app
import requests_mock

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

class TestViews(TestBase):
    # Test whether we get a successful response from our routes
    def test_home_get(self):
        with requests_mock.Mocker() as m:
            all_authors= {
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
        m.get(f"http://library_backend:5000/allauthors", json=all_authors)
        response = self.client.get(url_for('home'))
        self.assert200(response)
    
    def test_create_book_get(self):
        response = self.client.get(url_for('create_book', id=1))
        self.assert200(response)

    def test_create_review_get(self):
        response = self.client.get(url_for('create_review', id=1))
        self.assert200(response)

    def test_create_author_get(self):
        response = self.client.get(url_for('create_author'))
        self.assert200(response)

    def test_read_reviews_get(self):
        with requests_mock.Mocker() as m:
            all_reviews: {
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
        response = self.client.get(url_for(f"http://library_backend:5000/allreviews"))
        self.assert200(response)

    

class TestRead(TestBase):

    def test_read_home(self):
        with requests_mock.Mocker() as m:
            all_authors= {
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
        m.get(f"http://library_backend:5000/allauthors", json=all_authors)

        response = self.client.get(url_for('home'))
        self.assertIn(b"Pytest", response.data)
    

class TestCreate(TestBase):

    def test_create_author(self):
        with requests_mock.Mocker() as m:
            all_authors = { "authors": [test_home,
            {
            "Author": "Pytest",
            "Author ID: ": 1,
            "Books": [
                {
                    "ID": 1,
                    "name": "The adventures of Pytest"
                }
            ]
        }]}
            m.post(f"http://library_backend:5000/create/author", data="Test text")
            m.get(f"http://library_backend:5000/allauthors", json=all_authors)
        response = self.client.post(
            url_for('create_author'),
            follow_redirects=True
        )
        self.assertIn(b, response.data)
    
        

