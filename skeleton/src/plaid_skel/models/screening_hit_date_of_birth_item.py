# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.date_range import DateRange
from plaid_skel.models.match_summary import MatchSummary




class ScreeningHitDateOfBirthItem(BaseModel):
    """Analyzed date of birth for the associated hit"""


    analysis: Optional[MatchSummary] = Field(default=None,)
    data: Optional[DateRange] = Field(default=None,)

ScreeningHitDateOfBirthItem.update_forward_refs()
