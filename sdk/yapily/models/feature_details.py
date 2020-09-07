# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.236
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class FeatureDetails(object):
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
        'feature': 'str',
        'endpoint': 'str',
        'documentation_url': 'str'
    }

    attribute_map = {
        'feature': 'feature',
        'endpoint': 'endpoint',
        'documentation_url': 'documentationUrl'
    }

    def __init__(self, feature=None, endpoint=None, documentation_url=None, local_vars_configuration=None):  # noqa: E501
        """FeatureDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._feature = None
        self._endpoint = None
        self._documentation_url = None
        self.discriminator = None

        if feature is not None:
            self.feature = feature
        if endpoint is not None:
            self.endpoint = endpoint
        if documentation_url is not None:
            self.documentation_url = documentation_url

    @property
    def feature(self):
        """Gets the feature of this FeatureDetails.  # noqa: E501


        :return: The feature of this FeatureDetails.  # noqa: E501
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this FeatureDetails.


        :param feature: The feature of this FeatureDetails.  # noqa: E501
        :type: str
        """
        allowed_values = ["INITIATE_PRE_AUTHORISATION", "INITIATE_ACCOUNT_REQUEST", "ACCOUNT_REQUEST_DETAILS", "ACCOUNTS", "ACCOUNT", "ACCOUNT_TRANSACTIONS", "ACCOUNT_STATEMENTS", "ACCOUNT_STATEMENT", "ACCOUNT_STATEMENT_FILE", "ACCOUNT_SCHEDULED_PAYMENTS", "ACCOUNT_DIRECT_DEBITS", "ACCOUNT_PERIODIC_PAYMENTS", "ACCOUNT_TRANSACTIONS_WITH_MERCHANT", "IDENTITY", "ACCOUNTS_WITHOUT_BALANCE", "ACCOUNT_WITHOUT_BALANCE", "ACCOUNT_BALANCES", "INITIATE_SINGLE_PAYMENT_SORTCODE", "EXISTING_PAYMENT_INITIATION_DETAILS", "CREATE_SINGLE_PAYMENT_SORTCODE", "EXISTING_PAYMENTS_DETAILS", "INITIATE_DOMESTIC_SINGLE_PAYMENT", "CREATE_DOMESTIC_SINGLE_PAYMENT", "INITIATE_DOMESTIC_SINGLE_INSTANT_PAYMENT", "CREATE_DOMESTIC_SINGLE_INSTANT_PAYMENT", "INITIATE_DOMESTIC_VARIABLE_RECURRING_PAYMENT", "CREATE_DOMESTIC_VARIABLE_RECURRING_PAYMENT", "INITIATE_DOMESTIC_SCHEDULED_PAYMENT", "CREATE_DOMESTIC_SCHEDULED_PAYMENT", "INITIATE_DOMESTIC_PERIODIC_PAYMENT", "CREATE_DOMESTIC_PERIODIC_PAYMENT", "PERIODIC_PAYMENT_FREQUENCY_EXTENDED", "INITIATE_INTERNATIONAL_VARIABLE_RECURRING_PAYMENT", "CREATE_INTERNATIONAL_VARIABLE_RECURRING_PAYMENT", "INITIATE_INTERNATIONAL_SCHEDULED_PAYMENT", "CREATE_INTERNATIONAL_SCHEDULED_PAYMENT", "INITIATE_INTERNATIONAL_PERIODIC_PAYMENT", "CREATE_INTERNATIONAL_PERIODIC_PAYMENT", "INITIATE_INTERNATIONAL_SINGLE_PAYMENT", "CREATE_INTERNATIONAL_SINGLE_PAYMENT", "INITIATE_BULK_PAYMENT", "CREATE_BULK_PAYMENT", "TRANSFER", "OPEN_DATA_PERSONAL_CURRENT_ACCOUNTS", "OPEN_DATA_ATMS", "READ_DOMESTIC_SINGLE_REFUND", "READ_DOMESTIC_SCHEDULED_REFUND", "READ_DOMESTIC_PERIODIC_PAYMENT_REFUND", "READ_INTERNATIONAL_SINGLE_REFUND", "READ_INTERNATIONAL_SCHEDULED_REFUND"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and feature not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `feature` ({0}), must be one of {1}"  # noqa: E501
                .format(feature, allowed_values)
            )

        self._feature = feature

    @property
    def endpoint(self):
        """Gets the endpoint of this FeatureDetails.  # noqa: E501


        :return: The endpoint of this FeatureDetails.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this FeatureDetails.


        :param endpoint: The endpoint of this FeatureDetails.  # noqa: E501
        :type: str
        """

        self._endpoint = endpoint

    @property
    def documentation_url(self):
        """Gets the documentation_url of this FeatureDetails.  # noqa: E501


        :return: The documentation_url of this FeatureDetails.  # noqa: E501
        :rtype: str
        """
        return self._documentation_url

    @documentation_url.setter
    def documentation_url(self, documentation_url):
        """Sets the documentation_url of this FeatureDetails.


        :param documentation_url: The documentation_url of this FeatureDetails.  # noqa: E501
        :type: str
        """

        self._documentation_url = documentation_url

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
        if not isinstance(other, FeatureDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FeatureDetails):
            return True

        return self.to_dict() != other.to_dict()
