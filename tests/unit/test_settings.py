
from unittest import TestCase, main

from app.common.settings import config

class TestMain(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01_load_config(self):
        expected_keys = ['flask', 'aws', 'service', 'ms', 'token', 'log_level', 'logging']
        self.assertEqual(len(expected_keys), len(config.keys()))

    def test_02_flask_subkeys(self):
        expected_keys = ['api_version', 'debug']
        self.assertEqual(len(expected_keys), len(config['flask']))
        for ek in expected_keys:
            self.assertIn(ek, config['flask'])

    def test_03_aws_subkeys(self):
        expected_keys = ['access_key', 'secret_access_key', 'region', 'sqs_retry_limit', 'sns_retry_limit']
        self.assertEqual(len(expected_keys), len(config['aws']))
        for ek in expected_keys:
            self.assertIn(ek, config['aws'])

    def test_04_service_subkeys(self):
        expected_keys = ['max_attempts', 'ms']
        self.assertEqual(len(expected_keys), len(config['service']))
        for ek in expected_keys:
            self.assertIn(ek, config['service'])

    def test_05_ms_subkeys(self):
        expected_keys = ['item_api_version', 'po_api_version']
        self.assertEqual(len(expected_keys), len(config['ms']))
        for ek in expected_keys:
            self.assertIn(ek, config['ms'])

    def test_06_token_subkeys(self):
        expected_keys = ['expiration']
        self.assertEqual(len(expected_keys), len(config['token']))
        for ek in expected_keys:
            self.assertIn(ek, config['token'])

    def test_07_logging_subkeys(self):
        expected_keys = ['version', 'disable_existing_loggers', 'formatters',
                         'handlers', 'loggers']
        self.assertEqual(len(expected_keys), len(config['logging']))
        for ek in expected_keys:
            self.assertIn(ek, config['logging'])

