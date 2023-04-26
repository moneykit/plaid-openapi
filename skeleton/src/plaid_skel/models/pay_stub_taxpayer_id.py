# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class PayStubTaxpayerID(BaseModel):
    """Taxpayer ID of the individual receiving the paystub."""


    id_type: Optional[str] = Field(default=None, description="Type of ID, e.g. 'SSN'.")
    id_mask: Optional[str] = Field(default=None, description="ID mask; i.e. last 4 digits of the taxpayer ID.")

PayStubTaxpayerID.update_forward_refs()
