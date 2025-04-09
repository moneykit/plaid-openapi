# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.asset_report_item import AssetReportItem
from plaid_skel.models.asset_report_user import AssetReportUser




class AssetReport(BaseModel):
    """An object representing an Asset Report"""


    asset_report_id: str = Field( description="A unique ID identifying an Asset Report. Like all Plaid identifiers, this ID is case sensitive.")
    client_report_id: Optional[str] = Field(default=None, description="An identifier you determine and submit for the Asset Report.")
    date_generated: datetime = Field( description="The date and time when the Asset Report was created, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (e.g. \"2018-04-12T03:32:11Z\").")
    days_requested: float = Field( description="The duration of transaction history you requested")
    user: AssetReportUser = Field()
    items: List[AssetReportItem] = Field( description="Data returned by Plaid about each of the Items included in the Asset Report.")

AssetReport.update_forward_refs()
