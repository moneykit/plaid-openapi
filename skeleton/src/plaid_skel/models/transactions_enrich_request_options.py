# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class TransactionsEnrichRequestOptions(BaseModel):
    """An optional object to be used with the request."""


    include_legacy_category: Optional[bool] = Field(default=None, description="Include `legacy_category` and `legacy_category_id` in the response (in addition to the default `personal_finance_category`).  Categories are based on Plaid's legacy taxonomy. For a full list of legacy categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget).")

TransactionsEnrichRequestOptions.update_forward_refs()
