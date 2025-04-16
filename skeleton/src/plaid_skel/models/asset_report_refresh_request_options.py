# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.asset_report_user import AssetReportUser




class AssetReportRefreshRequestOptions(BaseModel):
    """An optional object to filter `/asset_report/refresh` results. If provided, cannot be `null`. If not specified, the `options` from the original call to `/asset_report/create` will be used."""


    client_report_id: Optional[str] = Field(default=None, description="Client-generated identifier, which can be used by lenders to track loan applications.")
    webhook: Optional[str] = Field(default=None, description="URL to which Plaid will send Assets webhooks, for example when the requested Asset Report is ready.")
    user: Optional[AssetReportUser] = Field(default=None,)

AssetReportRefreshRequestOptions.update_forward_refs()
