# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.asset_detail import AssetDetail
from plaid_skel.models.asset_holder import AssetHolder
from plaid_skel.models.asset_owners import AssetOwners
from plaid_skel.models.credit_freddie_mac_asset_transactions_voa24 import CreditFreddieMacAssetTransactionsVOA24
from plaid_skel.models.validation_sources import ValidationSources




class CreditFreddieMacAssetVOA24(BaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""


    asset_detail: AssetDetail = Field()
    asset_owners: AssetOwners = Field()
    asset_holder: AssetHolder = Field()
    asset_transactions: CreditFreddieMacAssetTransactionsVOA24 = Field()
    validation_sources: ValidationSources = Field()

CreditFreddieMacAssetVOA24.update_forward_refs()
