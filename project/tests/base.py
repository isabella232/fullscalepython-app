# project/server/tests/base.py


from flask.ext.testing import TestCase

from project.server import app, db
from project.server.models import User


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('project.server.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        user = User(
            email='ad@min.com',
            username='admin_user',
            password='admin_user',
            admin=True
        )
        duplicate_user = User(
            email='duplcate@user.com',
            username='duplicate_user',
            password='duplicate_user'
        )
        db.session.add(user)
        db.session.add(duplicate_user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()