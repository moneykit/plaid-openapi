# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class AssetReportFilterResponse(BaseModel):
    """AssetReportFilterResponse defines the response schema for `/asset_report/filter`"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#asset_report_filter_response"
            }
        }

    asset_report_token: str = Field( description="A token that can be provided to endpoints such as `/asset_report/get` or `/asset_report/pdf/get` to fetch or update an Asset Report.")
    asset_report_id: str = Field( description="A unique ID identifying an Asset Report. Like all Plaid identifiers, this ID is case sensitive.")
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

AssetReportFilterResponse.update_forward_refs()
