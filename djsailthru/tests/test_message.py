from djsailthru.mail.message import SailthruEmailMessage
from djsailthru.tests.mock_backend import SailthruBackendMockTestCase


class TestSailthruEamilMessage(SailthruBackendMockTestCase):
    def setUp(self):
        super(TestSailthruEamilMessage, self).setUp()
        self.message = SailthruEmailMessage('foo@bar.com', 'Email Template')

    def test_send_mail(self):
        self.message.send()
        self.assert_sailthru_called()
        data = self.get_api_call_data()
        self.assertEqual(data['template'], 'Email Template')
        self.assertEqual(data['email'], 'foo@bar.com')




# def mock_sailthru_response(**kwargs):
#     """
#     Helper function for mocking the response object returned from the
#     sailthru API.
#     """
#     response = mock.Mock(spec=SailthruResponse, **kwargs)
#     return response


# MockSendSailthruEmail = mock_a_thing(
#     'sailthru.sailthru_client.SailthruClient.api_post',
#     return_value=mock_sailthru_response(**{
#         'get_body.return_value': {'email': 'nick@simpleenergy.com', 'send_id': 'UxZ-C_3VrAVBAAhS', 'send_key': None, 'status': 'unknown', 'template': 'Forgot Password'},
#         'is_ok.return_value': True,
#         'get_status_code.return_value': 200,
#         'json': {'email': 'nick@simpleenergy.com', 'send_id': 'UxZ-C_3VrAVBAAhS', 'send_key': None, 'status': 'unknown', 'template': 'Forgot Password'},
#     }),

# )
