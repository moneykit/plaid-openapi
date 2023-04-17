# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.account_identity import AccountIdentity
from plaid_skel.models.item import Item




class IdentityGetResponse(BaseModel):
    """IdentityGetResponse defines the response schema for `/identity/get`"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#identity_get_response"
            }
        }

    accounts: List[AccountIdentity] = Field( description="The accounts for which Identity data has been requested")
    item: Item = Field()
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

IdentityGetResponse.update_forward_refs()
