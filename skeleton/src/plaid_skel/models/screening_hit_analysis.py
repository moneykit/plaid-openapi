# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.match_summary_code import MatchSummaryCode




class ScreeningHitAnalysis(BaseModel):
    """Analysis information describing why a screening hit matched the provided user information"""


    dates_of_birth: Optional[MatchSummaryCode] = Field(default=None,)
    documents: Optional[MatchSummaryCode] = Field(default=None,)
    locations: Optional[MatchSummaryCode] = Field(default=None,)
    names: Optional[MatchSummaryCode] = Field(default=None,)
    search_terms_version: float = Field( description="The version of the screening's `search_terms` that were compared when the screening hit was added. screening hits are immutable once they have been reviewed. If changes are detected due to updates to the screening's `search_terms`, the associated program, or the list's source data prior to review, the screening hit will be updated to reflect those changes.")

ScreeningHitAnalysis.update_forward_refs()
