# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.asset_type import AssetType




class CreditFreddieMacAssetDetailVOE25(BaseModel):
    """Details about an asset."""


    asset_unique_identifier: str = Field( description="A vendor created unique Identifier.")
    asset_account_identifier: str = Field( description="A unique alphanumeric string identifying an asset.")
    asset_as_of_date: str = Field( description="Account Report As of Date / Create Date. Format YYYY-MM-DD")
    asset_description: Optional[str] = Field(default=None, description="A text description that further defines the Asset. This could be used to describe the shares associated with the stocks, bonds or mutual funds, retirement funds or business owned that the borrower has disclosed (named) as an asset.")
    asset_type: AssetType = Field()
    asset_type_additional_description: Optional[str] = Field(default=None, description="Additional Asset Decription some examples are Investment Tax-Deferred , Loan, 401K, 403B, Checking, Money Market, Credit Card,ROTH,529,Biller,ROLLOVER,CD,Savings,Investment Taxable, IRA, Mortgage, Line Of Credit.")
    asset_days_requested_count: int = Field( description="The Number of days requested made to the Financial Institution. Example When looking for 3 months of data from the FI, pass in 90 days.")
    asset_ownership_type: Optional[str] = Field(default=None, description="Ownership type of the asset account.")

CreditFreddieMacAssetDetailVOE25.update_forward_refs()
