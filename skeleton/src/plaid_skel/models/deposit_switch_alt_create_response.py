# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class DepositSwitchAltCreateResponse(BaseModel):
    """DepositSwitchAltCreateResponse defines the response schema for `/deposit_switch/alt/create`"""


    deposit_switch_id: str = Field( description="ID of the deposit switch. This ID is persisted throughout the lifetime of the deposit switch.")
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

DepositSwitchAltCreateResponse.update_forward_refs()
