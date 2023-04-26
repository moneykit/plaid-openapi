# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.bank_transfer import BankTransfer




class BankTransferCreateResponse(BaseModel):
    """Defines the response schema for `/bank_transfer/create`"""


    bank_transfer: BankTransfer = Field()
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

BankTransferCreateResponse.update_forward_refs()
