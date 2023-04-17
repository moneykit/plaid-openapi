# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.link_token_get_metadata_response import LinkTokenGetMetadataResponse




class LinkTokenGetResponse(BaseModel):
    """LinkTokenGetResponse defines the response schema for `/link/token/get`"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#link_token_get_response"
            }
        }

    link_token: str = Field( description="A `link_token`, which can be supplied to Link in order to initialize it and receive a `public_token`, which can be exchanged for an `access_token`.")
    created_at: Optional[datetime] = Field(default=None, description="The creation timestamp for the `link_token`, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format.")
    expiration: Optional[datetime] = Field(default=None, description="The expiration timestamp for the `link_token`, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format.")
    metadata: LinkTokenGetMetadataResponse = Field()
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

LinkTokenGetResponse.update_forward_refs()
