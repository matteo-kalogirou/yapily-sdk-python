# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.33
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AccountRequest(object):
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
        'transaction_from': 'datetime',
        'transaction_to': 'datetime',
        'expires_at': 'datetime'
    }

    attribute_map = {
        'transaction_from': 'transactionFrom',
        'transaction_to': 'transactionTo',
        'expires_at': 'expiresAt'
    }

    def __init__(self, transaction_from=None, transaction_to=None, expires_at=None):  # noqa: E501
        """AccountRequest - a model defined in Swagger"""  # noqa: E501

        self._transaction_from = None
        self._transaction_to = None
        self._expires_at = None
        self.discriminator = None

        self.transaction_from = transaction_from
        self.transaction_to = transaction_to
        self.expires_at = expires_at

    @property
    def transaction_from(self):
        """Gets the transaction_from of this AccountRequest.  # noqa: E501


        :return: The transaction_from of this AccountRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._transaction_from

    @transaction_from.setter
    def transaction_from(self, transaction_from):
        """Sets the transaction_from of this AccountRequest.


        :param transaction_from: The transaction_from of this AccountRequest.  # noqa: E501
        :type: datetime
        """
        if transaction_from is None:
            raise ValueError("Invalid value for `transaction_from`, must not be `None`")  # noqa: E501

        self._transaction_from = transaction_from

    @property
    def transaction_to(self):
        """Gets the transaction_to of this AccountRequest.  # noqa: E501


        :return: The transaction_to of this AccountRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._transaction_to

    @transaction_to.setter
    def transaction_to(self, transaction_to):
        """Sets the transaction_to of this AccountRequest.


        :param transaction_to: The transaction_to of this AccountRequest.  # noqa: E501
        :type: datetime
        """
        if transaction_to is None:
            raise ValueError("Invalid value for `transaction_to`, must not be `None`")  # noqa: E501

        self._transaction_to = transaction_to

    @property
    def expires_at(self):
        """Gets the expires_at of this AccountRequest.  # noqa: E501


        :return: The expires_at of this AccountRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this AccountRequest.


        :param expires_at: The expires_at of this AccountRequest.  # noqa: E501
        :type: datetime
        """
        if expires_at is None:
            raise ValueError("Invalid value for `expires_at`, must not be `None`")  # noqa: E501

        self._expires_at = expires_at

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
        if not isinstance(other, AccountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
