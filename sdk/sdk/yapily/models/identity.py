# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from yapily.models.identity_address import IdentityAddress  # noqa: F401,E501


class Identity(object):
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
        'addresses': 'list[IdentityAddress]',
        'birthdate': 'str',
        'email': 'str',
        'first_name': 'str',
        'gender': 'str',
        'id': 'str',
        'last_name': 'str',
        'phone': 'str'
    }

    attribute_map = {
        'addresses': 'addresses',
        'birthdate': 'birthdate',
        'email': 'email',
        'first_name': 'firstName',
        'gender': 'gender',
        'id': 'id',
        'last_name': 'lastName',
        'phone': 'phone'
    }

    def __init__(self, addresses=None, birthdate=None, email=None, first_name=None, gender=None, id=None, last_name=None, phone=None):  # noqa: E501
        """Identity - a model defined in Swagger"""  # noqa: E501

        self._addresses = None
        self._birthdate = None
        self._email = None
        self._first_name = None
        self._gender = None
        self._id = None
        self._last_name = None
        self._phone = None
        self.discriminator = None

        if addresses is not None:
            self.addresses = addresses
        if birthdate is not None:
            self.birthdate = birthdate
        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if gender is not None:
            self.gender = gender
        if id is not None:
            self.id = id
        if last_name is not None:
            self.last_name = last_name
        if phone is not None:
            self.phone = phone

    @property
    def addresses(self):
        """Gets the addresses of this Identity.  # noqa: E501


        :return: The addresses of this Identity.  # noqa: E501
        :rtype: list[IdentityAddress]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this Identity.


        :param addresses: The addresses of this Identity.  # noqa: E501
        :type: list[IdentityAddress]
        """

        self._addresses = addresses

    @property
    def birthdate(self):
        """Gets the birthdate of this Identity.  # noqa: E501


        :return: The birthdate of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._birthdate

    @birthdate.setter
    def birthdate(self, birthdate):
        """Sets the birthdate of this Identity.


        :param birthdate: The birthdate of this Identity.  # noqa: E501
        :type: str
        """

        self._birthdate = birthdate

    @property
    def email(self):
        """Gets the email of this Identity.  # noqa: E501


        :return: The email of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Identity.


        :param email: The email of this Identity.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this Identity.  # noqa: E501


        :return: The first_name of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Identity.


        :param first_name: The first_name of this Identity.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def gender(self):
        """Gets the gender of this Identity.  # noqa: E501


        :return: The gender of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this Identity.


        :param gender: The gender of this Identity.  # noqa: E501
        :type: str
        """

        self._gender = gender

    @property
    def id(self):
        """Gets the id of this Identity.  # noqa: E501


        :return: The id of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Identity.


        :param id: The id of this Identity.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_name(self):
        """Gets the last_name of this Identity.  # noqa: E501


        :return: The last_name of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Identity.


        :param last_name: The last_name of this Identity.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def phone(self):
        """Gets the phone of this Identity.  # noqa: E501


        :return: The phone of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Identity.


        :param phone: The phone of this Identity.  # noqa: E501
        :type: str
        """

        self._phone = phone

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
        if not isinstance(other, Identity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
