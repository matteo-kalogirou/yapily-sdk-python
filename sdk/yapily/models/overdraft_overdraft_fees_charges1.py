# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.231
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class OverdraftOverdraftFeesCharges1(object):
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
        'overdraft_fee_charge_cap': 'list[OverdraftOverdraftFeeChargeCap]',
        'overdraft_fee_charge_detail': 'list[OverdraftOverdraftFeeChargeDetail]'
    }

    attribute_map = {
        'overdraft_fee_charge_cap': 'OverdraftFeeChargeCap',
        'overdraft_fee_charge_detail': 'OverdraftFeeChargeDetail'
    }

    def __init__(self, overdraft_fee_charge_cap=None, overdraft_fee_charge_detail=None, local_vars_configuration=None):  # noqa: E501
        """OverdraftOverdraftFeesCharges1 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._overdraft_fee_charge_cap = None
        self._overdraft_fee_charge_detail = None
        self.discriminator = None

        if overdraft_fee_charge_cap is not None:
            self.overdraft_fee_charge_cap = overdraft_fee_charge_cap
        if overdraft_fee_charge_detail is not None:
            self.overdraft_fee_charge_detail = overdraft_fee_charge_detail

    @property
    def overdraft_fee_charge_cap(self):
        """Gets the overdraft_fee_charge_cap of this OverdraftOverdraftFeesCharges1.  # noqa: E501


        :return: The overdraft_fee_charge_cap of this OverdraftOverdraftFeesCharges1.  # noqa: E501
        :rtype: list[OverdraftOverdraftFeeChargeCap]
        """
        return self._overdraft_fee_charge_cap

    @overdraft_fee_charge_cap.setter
    def overdraft_fee_charge_cap(self, overdraft_fee_charge_cap):
        """Sets the overdraft_fee_charge_cap of this OverdraftOverdraftFeesCharges1.


        :param overdraft_fee_charge_cap: The overdraft_fee_charge_cap of this OverdraftOverdraftFeesCharges1.  # noqa: E501
        :type: list[OverdraftOverdraftFeeChargeCap]
        """

        self._overdraft_fee_charge_cap = overdraft_fee_charge_cap

    @property
    def overdraft_fee_charge_detail(self):
        """Gets the overdraft_fee_charge_detail of this OverdraftOverdraftFeesCharges1.  # noqa: E501


        :return: The overdraft_fee_charge_detail of this OverdraftOverdraftFeesCharges1.  # noqa: E501
        :rtype: list[OverdraftOverdraftFeeChargeDetail]
        """
        return self._overdraft_fee_charge_detail

    @overdraft_fee_charge_detail.setter
    def overdraft_fee_charge_detail(self, overdraft_fee_charge_detail):
        """Sets the overdraft_fee_charge_detail of this OverdraftOverdraftFeesCharges1.


        :param overdraft_fee_charge_detail: The overdraft_fee_charge_detail of this OverdraftOverdraftFeesCharges1.  # noqa: E501
        :type: list[OverdraftOverdraftFeeChargeDetail]
        """

        self._overdraft_fee_charge_detail = overdraft_fee_charge_detail

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
        if not isinstance(other, OverdraftOverdraftFeesCharges1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OverdraftOverdraftFeesCharges1):
            return True

        return self.to_dict() != other.to_dict()
