# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401
from plaid_skel.models.asset_report_refresh_request_options import AssetReportRefreshRequestOptions




class AssetReportRefreshRequest(BaseModel):
    """AssetReportRefreshRequest defines the request schema for `/asset_report/refresh`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    asset_report_token: str = Field( description="The `asset_report_token` returned by the original call to `/asset_report/create`")
    days_requested: Optional[int] = Field(default=None, description="The maximum number of days of history to include in the Asset Report. Must be an integer. If not specified, the value from the original call to `/asset_report/create` will be used.")
    options: Optional[AssetReportRefreshRequestOptions] = Field(default=None,)

    @field_validator("days_requested")
    @classmethod
    def days_requested_max(cls, value):
        assert value <= 731
        return value

    @field_validator("days_requested")
    @classmethod
    def days_requested_min(cls, value):
        assert value >= 0
        return value

AssetReportRefreshRequest.update_forward_refs()
