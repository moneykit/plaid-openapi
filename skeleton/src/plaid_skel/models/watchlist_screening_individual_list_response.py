# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.watchlist_screening_individual import WatchlistScreeningIndividual




class WatchlistScreeningIndividualListResponse(BaseModel):
    """Paginated list of individual watchlist screenings."""


    watchlist_screenings: List[WatchlistScreeningIndividual] = Field( description="List of individual watchlist screenings")
    next_cursor: Optional[str] = Field(default=None, description="An identifier that determines which page of results you receive.")
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

WatchlistScreeningIndividualListResponse.update_forward_refs()
