# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.205
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.consent_auth_code_request import ConsentAuthCodeRequest  # noqa: E501
from yapily.rest import ApiException

class TestConsentAuthCodeRequest(unittest.TestCase):
    """ConsentAuthCodeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ConsentAuthCodeRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.consent_auth_code_request.ConsentAuthCodeRequest()  # noqa: E501
        if include_optional :
            return ConsentAuthCodeRequest(
                auth_code = '0', 
                auth_state = '0'
            )
        else :
            return ConsentAuthCodeRequest(
                auth_code = '0',
                auth_state = '0',
        )

    def testConsentAuthCodeRequest(self):
        """Test ConsentAuthCodeRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
