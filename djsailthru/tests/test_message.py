from djsailthru.mail.message import SailthruEmailMessage
from djsailthru.tests.mock_backend import SailthruBackendMockTestCase


class TestSailthruEamilMessage(SailthruBackendMockTestCase):
    def setUp(self):
        super(TestSailthruEamilMessage, self).setUp()
        self.message = SailthruEmailMessage('foo@bar.com', 'Email Template')

    def test_send_mail_without_vars(self):
        self.message.send()
        self.assert_sailthru_called()
        data = self.get_api_call_data()
        self.assertEqual(data['template'], 'Email Template')
        self.assertEqual(data['email'], 'foo@bar.com')
        self.assertEqual(data['vars'], {})

    def test_send_email_with_vars(self):
        params = {'foo': 'bar'}
        message = SailthruEmailMessage('foo@bar.com', 'Email Template', vars=params)
        message.send()
        self.assert_sailthru_called()
        data = self.get_api_call_data()
        self.assertEqual(data['template'], 'Email Template')
        self.assertEqual(data['email'], 'foo@bar.com')
        self.assertEqual(data['vars'], {'vars': params})
