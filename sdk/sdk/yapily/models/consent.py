# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Consent(object):
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
        'consent_token': 'str',
        'token_type': 'str'
    }

    attribute_map = {
        'consent_token': 'consentToken',
        'token_type': 'tokenType'
    }

    def __init__(self, consent_token=None, token_type=None):  # noqa: E501
        """Consent - a model defined in Swagger"""  # noqa: E501

        self._consent_token = None
        self._token_type = None
        self.discriminator = None

        if consent_token is not None:
            self.consent_token = consent_token
        if token_type is not None:
            self.token_type = token_type

    @property
    def consent_token(self):
        """Gets the consent_token of this Consent.  # noqa: E501


        :return: The consent_token of this Consent.  # noqa: E501
        :rtype: str
        """
        return self._consent_token

    @consent_token.setter
    def consent_token(self, consent_token):
        """Sets the consent_token of this Consent.


        :param consent_token: The consent_token of this Consent.  # noqa: E501
        :type: str
        """

        self._consent_token = consent_token

    @property
    def token_type(self):
        """Gets the token_type of this Consent.  # noqa: E501


        :return: The token_type of this Consent.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this Consent.


        :param token_type: The token_type of this Consent.  # noqa: E501
        :type: str
        """

        self._token_type = token_type

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
        if not isinstance(other, Consent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
