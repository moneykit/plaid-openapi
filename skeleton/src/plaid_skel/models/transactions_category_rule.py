# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.transactions_rule_details import TransactionsRuleDetails




class TransactionsCategoryRule(BaseModel):
    """A representation of a transactions category rule."""


    id: Optional[str] = Field(default=None, description="A unique identifier of the rule created")
    item_id: Optional[str] = Field(default=None, description="A unique identifier of the Item the rule was created for.")
    created_at: Optional[datetime] = Field(default=None, description="Date and time when a rule was created in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( `YYYY-MM-DDTHH:mm:ssZ` ). ")
    personal_finance_category: Optional[str] = Field(default=None, description="Personal finance category unique identifier.  In the personal finance category taxonomy, this field is represented by the detailed category field. ")
    rule_details: Optional[TransactionsRuleDetails] = Field(default=None,)

TransactionsCategoryRule.update_forward_refs()
