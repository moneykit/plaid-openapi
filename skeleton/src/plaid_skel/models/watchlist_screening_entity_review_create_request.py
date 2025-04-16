# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401




class WatchlistScreeningEntityReviewCreateRequest(BaseModel):
    """Request input for creating a review for an entity screening"""


    confirmed_hits: List[str] = Field( description="Hits to mark as a true positive after thorough manual review. These hits will never recur or be updated once dismissed. In most cases, confirmed hits indicate that the customer should be rejected.")
    dismissed_hits: List[str] = Field( description="Hits to mark as a false positive after thorough manual review. These hits will never recur or be updated once dismissed.")
    comment: Optional[str] = Field(default=None, description="A comment submitted by a team member as part of reviewing a watchlist screening.")
    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    entity_watchlist_screening_id: str = Field( description="ID of the associated entity screening.")

    @field_validator("comment")
    @classmethod
    def comment_min_length(cls, value):
        assert len(value) >= 1
        return value

WatchlistScreeningEntityReviewCreateRequest.update_forward_refs()
