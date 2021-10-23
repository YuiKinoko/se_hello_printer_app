import unittest
import json
import xml.etree.cElementTree as ET
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
        self.assertEqual(json.dumps({
            'imie': 'test',
            'msg': 'Hello World!'
        }), rv.data.decode())

    def test_xml(self):
        rv = self.app.get('/?name=test&output=xml')
        greetings = ET.Element("greetings")

        ET.SubElement(greetings, "imie").text = 'test'
        ET.SubElement(greetings, "msg").text = 'Hello World!'

        s = ET.tostring(greetings)

        self.assertEqual(s, rv.data)