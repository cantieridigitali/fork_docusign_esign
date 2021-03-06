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

from docusign_esign.client.configuration import Configuration


class BulkRecipientsRequest(object):
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
        'bulk_recipients': 'list[BulkRecipient]'
    }

    attribute_map = {
        'bulk_recipients': 'bulkRecipients'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """BulkRecipientsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bulk_recipients = None
        self.discriminator = None

        setattr(self, "_{}".format('bulk_recipients'), kwargs.get('bulk_recipients', None))

    @property
    def bulk_recipients(self):
        """Gets the bulk_recipients of this BulkRecipientsRequest.  # noqa: E501

        A complex type containing information about the bulk recipients in the request.  # noqa: E501

        :return: The bulk_recipients of this BulkRecipientsRequest.  # noqa: E501
        :rtype: list[BulkRecipient]
        """
        return self._bulk_recipients

    @bulk_recipients.setter
    def bulk_recipients(self, bulk_recipients):
        """Sets the bulk_recipients of this BulkRecipientsRequest.

        A complex type containing information about the bulk recipients in the request.  # noqa: E501

        :param bulk_recipients: The bulk_recipients of this BulkRecipientsRequest.  # noqa: E501
        :type: list[BulkRecipient]
        """

        self._bulk_recipients = bulk_recipients

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
        if issubclass(BulkRecipientsRequest, dict):
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
        if not isinstance(other, BulkRecipientsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BulkRecipientsRequest):
            return True

        return self.to_dict() != other.to_dict()
