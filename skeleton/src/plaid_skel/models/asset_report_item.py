# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.account_assets import AccountAssets




class AssetReportItem(BaseModel):
    """A representation of an Item within an Asset Report."""


    item_id: str = Field( description="The `item_id` of the Item associated with this webhook, warning, or error")
    institution_name: str = Field( description="The full financial institution name associated with the Item.")
    institution_id: str = Field( description="The id of the financial institution associated with the Item.")
    date_last_updated: datetime = Field( description="The date and time when this Item’s data was last retrieved from the financial institution, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format.")
    accounts: List[AccountAssets] = Field( description="Data about each of the accounts open on the Item.")

AssetReportItem.update_forward_refs()
