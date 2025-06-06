# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.entity_watchlist_screening_review import EntityWatchlistScreeningReview




class WatchlistScreeningEntityReviewListResponse(BaseModel):
    """Paginated list of entity watchlist screening reviews"""


    entity_watchlist_screening_reviews: List[EntityWatchlistScreeningReview] = Field( description="List of entity watchlist screening reviews")
    next_cursor: Optional[str] = Field(default=None, description="An identifier that determines which page of results you receive.")
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

WatchlistScreeningEntityReviewListResponse.update_forward_refs()
