# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.206
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class CreditInterestTierBand(object):
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
        'aer': 'str',
        'application_frequency': 'str',
        'bank_interest_rate': 'str',
        'bank_interest_rate_type': 'str',
        'calculation_frequency': 'str',
        'deposit_interest_applied_coverage': 'str',
        'fixed_variable_interest_rate_type': 'str',
        'identification': 'str',
        'notes': 'list[str]',
        'other_application_frequency': 'OtherApplicationFrequency',
        'other_bank_interest_type': 'OtherBankInterestType',
        'other_calculation_frequency': 'OtherCalculationFrequency',
        'tier_value_maximum': 'str',
        'tier_value_minimum': 'str'
    }

    attribute_map = {
        'aer': 'AER',
        'application_frequency': 'ApplicationFrequency',
        'bank_interest_rate': 'BankInterestRate',
        'bank_interest_rate_type': 'BankInterestRateType',
        'calculation_frequency': 'CalculationFrequency',
        'deposit_interest_applied_coverage': 'DepositInterestAppliedCoverage',
        'fixed_variable_interest_rate_type': 'FixedVariableInterestRateType',
        'identification': 'Identification',
        'notes': 'Notes',
        'other_application_frequency': 'OtherApplicationFrequency',
        'other_bank_interest_type': 'OtherBankInterestType',
        'other_calculation_frequency': 'OtherCalculationFrequency',
        'tier_value_maximum': 'TierValueMaximum',
        'tier_value_minimum': 'TierValueMinimum'
    }

    def __init__(self, aer=None, application_frequency=None, bank_interest_rate=None, bank_interest_rate_type=None, calculation_frequency=None, deposit_interest_applied_coverage=None, fixed_variable_interest_rate_type=None, identification=None, notes=None, other_application_frequency=None, other_bank_interest_type=None, other_calculation_frequency=None, tier_value_maximum=None, tier_value_minimum=None, local_vars_configuration=None):  # noqa: E501
        """CreditInterestTierBand - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._aer = None
        self._application_frequency = None
        self._bank_interest_rate = None
        self._bank_interest_rate_type = None
        self._calculation_frequency = None
        self._deposit_interest_applied_coverage = None
        self._fixed_variable_interest_rate_type = None
        self._identification = None
        self._notes = None
        self._other_application_frequency = None
        self._other_bank_interest_type = None
        self._other_calculation_frequency = None
        self._tier_value_maximum = None
        self._tier_value_minimum = None
        self.discriminator = None

        if aer is not None:
            self.aer = aer
        if application_frequency is not None:
            self.application_frequency = application_frequency
        if bank_interest_rate is not None:
            self.bank_interest_rate = bank_interest_rate
        if bank_interest_rate_type is not None:
            self.bank_interest_rate_type = bank_interest_rate_type
        if calculation_frequency is not None:
            self.calculation_frequency = calculation_frequency
        if deposit_interest_applied_coverage is not None:
            self.deposit_interest_applied_coverage = deposit_interest_applied_coverage
        if fixed_variable_interest_rate_type is not None:
            self.fixed_variable_interest_rate_type = fixed_variable_interest_rate_type
        if identification is not None:
            self.identification = identification
        if notes is not None:
            self.notes = notes
        if other_application_frequency is not None:
            self.other_application_frequency = other_application_frequency
        if other_bank_interest_type is not None:
            self.other_bank_interest_type = other_bank_interest_type
        if other_calculation_frequency is not None:
            self.other_calculation_frequency = other_calculation_frequency
        if tier_value_maximum is not None:
            self.tier_value_maximum = tier_value_maximum
        if tier_value_minimum is not None:
            self.tier_value_minimum = tier_value_minimum

    @property
    def aer(self):
        """Gets the aer of this CreditInterestTierBand.  # noqa: E501


        :return: The aer of this CreditInterestTierBand.  # noqa: E501
        :rtype: str
        """
        return self._aer

    @aer.setter
    def aer(self, aer):
        """Sets the aer of this CreditInterestTierBand.


        :param aer: The aer of this CreditInterestTierBand.  # noqa: E501
        :type: str
        """

        self._aer = aer

    @property
    def application_frequency(self):
        """Gets the application_frequency of this CreditInterestTierBand.  # noqa: E501


        :return: The application_frequency of this CreditInterestTierBand.  # noqa: E501
        :rtype: str
        """
        return self._application_frequency

    @application_frequency.setter
    def application_frequency(self, application_frequency):
        """Sets the application_frequency of this CreditInterestTierBand.


        :param application_frequency: The application_frequency of this CreditInterestTierBand.  # noqa: E501
        :type: str
        """
        allowed_values = ["PerAcademicTerm", "Daily", "HalfYearly", "Monthly", "Other", "Quarterly", "PerStatementDate", "Weekly", "Yearly"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and application_frequency not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `application_frequency` ({0}), must be one of {1}"  # noqa: E501
                .format(application_frequency, allowed_values)
            )

        self._application_frequency = application_frequency

    @property
    def bank_interest_rate(self):
        """Gets the bank_interest_rate of this CreditInterestTierBand.  # noqa: E501


        :return: The bank_interest_rate of this CreditInterestTierBand.  # noqa: E501
        :rtype: str
        """
        return self._bank_interest_rate

    @bank_interest_rate.setter
    def bank_interest_rate(self, bank_interest_rate):
        """Sets the bank_interest_rate of this CreditInterestTierBand.


        :param bank_interest_rate: The bank_interest_rate of this CreditInterestTierBand.  # noqa: E501
        :type: str
        """

        self._bank_interest_rate = bank_interest_rate

    @property
    def bank_interest_rate_type(self):
        """Gets the bank_interest_rate_type of this CreditInterestTierBand.  # noqa: E501


        :return: The bank_interest_rate_type of this CreditInterestTierBand.  # noqa: E501
        :rtype: str
        """
        return self._bank_interest_rate_type

    @bank_interest_rate_type.setter
    def bank_interest_rate_type(self, bank_interest_rate_type):
        """Sets the bank_interest_rate_type of this CreditInterestTierBand.


        :param bank_interest_rate_type: The bank_interest_rate_type of this CreditInterestTierBand.  # noqa: E501
        :type: str
        """
        allowed_values = ["LinkedBaseRate", "Gross", "Net", "Other"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and bank_interest_rate_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `bank_interest_rate_type` ({0}), must be one of {1}"  # noqa: E501
                .format(bank_interest_rate_type, allowed_values)
            )

        self._bank_interest_rate_type = bank_interest_rate_type

    @property
    def calculation_frequency(self):
        """Gets the calculation_frequency of this CreditInterestTierBand.  # noqa: E501


        :return: The calculation_frequency of this CreditInterestTierBand.  # noqa: E501
        :rtype: str
        """
        return self._calculation_frequency

    @calculation_frequency.setter
    def calculation_frequency(self, calculation_frequency):
        """Sets the calculation_frequency of this CreditInterestTierBand.


        :param calculation_frequency: The calculation_frequency of this CreditInterestTierBand.  # noqa: E501
        :type: str
        """
        allowed_values = ["PerAcademicTerm", "Daily", "HalfYearly", "Monthly", "Other", "Quarterly", "PerStatementDate", "Weekly", "Yearly"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and calculation_frequency not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `calculation_frequency` ({0}), must be one of {1}"  # noqa: E501
                .format(calculation_frequency, allowed_values)
            )

        self._calculation_frequency = calculation_frequency

    @property
    def deposit_interest_applied_coverage(self):
        """Gets the deposit_interest_applied_coverage of this CreditInterestTierBand.  # noqa: E501


        :return: The deposit_interest_applied_coverage of this CreditInterestTierBand.  # noqa: E501
        :rtype: str
        """
        return self._deposit_interest_applied_coverage

    @deposit_interest_applied_coverage.setter
    def deposit_interest_applied_coverage(self, deposit_interest_applied_coverage):
        """Sets the deposit_interest_applied_coverage of this CreditInterestTierBand.


        :param deposit_interest_applied_coverage: The deposit_interest_applied_coverage of this CreditInterestTierBand.  # noqa: E501
        :type: str
        """
        allowed_values = ["Tiered", "Whole"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and deposit_interest_applied_coverage not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `deposit_interest_applied_coverage` ({0}), must be one of {1}"  # noqa: E501
                .format(deposit_interest_applied_coverage, allowed_values)
            )

        self._deposit_interest_applied_coverage = deposit_interest_applied_coverage

    @property
    def fixed_variable_interest_rate_type(self):
        """Gets the fixed_variable_interest_rate_type of this CreditInterestTierBand.  # noqa: E501


        :return: The fixed_variable_interest_rate_type of this CreditInterestTierBand.  # noqa: E501
        :rtype: str
        """
        return self._fixed_variable_interest_rate_type

    @fixed_variable_interest_rate_type.setter
    def fixed_variable_interest_rate_type(self, fixed_variable_interest_rate_type):
        """Sets the fixed_variable_interest_rate_type of this CreditInterestTierBand.


        :param fixed_variable_interest_rate_type: The fixed_variable_interest_rate_type of this CreditInterestTierBand.  # noqa: E501
        :type: str
        """
        allowed_values = ["Fixed", "Variable"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and fixed_variable_interest_rate_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `fixed_variable_interest_rate_type` ({0}), must be one of {1}"  # noqa: E501
                .format(fixed_variable_interest_rate_type, allowed_values)
            )

        self._fixed_variable_interest_rate_type = fixed_variable_interest_rate_type

    @property
    def identification(self):
        """Gets the identification of this CreditInterestTierBand.  # noqa: E501


        :return: The identification of this CreditInterestTierBand.  # noqa: E501
        :rtype: str
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """Sets the identification of this CreditInterestTierBand.


        :param identification: The identification of this CreditInterestTierBand.  # noqa: E501
        :type: str
        """

        self._identification = identification

    @property
    def notes(self):
        """Gets the notes of this CreditInterestTierBand.  # noqa: E501


        :return: The notes of this CreditInterestTierBand.  # noqa: E501
        :rtype: list[str]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this CreditInterestTierBand.


        :param notes: The notes of this CreditInterestTierBand.  # noqa: E501
        :type: list[str]
        """

        self._notes = notes

    @property
    def other_application_frequency(self):
        """Gets the other_application_frequency of this CreditInterestTierBand.  # noqa: E501


        :return: The other_application_frequency of this CreditInterestTierBand.  # noqa: E501
        :rtype: OtherApplicationFrequency
        """
        return self._other_application_frequency

    @other_application_frequency.setter
    def other_application_frequency(self, other_application_frequency):
        """Sets the other_application_frequency of this CreditInterestTierBand.


        :param other_application_frequency: The other_application_frequency of this CreditInterestTierBand.  # noqa: E501
        :type: OtherApplicationFrequency
        """

        self._other_application_frequency = other_application_frequency

    @property
    def other_bank_interest_type(self):
        """Gets the other_bank_interest_type of this CreditInterestTierBand.  # noqa: E501


        :return: The other_bank_interest_type of this CreditInterestTierBand.  # noqa: E501
        :rtype: OtherBankInterestType
        """
        return self._other_bank_interest_type

    @other_bank_interest_type.setter
    def other_bank_interest_type(self, other_bank_interest_type):
        """Sets the other_bank_interest_type of this CreditInterestTierBand.


        :param other_bank_interest_type: The other_bank_interest_type of this CreditInterestTierBand.  # noqa: E501
        :type: OtherBankInterestType
        """

        self._other_bank_interest_type = other_bank_interest_type

    @property
    def other_calculation_frequency(self):
        """Gets the other_calculation_frequency of this CreditInterestTierBand.  # noqa: E501


        :return: The other_calculation_frequency of this CreditInterestTierBand.  # noqa: E501
        :rtype: OtherCalculationFrequency
        """
        return self._other_calculation_frequency

    @other_calculation_frequency.setter
    def other_calculation_frequency(self, other_calculation_frequency):
        """Sets the other_calculation_frequency of this CreditInterestTierBand.


        :param other_calculation_frequency: The other_calculation_frequency of this CreditInterestTierBand.  # noqa: E501
        :type: OtherCalculationFrequency
        """

        self._other_calculation_frequency = other_calculation_frequency

    @property
    def tier_value_maximum(self):
        """Gets the tier_value_maximum of this CreditInterestTierBand.  # noqa: E501


        :return: The tier_value_maximum of this CreditInterestTierBand.  # noqa: E501
        :rtype: str
        """
        return self._tier_value_maximum

    @tier_value_maximum.setter
    def tier_value_maximum(self, tier_value_maximum):
        """Sets the tier_value_maximum of this CreditInterestTierBand.


        :param tier_value_maximum: The tier_value_maximum of this CreditInterestTierBand.  # noqa: E501
        :type: str
        """

        self._tier_value_maximum = tier_value_maximum

    @property
    def tier_value_minimum(self):
        """Gets the tier_value_minimum of this CreditInterestTierBand.  # noqa: E501


        :return: The tier_value_minimum of this CreditInterestTierBand.  # noqa: E501
        :rtype: str
        """
        return self._tier_value_minimum

    @tier_value_minimum.setter
    def tier_value_minimum(self, tier_value_minimum):
        """Sets the tier_value_minimum of this CreditInterestTierBand.


        :param tier_value_minimum: The tier_value_minimum of this CreditInterestTierBand.  # noqa: E501
        :type: str
        """

        self._tier_value_minimum = tier_value_minimum

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
        if not isinstance(other, CreditInterestTierBand):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreditInterestTierBand):
            return True

        return self.to_dict() != other.to_dict()
