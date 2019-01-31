# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.74
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from yapily.models.duration import Duration  # noqa: F401,E501


class TemporalUnit(object):
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
        'date_based': 'bool',
        'duration': 'Duration',
        'duration_estimated': 'bool',
        'time_based': 'bool'
    }

    attribute_map = {
        'date_based': 'dateBased',
        'duration': 'duration',
        'duration_estimated': 'durationEstimated',
        'time_based': 'timeBased'
    }

    def __init__(self, date_based=None, duration=None, duration_estimated=None, time_based=None):  # noqa: E501
        """TemporalUnit - a model defined in Swagger"""  # noqa: E501

        self._date_based = None
        self._duration = None
        self._duration_estimated = None
        self._time_based = None
        self.discriminator = None

        if date_based is not None:
            self.date_based = date_based
        if duration is not None:
            self.duration = duration
        if duration_estimated is not None:
            self.duration_estimated = duration_estimated
        if time_based is not None:
            self.time_based = time_based

    @property
    def date_based(self):
        """Gets the date_based of this TemporalUnit.  # noqa: E501


        :return: The date_based of this TemporalUnit.  # noqa: E501
        :rtype: bool
        """
        return self._date_based

    @date_based.setter
    def date_based(self, date_based):
        """Sets the date_based of this TemporalUnit.


        :param date_based: The date_based of this TemporalUnit.  # noqa: E501
        :type: bool
        """

        self._date_based = date_based

    @property
    def duration(self):
        """Gets the duration of this TemporalUnit.  # noqa: E501


        :return: The duration of this TemporalUnit.  # noqa: E501
        :rtype: Duration
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TemporalUnit.


        :param duration: The duration of this TemporalUnit.  # noqa: E501
        :type: Duration
        """

        self._duration = duration

    @property
    def duration_estimated(self):
        """Gets the duration_estimated of this TemporalUnit.  # noqa: E501


        :return: The duration_estimated of this TemporalUnit.  # noqa: E501
        :rtype: bool
        """
        return self._duration_estimated

    @duration_estimated.setter
    def duration_estimated(self, duration_estimated):
        """Sets the duration_estimated of this TemporalUnit.


        :param duration_estimated: The duration_estimated of this TemporalUnit.  # noqa: E501
        :type: bool
        """

        self._duration_estimated = duration_estimated

    @property
    def time_based(self):
        """Gets the time_based of this TemporalUnit.  # noqa: E501


        :return: The time_based of this TemporalUnit.  # noqa: E501
        :rtype: bool
        """
        return self._time_based

    @time_based.setter
    def time_based(self, time_based):
        """Sets the time_based of this TemporalUnit.


        :param time_based: The time_based of this TemporalUnit.  # noqa: E501
        :type: bool
        """

        self._time_based = time_based

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
        if not isinstance(other, TemporalUnit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
