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


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PutMyPasswordRequest(BaseModel):
    """
    パスワード変更リクエスト
    """ # noqa: E501
    password: Annotated[str, Field(strict=True)] = Field(description="現在のパスワード")
    new_password: Annotated[str, Field(strict=True)] = Field(description="新しいパスワード", alias="newPassword")
    __properties: ClassVar[List[str]] = ["password", "newPassword"]

    @field_validator('password')
    def password_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\x20-\x7E]{10,32}$", value):
            raise ValueError(r"must validate the regular expression /^[\x20-\x7E]{10,32}$/")
        return value

    @field_validator('new_password')
    def new_password_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\x20-\x7E]{10,32}$", value):
            raise ValueError(r"must validate the regular expression /^[\x20-\x7E]{10,32}$/")
        return value

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
        """Create an instance of PutMyPasswordRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PutMyPasswordRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "password": obj.get("password"),
            "newPassword": obj.get("newPassword")
        })
        return _obj


