# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.address_data import AddressData




class Address(BaseModel):
    """A physical mailing address."""


    data: AddressData = Field()
    primary: Optional[bool] = Field(default=None, description="When `true`, identifies the address as the primary address on an account.")

Address.update_forward_refs()
