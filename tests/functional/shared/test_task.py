
from requests import ConnectionError
from unittest import Testcase

from app.shared.task import Task

class TestSharedTask(TestCase):
    def setUp(self):
        pass
  
    def tearDown(self):
        pass

    def test_01_forward(self):
        url = 'http://www.google.com'
        method = 'GET'
        response = Task.forward(url, method=method)
        self.assertEqual('OK', response.reason)
        self.assertEqual(200, response.status_code)

    def test_02_throw_error(self):
        url = 'http://wwww.google.com'
        method = 'GET'
        self.assertRaises(ConnectionError, Task.forward(url, method=method)
