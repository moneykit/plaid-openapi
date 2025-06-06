# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class LinkTokenInvestments(BaseModel):
    """Configuration parameters for the Investments product"""


    allow_unverified_crypto_wallets: Optional[bool] = Field(default=None, description="If `true`, allow self-custody crypto wallets to be added without requiring signature verification. Defaults to `false`.")

LinkTokenInvestments.update_forward_refs()
