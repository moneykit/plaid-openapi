# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.credit_freddie_mac_verification_of_assets_deal_voa24 import CreditFreddieMacVerificationOfAssetsDealVOA24




class CreditFreddieMacVerificationOfAssetsVOA24(BaseModel):
    """Verification of Assets Report"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#credit_freddie_mac_verification_of_assets_voa24"
            }
        }

    deal: CreditFreddieMacVerificationOfAssetsDealVOA24 = Field()
    schema_version: float = Field( description="The Verification Of Assets (VOA) schema version.")

CreditFreddieMacVerificationOfAssetsVOA24.update_forward_refs()
