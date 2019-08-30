# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.137
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Country(object):
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
        'country_code2': 'str',
        'display_name': 'str'
    }

    attribute_map = {
        'country_code2': 'countryCode2',
        'display_name': 'displayName'
    }

    def __init__(self, country_code2=None, display_name=None):  # noqa: E501
        """Country - a model defined in Swagger"""  # noqa: E501

        self._country_code2 = None
        self._display_name = None
        self.discriminator = None

        if country_code2 is not None:
            self.country_code2 = country_code2
        if display_name is not None:
            self.display_name = display_name

    @property
    def country_code2(self):
        """Gets the country_code2 of this Country.  # noqa: E501


        :return: The country_code2 of this Country.  # noqa: E501
        :rtype: str
        """
        return self._country_code2

    @country_code2.setter
    def country_code2(self, country_code2):
        """Sets the country_code2 of this Country.


        :param country_code2: The country_code2 of this Country.  # noqa: E501
        :type: str
        """

        self._country_code2 = country_code2

    @property
    def display_name(self):
        """Gets the display_name of this Country.  # noqa: E501


        :return: The display_name of this Country.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Country.


        :param display_name: The display_name of this Country.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

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
        if not isinstance(other, Country):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
