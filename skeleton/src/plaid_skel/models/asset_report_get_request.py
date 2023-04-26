# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.asset_report_get_request_options import AssetReportGetRequestOptions




class AssetReportGetRequest(BaseModel):
    """AssetReportGetRequest defines the request schema for `/asset_report/get`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    asset_report_token: str = Field( description="A token that can be provided to endpoints such as `/asset_report/get` or `/asset_report/pdf/get` to fetch or update an Asset Report.")
    include_insights: Optional[bool] = Field(default=None, description="`true` if you would like to retrieve the Asset Report with Insights, `false` otherwise. This field defaults to `false` if omitted.")
    fast_report: Optional[bool] = Field(default=None, description="`true` to fetch \"fast\" version of asset report. Defaults to false if omitted. Can only be used if `/asset_report/create` was called with `options.add_ons` set to `[\"fast_assets\"]`.")
    options: Optional[AssetReportGetRequestOptions] = Field(default=None,)

AssetReportGetRequest.update_forward_refs()
