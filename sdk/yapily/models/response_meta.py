# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.181
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ResponseMeta(object):
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
        'tracing_id': 'str'
    }

    attribute_map = {
        'tracing_id': 'tracingId'
    }

    def __init__(self, tracing_id=None):  # noqa: E501
        """ResponseMeta - a model defined in Swagger"""  # noqa: E501

        self._tracing_id = None
        self.discriminator = None

        if tracing_id is not None:
            self.tracing_id = tracing_id

    @property
    def tracing_id(self):
        """Gets the tracing_id of this ResponseMeta.  # noqa: E501


        :return: The tracing_id of this ResponseMeta.  # noqa: E501
        :rtype: str
        """
        return self._tracing_id

    @tracing_id.setter
    def tracing_id(self, tracing_id):
        """Sets the tracing_id of this ResponseMeta.


        :param tracing_id: The tracing_id of this ResponseMeta.  # noqa: E501
        :type: str
        """

        self._tracing_id = tracing_id

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
        if not isinstance(other, ResponseMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
