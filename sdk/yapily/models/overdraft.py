# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.119
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from yapily.models.overdraft_overdraft_tier_band_set import OverdraftOverdraftTierBandSet  # noqa: F401,E501


class Overdraft(object):
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
        'overdraft_tier_band_set': 'list[OverdraftOverdraftTierBandSet]',
        'tcs_and_cs_url': 'str'
    }

    attribute_map = {
        'notes': 'Notes',
        'overdraft_tier_band_set': 'OverdraftTierBandSet',
        'tcs_and_cs_url': 'TcsAndCsURL'
    }

    def __init__(self, notes=None, overdraft_tier_band_set=None, tcs_and_cs_url=None):  # noqa: E501
        """Overdraft - a model defined in Swagger"""  # noqa: E501

        self._notes = None
        self._overdraft_tier_band_set = None
        self._tcs_and_cs_url = None
        self.discriminator = None

        if notes is not None:
            self.notes = notes
        if overdraft_tier_band_set is not None:
            self.overdraft_tier_band_set = overdraft_tier_band_set
        if tcs_and_cs_url is not None:
            self.tcs_and_cs_url = tcs_and_cs_url

    @property
    def notes(self):
        """Gets the notes of this Overdraft.  # noqa: E501


        :return: The notes of this Overdraft.  # noqa: E501
        :rtype: list[str]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Overdraft.


        :param notes: The notes of this Overdraft.  # noqa: E501
        :type: list[str]
        """

        self._notes = notes

    @property
    def overdraft_tier_band_set(self):
        """Gets the overdraft_tier_band_set of this Overdraft.  # noqa: E501


        :return: The overdraft_tier_band_set of this Overdraft.  # noqa: E501
        :rtype: list[OverdraftOverdraftTierBandSet]
        """
        return self._overdraft_tier_band_set

    @overdraft_tier_band_set.setter
    def overdraft_tier_band_set(self, overdraft_tier_band_set):
        """Sets the overdraft_tier_band_set of this Overdraft.


        :param overdraft_tier_band_set: The overdraft_tier_band_set of this Overdraft.  # noqa: E501
        :type: list[OverdraftOverdraftTierBandSet]
        """

        self._overdraft_tier_band_set = overdraft_tier_band_set

    @property
    def tcs_and_cs_url(self):
        """Gets the tcs_and_cs_url of this Overdraft.  # noqa: E501


        :return: The tcs_and_cs_url of this Overdraft.  # noqa: E501
        :rtype: str
        """
        return self._tcs_and_cs_url

    @tcs_and_cs_url.setter
    def tcs_and_cs_url(self, tcs_and_cs_url):
        """Sets the tcs_and_cs_url of this Overdraft.


        :param tcs_and_cs_url: The tcs_and_cs_url of this Overdraft.  # noqa: E501
        :type: str
        """

        self._tcs_and_cs_url = tcs_and_cs_url

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
        if not isinstance(other, Overdraft):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
