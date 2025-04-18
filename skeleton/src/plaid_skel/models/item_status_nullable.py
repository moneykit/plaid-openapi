# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.item_status_investments import ItemStatusInvestments
from plaid_skel.models.item_status_last_webhook import ItemStatusLastWebhook
from plaid_skel.models.item_status_transactions import ItemStatusTransactions




class ItemStatusNullable(BaseModel):
    """Information about the last successful and failed transactions update for the Item."""
    model_config = ConfigDict(json_schema_extra={"nullable": True})

    investments: Optional[ItemStatusInvestments] = Field(default=None,)
    transactions: Optional[ItemStatusTransactions] = Field(default=None,)
    last_webhook: Optional[ItemStatusLastWebhook] = Field(default=None,)

ItemStatusNullable.update_forward_refs()
