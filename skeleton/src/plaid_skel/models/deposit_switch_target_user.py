# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.deposit_switch_address_data import DepositSwitchAddressData




class DepositSwitchTargetUser(BaseModel):
    """The deposit switch target user"""


    given_name: str = Field( description="The given name (first name) of the user.")
    family_name: str = Field( description="The family name (last name) of the user.")
    phone: str = Field( description="The phone number of the user. The endpoint can accept a variety of phone number formats, including E.164.")
    email: str = Field( description="The email address of the user.")
    address: Optional[DepositSwitchAddressData] = Field(default=None,)
    tax_payer_id: Optional[str] = Field(default=None, description="The taxpayer ID of the user, generally their SSN, EIN, or TIN.")

DepositSwitchTargetUser.update_forward_refs()
