# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from pprint import pformat
from six import iteritems
import re


class V1Settlement(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, status=None, total_money=None, initiated_at=None, bank_account_id=None, entries=None):
        """
        V1Settlement - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'status': 'str',
            'total_money': 'V1Money',
            'initiated_at': 'str',
            'bank_account_id': 'str',
            'entries': 'list[V1SettlementEntry]'
        }

        self.attribute_map = {
            'id': 'id',
            'status': 'status',
            'total_money': 'total_money',
            'initiated_at': 'initiated_at',
            'bank_account_id': 'bank_account_id',
            'entries': 'entries'
        }

        self._id = id
        self._status = status
        self._total_money = total_money
        self._initiated_at = initiated_at
        self._bank_account_id = bank_account_id
        self._entries = entries

    @property
    def id(self):
        """
        Gets the id of this V1Settlement.
        The settlement's unique identifier.

        :return: The id of this V1Settlement.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this V1Settlement.
        The settlement's unique identifier.

        :param id: The id of this V1Settlement.
        :type: str
        """

        self._id = id

    @property
    def status(self):
        """
        Gets the status of this V1Settlement.
        The settlement's current status.

        :return: The status of this V1Settlement.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this V1Settlement.
        The settlement's current status.

        :param status: The status of this V1Settlement.
        :type: str
        """

        self._status = status

    @property
    def total_money(self):
        """
        Gets the total_money of this V1Settlement.
        The amount of money involved in the settlement. A positive amount indicates a deposit, and a negative amount indicates a withdrawal. This amount is never zero.

        :return: The total_money of this V1Settlement.
        :rtype: V1Money
        """
        return self._total_money

    @total_money.setter
    def total_money(self, total_money):
        """
        Sets the total_money of this V1Settlement.
        The amount of money involved in the settlement. A positive amount indicates a deposit, and a negative amount indicates a withdrawal. This amount is never zero.

        :param total_money: The total_money of this V1Settlement.
        :type: V1Money
        """

        self._total_money = total_money

    @property
    def initiated_at(self):
        """
        Gets the initiated_at of this V1Settlement.
        The time when the settlement was submitted for deposit or withdrawal, in ISO 8601 format.

        :return: The initiated_at of this V1Settlement.
        :rtype: str
        """
        return self._initiated_at

    @initiated_at.setter
    def initiated_at(self, initiated_at):
        """
        Sets the initiated_at of this V1Settlement.
        The time when the settlement was submitted for deposit or withdrawal, in ISO 8601 format.

        :param initiated_at: The initiated_at of this V1Settlement.
        :type: str
        """

        self._initiated_at = initiated_at

    @property
    def bank_account_id(self):
        """
        Gets the bank_account_id of this V1Settlement.
        The Square-issued unique identifier for the bank account associated with the settlement.

        :return: The bank_account_id of this V1Settlement.
        :rtype: str
        """
        return self._bank_account_id

    @bank_account_id.setter
    def bank_account_id(self, bank_account_id):
        """
        Sets the bank_account_id of this V1Settlement.
        The Square-issued unique identifier for the bank account associated with the settlement.

        :param bank_account_id: The bank_account_id of this V1Settlement.
        :type: str
        """

        self._bank_account_id = bank_account_id

    @property
    def entries(self):
        """
        Gets the entries of this V1Settlement.
        The entries included in this settlement.

        :return: The entries of this V1Settlement.
        :rtype: list[V1SettlementEntry]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """
        Sets the entries of this V1Settlement.
        The entries included in this settlement.

        :param entries: The entries of this V1Settlement.
        :type: list[V1SettlementEntry]
        """

        self._entries = entries

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other