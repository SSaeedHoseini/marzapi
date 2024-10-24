# coding: utf-8

"""
    MarzbanAPI

    Unified GUI Censorship Resistant Solution Powered by Xray

    The version of the OpenAPI document: 0.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ProxyTypes(str, Enum):
    """
    An enumeration.
    """

    """
    allowed enum values
    """
    VMESS = 'vmess'
    VLESS = 'vless'
    TROJAN = 'trojan'
    SHADOWSOCKS = 'shadowsocks'

    @classmethod
    def from_json(cls, json_str: str) -> 'ProxyTypes':
        """Create an instance of ProxyTypes from a JSON string"""
        return cls(json.loads(json_str))


