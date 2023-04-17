# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.watchlist_screening_status import WatchlistScreeningStatus




class WatchlistScreeningIndividualListRequest(BaseModel):
    """Request input for listinging watchlist screenings for individuals"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#watchlist_screening_individual_list_request"
            }
        }

    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    watchlist_program_id: str = Field( description="ID of the associated program.")
    client_user_id: Optional[str] = Field(default=None, description="An identifier to help you connect this object to your internal systems. For example, your database ID corresponding to this object.")
    status: Optional[WatchlistScreeningStatus] = Field(default=None,)
    assignee: Optional[str] = Field(default=None, description="ID of the associated user.")
    cursor: Optional[str] = Field(default=None, description="An identifier that determines which page of results you receive.")

    @validator("client_user_id")
    def client_user_id_min_length(cls, value):
        assert len(value) >= 1
        return value

WatchlistScreeningIndividualListRequest.update_forward_refs()
