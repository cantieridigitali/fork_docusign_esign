# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RecipientProofFile(object):
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
        'is_in_proof_file': 'str'
    }

    attribute_map = {
        'is_in_proof_file': 'isInProofFile'
    }

    def __init__(self, is_in_proof_file=None):  # noqa: E501
        """RecipientProofFile - a model defined in Swagger"""  # noqa: E501

        self._is_in_proof_file = None
        self.discriminator = None

        if is_in_proof_file is not None:
            self.is_in_proof_file = is_in_proof_file

    @property
    def is_in_proof_file(self):
        """Gets the is_in_proof_file of this RecipientProofFile.  # noqa: E501

          # noqa: E501

        :return: The is_in_proof_file of this RecipientProofFile.  # noqa: E501
        :rtype: str
        """
        return self._is_in_proof_file

    @is_in_proof_file.setter
    def is_in_proof_file(self, is_in_proof_file):
        """Sets the is_in_proof_file of this RecipientProofFile.

          # noqa: E501

        :param is_in_proof_file: The is_in_proof_file of this RecipientProofFile.  # noqa: E501
        :type: str
        """

        self._is_in_proof_file = is_in_proof_file

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
        if issubclass(RecipientProofFile, dict):
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
        if not isinstance(other, RecipientProofFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other