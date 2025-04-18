# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.client_provided_enhanced_transaction import ClientProvidedEnhancedTransaction




class TransactionsEnhanceGetResponse(BaseModel):
    """TransactionsEnhanceGetResponse defines the response schema for `/beta/transactions/v1/enhance`."""


    enhanced_transactions: List[ClientProvidedEnhancedTransaction] = Field( description="An array of enhanced transactions.")

TransactionsEnhanceGetResponse.update_forward_refs()
