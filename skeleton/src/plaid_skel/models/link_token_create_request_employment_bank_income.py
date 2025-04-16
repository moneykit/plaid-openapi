# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class LinkTokenCreateRequestEmploymentBankIncome(BaseModel):
    """Specifies options for initializing Link for use with Bank Employment. This field is required if `employment` is included in the `products` array and `bank` is specified in `employment_source_types`."""


    days_requested: int = Field( description="The number of days of data to request for the Bank Employment product.")

LinkTokenCreateRequestEmploymentBankIncome.update_forward_refs()
