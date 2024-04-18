import unittest
from app import app, db, Todo

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_task(self):
        response = self.app.post('/', data={'content': 'Test task content'})
        self.assertEqual(response.status_code, 302)  # Redirects to homepage

        with app.app_context():
            task = Todo.query.first()
            self.assertEqual(task.content, 'Test task content')

if __name__ == '__main__':
    unittest.main()
