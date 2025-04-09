# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.earnings_breakdown import EarningsBreakdown
from plaid_skel.models.earnings_total import EarningsTotal




class Earnings(BaseModel):
    """An object representing both a breakdown of earnings on a paystub and the total earnings."""


    subtotals: Optional[List[EarningsTotal]] = Field(default=None,)
    totals: Optional[List[EarningsTotal]] = Field(default=None,)
    breakdown: Optional[List[EarningsBreakdown]] = Field(default=None,)
    total: Optional[EarningsTotal] = Field(default=None,)

Earnings.update_forward_refs()
