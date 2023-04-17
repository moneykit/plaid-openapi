# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.asset_transaction_description import AssetTransactionDescription
from plaid_skel.models.credit_freddie_mac_asset_transaction_detail_voe25 import CreditFreddieMacAssetTransactionDetailVOE25




class CreditFreddieMacAssetTransactionVOE25(BaseModel):
    """An object representing..."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#credit_freddie_mac_asset_transaction_voe25"
            }
        }

    asset_transaction_detail: CreditFreddieMacAssetTransactionDetailVOE25 = Field()
    asset_transaction_description: List[AssetTransactionDescription] = Field( description="Documentation not found in the MISMO model viewer and not provided by Freddie Mac.")

CreditFreddieMacAssetTransactionVOE25.update_forward_refs()
