# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401
from plaid_skel.models.watchlist_screening_audit_trail import WatchlistScreeningAuditTrail




class WatchlistScreeningEntityReviewCreateResponse(BaseModel):
    """A review submitted by a team member for an entity watchlist screening. A review can be either a comment on the current screening state, actions taken against hits attached to the watchlist screening, or both."""


    id: str = Field( description="ID of the associated entity review.")
    confirmed_hits: List[str] = Field( description="Hits marked as a true positive after thorough manual review. These hits will never recur or be updated once dismissed. In most cases, confirmed hits indicate that the customer should be rejected.")
    dismissed_hits: List[str] = Field( description="Hits marked as a false positive after thorough manual review. These hits will never recur or be updated once dismissed.")
    comment: Optional[str] = Field(default=None, description="A comment submitted by a team member as part of reviewing a watchlist screening.")
    audit_trail: WatchlistScreeningAuditTrail = Field()
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

    @field_validator("comment")
    @classmethod
    def comment_min_length(cls, value):
        assert len(value) >= 1
        return value

WatchlistScreeningEntityReviewCreateResponse.update_forward_refs()
