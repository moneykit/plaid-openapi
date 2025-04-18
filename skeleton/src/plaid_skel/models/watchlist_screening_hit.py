# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401
from plaid_skel.models.individual_watchlist_code import IndividualWatchlistCode
from plaid_skel.models.screening_hit_analysis import ScreeningHitAnalysis
from plaid_skel.models.screening_hit_data import ScreeningHitData
from plaid_skel.models.watchlist_screening_hit_status import WatchlistScreeningHitStatus




class WatchlistScreeningHit(BaseModel):
    """Data from a government watchlist or PEP list that has been attached to the screening."""


    id: str = Field( description="ID of the associated screening hit.")
    review_status: WatchlistScreeningHitStatus = Field()
    first_active: datetime_ = Field( description="An ISO8601 formatted timestamp.")
    inactive_since: Optional[datetime_] = Field(default=None, description="An ISO8601 formatted timestamp.")
    historical_since: Optional[datetime_] = Field(default=None, description="An ISO8601 formatted timestamp.")
    list_code: IndividualWatchlistCode = Field()
    plaid_uid: str = Field( description="A universal identifier for a watchlist individual that is stable across searches and updates.")
    source_uid: Optional[str] = Field(default=None, description="The identifier provided by the source sanction or watchlist. When one is not provided by the source, this is `null`.")
    analysis: Optional[ScreeningHitAnalysis] = Field(default=None,)
    data: Optional[ScreeningHitData] = Field(default=None,)

    @field_validator("source_uid")
    @classmethod
    def source_uid_min_length(cls, value):
        assert len(value) >= 1
        return value

WatchlistScreeningHit.update_forward_refs()
