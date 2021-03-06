# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.242
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.payment_status_details import PaymentStatusDetails  # noqa: E501
from yapily.rest import ApiException

class TestPaymentStatusDetails(unittest.TestCase):
    """PaymentStatusDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaymentStatusDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.payment_status_details.PaymentStatusDetails()  # noqa: E501
        if include_optional :
            return PaymentStatusDetails(
                status = 'PENDING', 
                status_reason = '0', 
                status_reason_description = '0', 
                status_update_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                multi_authorisation_status = yapily.models.multi_authorisation.MultiAuthorisation(
                    status = '0', 
                    number_of_authorisation_required = 56, 
                    number_of_authorisation_received = 56, 
                    last_updated_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    expiration_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else :
            return PaymentStatusDetails(
        )

    def testPaymentStatusDetails(self):
        """Test PaymentStatusDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
