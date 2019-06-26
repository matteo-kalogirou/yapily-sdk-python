# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.118
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CreditCheck(object):
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
        'notes': 'list[str]',
        'scoring_type': 'str'
    }

    attribute_map = {
        'notes': 'Notes',
        'scoring_type': 'ScoringType'
    }

    def __init__(self, notes=None, scoring_type=None):  # noqa: E501
        """CreditCheck - a model defined in Swagger"""  # noqa: E501

        self._notes = None
        self._scoring_type = None
        self.discriminator = None

        if notes is not None:
            self.notes = notes
        if scoring_type is not None:
            self.scoring_type = scoring_type

    @property
    def notes(self):
        """Gets the notes of this CreditCheck.  # noqa: E501


        :return: The notes of this CreditCheck.  # noqa: E501
        :rtype: list[str]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this CreditCheck.


        :param notes: The notes of this CreditCheck.  # noqa: E501
        :type: list[str]
        """

        self._notes = notes

    @property
    def scoring_type(self):
        """Gets the scoring_type of this CreditCheck.  # noqa: E501


        :return: The scoring_type of this CreditCheck.  # noqa: E501
        :rtype: str
        """
        return self._scoring_type

    @scoring_type.setter
    def scoring_type(self, scoring_type):
        """Sets the scoring_type of this CreditCheck.


        :param scoring_type: The scoring_type of this CreditCheck.  # noqa: E501
        :type: str
        """
        allowed_values = ["Hard", "Soft"]  # noqa: E501
        if scoring_type not in allowed_values:
            raise ValueError(
                "Invalid value for `scoring_type` ({0}), must be one of {1}"  # noqa: E501
                .format(scoring_type, allowed_values)
            )

        self._scoring_type = scoring_type

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
        if not isinstance(other, CreditCheck):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
