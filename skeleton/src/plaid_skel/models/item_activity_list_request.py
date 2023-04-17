# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class ItemActivityListRequest(BaseModel):
    """Request to list a historical log of user consent events."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#item_activity_list_request"
            }
        }

    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    access_token: Optional[str] = Field(default=None, description="The access token associated with the Item data is being requested for.")
    cursor: Optional[str] = Field(default=None, description="Cursor used for pagination.")
    count: Optional[int] = Field(default=None,)

    @validator("count")
    def count_max(cls, value):
        assert value <= 50
        return value

    @validator("count")
    def count_min(cls, value):
        assert value >= 1
        return value

ItemActivityListRequest.update_forward_refs()
