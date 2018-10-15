# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.37
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from yapily.models.core_product import CoreProduct  # noqa: F401,E501
from yapily.models.credit_interest import CreditInterest  # noqa: F401,E501
from yapily.models.eligibility import Eligibility  # noqa: F401,E501
from yapily.models.overdraft import Overdraft  # noqa: F401,E501


class PersonalCurrentAccountPCAMarketingState(object):
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
        'core_product': 'CoreProduct',
        'credit_interest': 'CreditInterest',
        'eligibility': 'Eligibility',
        'first_marketed_date': 'datetime',
        'identification': 'str',
        'last_marketed_date': 'datetime',
        'marketing_state': 'str',
        'notes': 'list[str]',
        'overdraft': 'Overdraft',
        'predecessor_id': 'str',
        'state_tenure_length': 'float',
        'state_tenure_period': 'str'
    }

    attribute_map = {
        'core_product': 'CoreProduct',
        'credit_interest': 'CreditInterest',
        'eligibility': 'Eligibility',
        'first_marketed_date': 'FirstMarketedDate',
        'identification': 'Identification',
        'last_marketed_date': 'LastMarketedDate',
        'marketing_state': 'MarketingState',
        'notes': 'Notes',
        'overdraft': 'Overdraft',
        'predecessor_id': 'PredecessorID',
        'state_tenure_length': 'StateTenureLength',
        'state_tenure_period': 'StateTenurePeriod'
    }

    def __init__(self, core_product=None, credit_interest=None, eligibility=None, first_marketed_date=None, identification=None, last_marketed_date=None, marketing_state=None, notes=None, overdraft=None, predecessor_id=None, state_tenure_length=None, state_tenure_period=None):  # noqa: E501
        """PersonalCurrentAccountPCAMarketingState - a model defined in Swagger"""  # noqa: E501

        self._core_product = None
        self._credit_interest = None
        self._eligibility = None
        self._first_marketed_date = None
        self._identification = None
        self._last_marketed_date = None
        self._marketing_state = None
        self._notes = None
        self._overdraft = None
        self._predecessor_id = None
        self._state_tenure_length = None
        self._state_tenure_period = None
        self.discriminator = None

        if core_product is not None:
            self.core_product = core_product
        if credit_interest is not None:
            self.credit_interest = credit_interest
        if eligibility is not None:
            self.eligibility = eligibility
        if first_marketed_date is not None:
            self.first_marketed_date = first_marketed_date
        if identification is not None:
            self.identification = identification
        if last_marketed_date is not None:
            self.last_marketed_date = last_marketed_date
        if marketing_state is not None:
            self.marketing_state = marketing_state
        if notes is not None:
            self.notes = notes
        if overdraft is not None:
            self.overdraft = overdraft
        if predecessor_id is not None:
            self.predecessor_id = predecessor_id
        if state_tenure_length is not None:
            self.state_tenure_length = state_tenure_length
        if state_tenure_period is not None:
            self.state_tenure_period = state_tenure_period

    @property
    def core_product(self):
        """Gets the core_product of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501


        :return: The core_product of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501
        :rtype: CoreProduct
        """
        return self._core_product

    @core_product.setter
    def core_product(self, core_product):
        """Sets the core_product of this PersonalCurrentAccountPCAMarketingState.


        :param core_product: The core_product of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501
        :type: CoreProduct
        """

        self._core_product = core_product

    @property
    def credit_interest(self):
        """Gets the credit_interest of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501


        :return: The credit_interest of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501
        :rtype: CreditInterest
        """
        return self._credit_interest

    @credit_interest.setter
    def credit_interest(self, credit_interest):
        """Sets the credit_interest of this PersonalCurrentAccountPCAMarketingState.


        :param credit_interest: The credit_interest of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501
        :type: CreditInterest
        """

        self._credit_interest = credit_interest

    @property
    def eligibility(self):
        """Gets the eligibility of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501


        :return: The eligibility of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501
        :rtype: Eligibility
        """
        return self._eligibility

    @eligibility.setter
    def eligibility(self, eligibility):
        """Sets the eligibility of this PersonalCurrentAccountPCAMarketingState.


        :param eligibility: The eligibility of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501
        :type: Eligibility
        """

        self._eligibility = eligibility

    @property
    def first_marketed_date(self):
        """Gets the first_marketed_date of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501


        :return: The first_marketed_date of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501
        :rtype: datetime
        """
        return self._first_marketed_date

    @first_marketed_date.setter
    def first_marketed_date(self, first_marketed_date):
        """Sets the first_marketed_date of this PersonalCurrentAccountPCAMarketingState.


        :param first_marketed_date: The first_marketed_date of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501
        :type: datetime
        """

        self._first_marketed_date = first_marketed_date

    @property
    def identification(self):
        """Gets the identification of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501


        :return: The identification of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501
        :rtype: str
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """Sets the identification of this PersonalCurrentAccountPCAMarketingState.


        :param identification: The identification of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501
        :type: str
        """

        self._identification = identification

    @property
    def last_marketed_date(self):
        """Gets the last_marketed_date of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501


        :return: The last_marketed_date of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501
        :rtype: datetime
        """
        return self._last_marketed_date

    @last_marketed_date.setter
    def last_marketed_date(self, last_marketed_date):
        """Sets the last_marketed_date of this PersonalCurrentAccountPCAMarketingState.


        :param last_marketed_date: The last_marketed_date of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501
        :type: datetime
        """

        self._last_marketed_date = last_marketed_date

    @property
    def marketing_state(self):
        """Gets the marketing_state of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501


        :return: The marketing_state of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501
        :rtype: str
        """
        return self._marketing_state

    @marketing_state.setter
    def marketing_state(self, marketing_state):
        """Sets the marketing_state of this PersonalCurrentAccountPCAMarketingState.


        :param marketing_state: The marketing_state of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501
        :type: str
        """

        self._marketing_state = marketing_state

    @property
    def notes(self):
        """Gets the notes of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501


        :return: The notes of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501
        :rtype: list[str]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this PersonalCurrentAccountPCAMarketingState.


        :param notes: The notes of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501
        :type: list[str]
        """

        self._notes = notes

    @property
    def overdraft(self):
        """Gets the overdraft of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501


        :return: The overdraft of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501
        :rtype: Overdraft
        """
        return self._overdraft

    @overdraft.setter
    def overdraft(self, overdraft):
        """Sets the overdraft of this PersonalCurrentAccountPCAMarketingState.


        :param overdraft: The overdraft of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501
        :type: Overdraft
        """

        self._overdraft = overdraft

    @property
    def predecessor_id(self):
        """Gets the predecessor_id of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501


        :return: The predecessor_id of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501
        :rtype: str
        """
        return self._predecessor_id

    @predecessor_id.setter
    def predecessor_id(self, predecessor_id):
        """Sets the predecessor_id of this PersonalCurrentAccountPCAMarketingState.


        :param predecessor_id: The predecessor_id of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501
        :type: str
        """

        self._predecessor_id = predecessor_id

    @property
    def state_tenure_length(self):
        """Gets the state_tenure_length of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501


        :return: The state_tenure_length of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501
        :rtype: float
        """
        return self._state_tenure_length

    @state_tenure_length.setter
    def state_tenure_length(self, state_tenure_length):
        """Sets the state_tenure_length of this PersonalCurrentAccountPCAMarketingState.


        :param state_tenure_length: The state_tenure_length of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501
        :type: float
        """

        self._state_tenure_length = state_tenure_length

    @property
    def state_tenure_period(self):
        """Gets the state_tenure_period of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501


        :return: The state_tenure_period of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501
        :rtype: str
        """
        return self._state_tenure_period

    @state_tenure_period.setter
    def state_tenure_period(self, state_tenure_period):
        """Sets the state_tenure_period of this PersonalCurrentAccountPCAMarketingState.


        :param state_tenure_period: The state_tenure_period of this PersonalCurrentAccountPCAMarketingState.  # noqa: E501
        :type: str
        """

        self._state_tenure_period = state_tenure_period

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
        if not isinstance(other, PersonalCurrentAccountPCAMarketingState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
