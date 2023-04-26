# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.entity_screening_hit_analysis import EntityScreeningHitAnalysis
from plaid_skel.models.entity_screening_hit_data import EntityScreeningHitData
from plaid_skel.models.entity_watchlist_code import EntityWatchlistCode
from plaid_skel.models.watchlist_screening_hit_status import WatchlistScreeningHitStatus




class EntityWatchlistScreeningHit(BaseModel):
    """Data from a government watchlist that has been attached to the screening."""


    id: str = Field( description="ID of the associated entity screening hit.")
    review_status: WatchlistScreeningHitStatus = Field()
    first_active: datetime = Field( description="An ISO8601 formatted timestamp.")
    inactive_since: Optional[datetime] = Field(default=None, description="An ISO8601 formatted timestamp.")
    historical_since: Optional[datetime] = Field(default=None, description="An ISO8601 formatted timestamp.")
    list_code: EntityWatchlistCode = Field()
    plaid_uid: str = Field( description="A universal identifier for a watchlist individual that is stable across searches and updates.")
    source_uid: Optional[str] = Field(default=None, description="The identifier provided by the source sanction or watchlist. When one is not provided by the source, this is `null`.")
    analysis: Optional[EntityScreeningHitAnalysis] = Field(default=None,)
    data: Optional[EntityScreeningHitData] = Field(default=None,)

    @validator("source_uid")
    def source_uid_min_length(cls, value):
        assert len(value) >= 1
        return value

EntityWatchlistScreeningHit.update_forward_refs()
