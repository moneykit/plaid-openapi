# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.credit_pay_stub_address import CreditPayStubAddress




class Credit1099Filer(BaseModel):
    """An object representing a filer used by 1099-K tax documents."""


    address: Optional[CreditPayStubAddress] = Field(default=None,)
    name: Optional[str] = Field(default=None, description="Name of filer.")
    tin: Optional[str] = Field(default=None, description="Tax identification number of filer.")
    type: Optional[str] = Field(default=None, description="One of the following values will be provided: Payment Settlement Entity (PSE), Electronic Payment Facilitator (EPF), Other Third Party")

Credit1099Filer.update_forward_refs()
