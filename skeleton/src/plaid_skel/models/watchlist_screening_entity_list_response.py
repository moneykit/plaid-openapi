# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.entity_watchlist_screening import EntityWatchlistScreening




class WatchlistScreeningEntityListResponse(BaseModel):
    """Paginated list of entity watchlist screenings"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#watchlist_screening_entity_list_response"
            }
        }

    entity_watchlist_screenings: List[EntityWatchlistScreening] = Field( description="List of entity watchlist screening")
    next_cursor: Optional[str] = Field(default=None, description="An identifier that determines which page of results you receive.")
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

WatchlistScreeningEntityListResponse.update_forward_refs()
