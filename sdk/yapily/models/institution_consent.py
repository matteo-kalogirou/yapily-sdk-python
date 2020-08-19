# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.225
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class InstitutionConsent(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'institution_id': 'str'
    }

    attribute_map = {
        'institution_id': 'institutionId'
    }

    def __init__(self, institution_id=None, local_vars_configuration=None):  # noqa: E501
        """InstitutionConsent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._institution_id = None
        self.discriminator = None

        if institution_id is not None:
            self.institution_id = institution_id

    @property
    def institution_id(self):
        """Gets the institution_id of this InstitutionConsent.  # noqa: E501


        :return: The institution_id of this InstitutionConsent.  # noqa: E501
        :rtype: str
        """
        return self._institution_id

    @institution_id.setter
    def institution_id(self, institution_id):
        """Sets the institution_id of this InstitutionConsent.


        :param institution_id: The institution_id of this InstitutionConsent.  # noqa: E501
        :type: str
        """

        self._institution_id = institution_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, InstitutionConsent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstitutionConsent):
            return True

        return self.to_dict() != other.to_dict()
