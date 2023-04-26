# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.credit_freddie_mac_assets_voa24 import CreditFreddieMacAssetsVOA24




class CreditFreddieMacVerificationOfAssetResponseVOA24(BaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""


    assets: CreditFreddieMacAssetsVOA24 = Field()

CreditFreddieMacVerificationOfAssetResponseVOA24.update_forward_refs()
