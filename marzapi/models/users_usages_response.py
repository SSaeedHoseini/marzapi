# coding: utf-8

"""
    MarzbanAPI

    Unified GUI Censorship Resistant Solution Powered by Xray

    The version of the OpenAPI document: 0.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, conlist
from marzapi.models.user_usage_response import UserUsageResponse

class UsersUsagesResponse(BaseModel):
    """
    UsersUsagesResponse
    """
    usages: conlist(UserUsageResponse) = Field(...)
    __properties = ["usages"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> UsersUsagesResponse:
        """Create an instance of UsersUsagesResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in usages (list)
        _items = []
        if self.usages:
            for _item in self.usages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['usages'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UsersUsagesResponse:
        """Create an instance of UsersUsagesResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UsersUsagesResponse.parse_obj(obj)

        _obj = UsersUsagesResponse.parse_obj({
            "usages": [UserUsageResponse.from_dict(_item) for _item in obj.get("usages")] if obj.get("usages") is not None else None
        })
        return _obj


