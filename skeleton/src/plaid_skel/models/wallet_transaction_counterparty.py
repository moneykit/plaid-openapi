# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.wallet_transaction_counterparty_numbers import WalletTransactionCounterpartyNumbers




class WalletTransactionCounterparty(BaseModel):
    """An object representing the e-wallet transaction's counterparty"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#wallet_transaction_counterparty"
            }
        }

    name: str = Field( description="The name of the counterparty")
    numbers: WalletTransactionCounterpartyNumbers = Field()

    @validator("name")
    def name_min_length(cls, value):
        assert len(value) >= 1
        return value

WalletTransactionCounterparty.update_forward_refs()
