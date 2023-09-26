# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class WalletTransactionListRequestOptions(BaseModel):
    """Additional wallet transaction options"""


    start_time: Optional[datetime] = Field(default=None, description="Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DDThh:mm:ssZ) for filtering transactions, inclusive of the provided date.")
    end_time: Optional[datetime] = Field(default=None, description="Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DDThh:mm:ssZ) for filtering transactions, inclusive of the provided date.")

WalletTransactionListRequestOptions.update_forward_refs()
