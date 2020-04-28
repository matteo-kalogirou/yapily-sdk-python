# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.182
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from yapily.models.account_identification import AccountIdentification  # noqa: F401,E501
from yapily.models.address import Address  # noqa: F401,E501


class Payer(object):
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
        'name': 'str',
        'address': 'Address',
        'account_identifications': 'list[AccountIdentification]'
    }

    attribute_map = {
        'name': 'name',
        'address': 'address',
        'account_identifications': 'accountIdentifications'
    }

    def __init__(self, name=None, address=None, account_identifications=None):  # noqa: E501
        """Payer - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._address = None
        self._account_identifications = None
        self.discriminator = None

        self.name = name
        if address is not None:
            self.address = address
        self.account_identifications = account_identifications

    @property
    def name(self):
        """Gets the name of this Payer.  # noqa: E501


        :return: The name of this Payer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Payer.


        :param name: The name of this Payer.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def address(self):
        """Gets the address of this Payer.  # noqa: E501


        :return: The address of this Payer.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Payer.


        :param address: The address of this Payer.  # noqa: E501
        :type: Address
        """

        self._address = address

    @property
    def account_identifications(self):
        """Gets the account_identifications of this Payer.  # noqa: E501


        :return: The account_identifications of this Payer.  # noqa: E501
        :rtype: list[AccountIdentification]
        """
        return self._account_identifications

    @account_identifications.setter
    def account_identifications(self, account_identifications):
        """Sets the account_identifications of this Payer.


        :param account_identifications: The account_identifications of this Payer.  # noqa: E501
        :type: list[AccountIdentification]
        """
        if account_identifications is None:
            raise ValueError("Invalid value for `account_identifications`, must not be `None`")  # noqa: E501

        self._account_identifications = account_identifications

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
        if not isinstance(other, Payer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
