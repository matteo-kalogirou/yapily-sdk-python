# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.184
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from yapily.models.payment_request import PaymentRequest  # noqa: F401,E501


class BulkPaymentRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'execution_date_time': 'datetime',
        'originator_identification_number': 'str',
        'payments': 'list[PaymentRequest]'
    }

    attribute_map = {
        'execution_date_time': 'executionDateTime',
        'originator_identification_number': 'originatorIdentificationNumber',
        'payments': 'payments'
    }

    def __init__(self, execution_date_time=None, originator_identification_number=None, payments=None):  # noqa: E501
        """BulkPaymentRequest - a model defined in Swagger"""  # noqa: E501

        self._execution_date_time = None
        self._originator_identification_number = None
        self._payments = None
        self.discriminator = None

        if execution_date_time is not None:
            self.execution_date_time = execution_date_time
        if originator_identification_number is not None:
            self.originator_identification_number = originator_identification_number
        self.payments = payments

    @property
    def execution_date_time(self):
        """Gets the execution_date_time of this BulkPaymentRequest.  # noqa: E501

        Execution datetime for the bulk payments  # noqa: E501

        :return: The execution_date_time of this BulkPaymentRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._execution_date_time

    @execution_date_time.setter
    def execution_date_time(self, execution_date_time):
        """Sets the execution_date_time of this BulkPaymentRequest.

        Execution datetime for the bulk payments  # noqa: E501

        :param execution_date_time: The execution_date_time of this BulkPaymentRequest.  # noqa: E501
        :type: datetime
        """

        self._execution_date_time = execution_date_time

    @property
    def originator_identification_number(self):
        """Gets the originator_identification_number of this BulkPaymentRequest.  # noqa: E501

        Required field for AIB bulk payments  # noqa: E501

        :return: The originator_identification_number of this BulkPaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._originator_identification_number

    @originator_identification_number.setter
    def originator_identification_number(self, originator_identification_number):
        """Sets the originator_identification_number of this BulkPaymentRequest.

        Required field for AIB bulk payments  # noqa: E501

        :param originator_identification_number: The originator_identification_number of this BulkPaymentRequest.  # noqa: E501
        :type: str
        """

        self._originator_identification_number = originator_identification_number

    @property
    def payments(self):
        """Gets the payments of this BulkPaymentRequest.  # noqa: E501


        :return: The payments of this BulkPaymentRequest.  # noqa: E501
        :rtype: list[PaymentRequest]
        """
        return self._payments

    @payments.setter
    def payments(self, payments):
        """Sets the payments of this BulkPaymentRequest.


        :param payments: The payments of this BulkPaymentRequest.  # noqa: E501
        :type: list[PaymentRequest]
        """
        if payments is None:
            raise ValueError("Invalid value for `payments`, must not be `None`")  # noqa: E501

        self._payments = payments

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BulkPaymentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
