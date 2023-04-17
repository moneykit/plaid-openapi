# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.bank_transfer import BankTransfer




class ProcessorBankTransferCreateResponse(BaseModel):
    """Defines the response schema for `/processor/bank_transfer/create`"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#processor_bank_transfer_create_response"
            }
        }

    bank_transfer: BankTransfer = Field()
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

ProcessorBankTransferCreateResponse.update_forward_refs()
