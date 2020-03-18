# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.175
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from yapily.models.iso_code_details import IsoCodeDetails  # noqa: F401,E501


class IsoBankTransactionCode(object):
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
        'domain_code': 'IsoCodeDetails',
        'family_code': 'IsoCodeDetails',
        'sub_family_code': 'IsoCodeDetails'
    }

    attribute_map = {
        'domain_code': 'domainCode',
        'family_code': 'familyCode',
        'sub_family_code': 'subFamilyCode'
    }

    def __init__(self, domain_code=None, family_code=None, sub_family_code=None):  # noqa: E501
        """IsoBankTransactionCode - a model defined in Swagger"""  # noqa: E501

        self._domain_code = None
        self._family_code = None
        self._sub_family_code = None
        self.discriminator = None

        if domain_code is not None:
            self.domain_code = domain_code
        if family_code is not None:
            self.family_code = family_code
        if sub_family_code is not None:
            self.sub_family_code = sub_family_code

    @property
    def domain_code(self):
        """Gets the domain_code of this IsoBankTransactionCode.  # noqa: E501


        :return: The domain_code of this IsoBankTransactionCode.  # noqa: E501
        :rtype: IsoCodeDetails
        """
        return self._domain_code

    @domain_code.setter
    def domain_code(self, domain_code):
        """Sets the domain_code of this IsoBankTransactionCode.


        :param domain_code: The domain_code of this IsoBankTransactionCode.  # noqa: E501
        :type: IsoCodeDetails
        """

        self._domain_code = domain_code

    @property
    def family_code(self):
        """Gets the family_code of this IsoBankTransactionCode.  # noqa: E501


        :return: The family_code of this IsoBankTransactionCode.  # noqa: E501
        :rtype: IsoCodeDetails
        """
        return self._family_code

    @family_code.setter
    def family_code(self, family_code):
        """Sets the family_code of this IsoBankTransactionCode.


        :param family_code: The family_code of this IsoBankTransactionCode.  # noqa: E501
        :type: IsoCodeDetails
        """

        self._family_code = family_code

    @property
    def sub_family_code(self):
        """Gets the sub_family_code of this IsoBankTransactionCode.  # noqa: E501


        :return: The sub_family_code of this IsoBankTransactionCode.  # noqa: E501
        :rtype: IsoCodeDetails
        """
        return self._sub_family_code

    @sub_family_code.setter
    def sub_family_code(self, sub_family_code):
        """Sets the sub_family_code of this IsoBankTransactionCode.


        :param sub_family_code: The sub_family_code of this IsoBankTransactionCode.  # noqa: E501
        :type: IsoCodeDetails
        """

        self._sub_family_code = sub_family_code

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
        if not isinstance(other, IsoBankTransactionCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
