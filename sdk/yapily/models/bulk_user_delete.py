# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.188
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BulkUserDelete(object):
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
        'id': 'str',
        'status': 'str',
        'started_at': 'datetime',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'started_at': 'startedAt',
        'links': 'links'
    }

    def __init__(self, id=None, status=None, started_at=None, links=None):  # noqa: E501
        """BulkUserDelete - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._status = None
        self._started_at = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if started_at is not None:
            self.started_at = started_at
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this BulkUserDelete.  # noqa: E501


        :return: The id of this BulkUserDelete.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BulkUserDelete.


        :param id: The id of this BulkUserDelete.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this BulkUserDelete.  # noqa: E501


        :return: The status of this BulkUserDelete.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BulkUserDelete.


        :param status: The status of this BulkUserDelete.  # noqa: E501
        :type: str
        """
        allowed_values = ["IN_PROGRESS", "COMPLETED", "FAILED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def started_at(self):
        """Gets the started_at of this BulkUserDelete.  # noqa: E501


        :return: The started_at of this BulkUserDelete.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this BulkUserDelete.


        :param started_at: The started_at of this BulkUserDelete.  # noqa: E501
        :type: datetime
        """

        self._started_at = started_at

    @property
    def links(self):
        """Gets the links of this BulkUserDelete.  # noqa: E501


        :return: The links of this BulkUserDelete.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this BulkUserDelete.


        :param links: The links of this BulkUserDelete.  # noqa: E501
        :type: dict(str, str)
        """

        self._links = links

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
        if not isinstance(other, BulkUserDelete):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
