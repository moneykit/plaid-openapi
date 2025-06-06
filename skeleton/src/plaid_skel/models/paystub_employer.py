# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.paystub_address import PaystubAddress




class PaystubEmployer(BaseModel):
    """Information about the employer on the paystub"""


    address: Optional[PaystubAddress] = Field(default=None,)
    name: Optional[str] = Field(default=None, description="The name of the employer on the paystub.")

PaystubEmployer.update_forward_refs()
