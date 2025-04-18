# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.transfer_user_address_in_response import TransferUserAddressInResponse




class TransferUserInResponse(BaseModel):
    """The legal name and other information for the account holder."""


    legal_name: str = Field( description="The user's legal name.")
    phone_number: Optional[str] = Field(default=None, description="The user's phone number.")
    email_address: Optional[str] = Field(default=None, description="The user's email address.")
    address: Optional[TransferUserAddressInResponse] = Field(default=None,)

TransferUserInResponse.update_forward_refs()
