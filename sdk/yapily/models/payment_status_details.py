# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.132
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PaymentStatusDetails(object):
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
        'status': 'str',
        'status_reason': 'str',
        'status_reason_description': 'str',
        'status_update_date': 'datetime'
    }

    attribute_map = {
        'status': 'status',
        'status_reason': 'statusReason',
        'status_reason_description': 'statusReasonDescription',
        'status_update_date': 'statusUpdateDate'
    }

    def __init__(self, status=None, status_reason=None, status_reason_description=None, status_update_date=None):  # noqa: E501
        """PaymentStatusDetails - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._status_reason = None
        self._status_reason_description = None
        self._status_update_date = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if status_reason is not None:
            self.status_reason = status_reason
        if status_reason_description is not None:
            self.status_reason_description = status_reason_description
        if status_update_date is not None:
            self.status_update_date = status_update_date

    @property
    def status(self):
        """Gets the status of this PaymentStatusDetails.  # noqa: E501


        :return: The status of this PaymentStatusDetails.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PaymentStatusDetails.


        :param status: The status of this PaymentStatusDetails.  # noqa: E501
        :type: str
        """
        allowed_values = ["PENDING", "FAILED", "DECLINED", "COMPLETED", "EXPIRED", "UNKNOWN"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def status_reason(self):
        """Gets the status_reason of this PaymentStatusDetails.  # noqa: E501


        :return: The status_reason of this PaymentStatusDetails.  # noqa: E501
        :rtype: str
        """
        return self._status_reason

    @status_reason.setter
    def status_reason(self, status_reason):
        """Sets the status_reason of this PaymentStatusDetails.


        :param status_reason: The status_reason of this PaymentStatusDetails.  # noqa: E501
        :type: str
        """

        self._status_reason = status_reason

    @property
    def status_reason_description(self):
        """Gets the status_reason_description of this PaymentStatusDetails.  # noqa: E501


        :return: The status_reason_description of this PaymentStatusDetails.  # noqa: E501
        :rtype: str
        """
        return self._status_reason_description

    @status_reason_description.setter
    def status_reason_description(self, status_reason_description):
        """Sets the status_reason_description of this PaymentStatusDetails.


        :param status_reason_description: The status_reason_description of this PaymentStatusDetails.  # noqa: E501
        :type: str
        """

        self._status_reason_description = status_reason_description

    @property
    def status_update_date(self):
        """Gets the status_update_date of this PaymentStatusDetails.  # noqa: E501


        :return: The status_update_date of this PaymentStatusDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._status_update_date

    @status_update_date.setter
    def status_update_date(self, status_update_date):
        """Sets the status_update_date of this PaymentStatusDetails.


        :param status_update_date: The status_update_date of this PaymentStatusDetails.  # noqa: E501
        :type: datetime
        """

        self._status_update_date = status_update_date

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
        if not isinstance(other, PaymentStatusDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
