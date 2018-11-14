# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.40
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class FilterAndSort(object):
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
        'before': 'datetime',
        '_from': 'datetime',
        'limit': 'int',
        'sort': 'str'
    }

    attribute_map = {
        'before': 'before',
        '_from': 'from',
        'limit': 'limit',
        'sort': 'sort'
    }

    def __init__(self, before=None, _from=None, limit=None, sort=None):  # noqa: E501
        """FilterAndSort - a model defined in Swagger"""  # noqa: E501

        self._before = None
        self.__from = None
        self._limit = None
        self._sort = None
        self.discriminator = None

        if before is not None:
            self.before = before
        if _from is not None:
            self._from = _from
        if limit is not None:
            self.limit = limit
        if sort is not None:
            self.sort = sort

    @property
    def before(self):
        """Gets the before of this FilterAndSort.  # noqa: E501


        :return: The before of this FilterAndSort.  # noqa: E501
        :rtype: datetime
        """
        return self._before

    @before.setter
    def before(self, before):
        """Sets the before of this FilterAndSort.


        :param before: The before of this FilterAndSort.  # noqa: E501
        :type: datetime
        """

        self._before = before

    @property
    def _from(self):
        """Gets the _from of this FilterAndSort.  # noqa: E501


        :return: The _from of this FilterAndSort.  # noqa: E501
        :rtype: datetime
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this FilterAndSort.


        :param _from: The _from of this FilterAndSort.  # noqa: E501
        :type: datetime
        """

        self.__from = _from

    @property
    def limit(self):
        """Gets the limit of this FilterAndSort.  # noqa: E501


        :return: The limit of this FilterAndSort.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this FilterAndSort.


        :param limit: The limit of this FilterAndSort.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def sort(self):
        """Gets the sort of this FilterAndSort.  # noqa: E501


        :return: The sort of this FilterAndSort.  # noqa: E501
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this FilterAndSort.


        :param sort: The sort of this FilterAndSort.  # noqa: E501
        :type: str
        """
        allowed_values = ["date", "-date"]  # noqa: E501
        if sort not in allowed_values:
            raise ValueError(
                "Invalid value for `sort` ({0}), must be one of {1}"  # noqa: E501
                .format(sort, allowed_values)
            )

        self._sort = sort

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
        if not isinstance(other, FilterAndSort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
