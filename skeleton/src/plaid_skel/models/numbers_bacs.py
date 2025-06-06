# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class NumbersBACS(BaseModel):
    """Identifying information for transferring money to or from a UK bank account via BACS."""


    account_id: str = Field( description="The Plaid account ID associated with the account numbers")
    account: str = Field( description="The BACS account number for the account")
    sort_code: str = Field( description="The BACS sort code for the account")

NumbersBACS.update_forward_refs()
