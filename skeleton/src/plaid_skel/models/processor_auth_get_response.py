# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.account_base import AccountBase
from plaid_skel.models.processor_number import ProcessorNumber




class ProcessorAuthGetResponse(BaseModel):
    """ProcessorAuthGetResponse defines the response schema for `/processor/auth/get`"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#processor_auth_get_response"
            }
        }

    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")
    numbers: ProcessorNumber = Field()
    account: AccountBase = Field()

ProcessorAuthGetResponse.update_forward_refs()
