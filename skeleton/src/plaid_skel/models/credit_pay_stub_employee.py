# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.credit_pay_stub_address import CreditPayStubAddress
from plaid_skel.models.pay_stub_taxpayer_id import PayStubTaxpayerID




class CreditPayStubEmployee(BaseModel):
    """Data about the employee."""


    address: CreditPayStubAddress = Field()
    name: Optional[str] = Field(default=None, description="The name of the employee.")
    marital_status: Optional[str] = Field(default=None, description="Marital status of the employee - either `SINGLE` or `MARRIED`.")
    taxpayer_id: PayStubTaxpayerID = Field()

CreditPayStubEmployee.update_forward_refs()
