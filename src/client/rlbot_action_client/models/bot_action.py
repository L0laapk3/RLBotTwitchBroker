# coding: utf-8

"""
    Bot Action Server

    Allows custom Rocket League bots to accept tactical suggestions in the middle of a game.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: rlbotofficial@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class BotAction(object):
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
        'name': 'str',
        'strategic_category': 'StrategicCategory'
    }

    attribute_map = {
        'name': 'name',
        'strategic_category': 'strategicCategory'
    }

    def __init__(self, name=None, strategic_category=None):  # noqa: E501
        """BotAction - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._strategic_category = None
        self.discriminator = None
        self.name = name
        self.strategic_category = strategic_category

    @property
    def name(self):
        """Gets the name of this BotAction.  # noqa: E501


        :return: The name of this BotAction.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BotAction.


        :param name: The name of this BotAction.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def strategic_category(self):
        """Gets the strategic_category of this BotAction.  # noqa: E501


        :return: The strategic_category of this BotAction.  # noqa: E501
        :rtype: StrategicCategory
        """
        return self._strategic_category

    @strategic_category.setter
    def strategic_category(self, strategic_category):
        """Sets the strategic_category of this BotAction.


        :param strategic_category: The strategic_category of this BotAction.  # noqa: E501
        :type: StrategicCategory
        """
        if strategic_category is None:
            raise ValueError("Invalid value for `strategic_category`, must not be `None`")  # noqa: E501

        self._strategic_category = strategic_category

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
        if issubclass(BotAction, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BotAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other