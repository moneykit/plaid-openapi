# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401




class AssetReportGetRequestOptions(BaseModel):
    """An optional object to filter or add data to `/asset_report/get` results. If provided, must be non-`null`."""


    days_to_include: Optional[int] = Field(default=None, description="The maximum number of days of history to include in the Asset Report.")

    @field_validator("days_to_include")
    @classmethod
    def days_to_include_max(cls, value):
        assert value <= 731
        return value

    @field_validator("days_to_include")
    @classmethod
    def days_to_include_min(cls, value):
        assert value >= 0
        return value

AssetReportGetRequestOptions.update_forward_refs()
