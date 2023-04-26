# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.id_number_type import IDNumberType




class UserIDNumber(BaseModel):
    """ID number submitted by the user, currently used only for the Identity Verification product. If the user has not submitted this data yet, this field will be `null`. Otherwise, both fields are guaranteed to be filled."""

    class Config:
        schema_extra = {"nullable": True}

    value: str = Field( description="Value of identity document value typed in by user. Alpha-numeric, with all formatting characters stripped.")
    type: IDNumberType = Field()

UserIDNumber.update_forward_refs()
