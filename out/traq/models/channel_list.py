# coding: utf-8

"""
    traQ v3

    traQ v3 API

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from pydantic import Field
from traq.models.channel import Channel
from traq.models.dm_channel import DMChannel
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ChannelList(BaseModel):
    """
    GET /channelsレスポンス
    """ # noqa: E501
    public: List[Channel] = Field(description="パブリックチャンネルの配列")
    dm: Optional[List[DMChannel]] = Field(default=None, description="ダイレクトメッセージチャンネルの配列")
    __properties: ClassVar[List[str]] = ["public", "dm"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ChannelList from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in public (list)
        _items = []
        if self.public:
            for _item in self.public:
                if _item:
                    _items.append(_item.to_dict())
            _dict['public'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in dm (list)
        _items = []
        if self.dm:
            for _item in self.dm:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dm'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ChannelList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "public": [Channel.from_dict(_item) for _item in obj.get("public")] if obj.get("public") is not None else None,
            "dm": [DMChannel.from_dict(_item) for _item in obj.get("dm")] if obj.get("dm") is not None else None
        })
        return _obj


