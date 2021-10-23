import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output(self):
        rv = self.app.get('/?name=test&output=json')
        self.assertEqual(b'{"imie": "test", "msg": "Hello World!"}', rv.data)

    def test_xml(self):
        rv = self.app.get('/?name=agata&output=xml')
        self.assertEqual(b'<greetings><imie>agata</imie><msg>Hello World!</msg></greetings>', rv.data)
