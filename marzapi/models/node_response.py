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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from marzapi.models.node_status import NodeStatus

class NodeResponse(BaseModel):
    """
    NodeResponse
    """
    name: StrictStr = Field(...)
    address: StrictStr = Field(...)
    port: Optional[StrictInt] = 62050
    api_port: Optional[StrictInt] = 62051
    usage_coefficient: Optional[Union[StrictFloat, StrictInt]] = 1.0
    id: StrictInt = Field(...)
    xray_version: Optional[StrictStr] = None
    status: NodeStatus = Field(...)
    message: Optional[StrictStr] = None
    __properties = ["name", "address", "port", "api_port", "usage_coefficient", "id", "xray_version", "status", "message"]

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
    def from_json(cls, json_str: str) -> 'NodeResponse':
        """Create an instance of NodeResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> 'NodeResponse':
        """Create an instance of NodeResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.parse_obj(obj)

        _obj = cls.parse_obj({
            "name": obj.get("name"),
            "address": obj.get("address"),
            "port": obj.get("port") if obj.get("port") is not None else 62050,
            "api_port": obj.get("api_port") if obj.get("api_port") is not None else 62051,
            "usage_coefficient": obj.get("usage_coefficient") if obj.get("usage_coefficient") is not None else 1.0,
            "id": obj.get("id"),
            "xray_version": obj.get("xray_version"),
            "status": obj.get("status"),
            "message": obj.get("message")
        })
        return _obj


