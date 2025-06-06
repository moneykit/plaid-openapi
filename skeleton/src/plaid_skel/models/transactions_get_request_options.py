# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401




class TransactionsGetRequestOptions(BaseModel):
    """An optional object to be used with the request. If specified, `options` must not be `null`."""


    account_ids: Optional[List[str]] = Field(default=None, description="A list of `account_ids` to retrieve for the Item  Note: An error will be returned if a provided `account_id` is not associated with the Item.")
    count: Optional[int] = Field(default=None, description="The number of transactions to fetch.")
    offset: Optional[int] = Field(default=None, description="The number of transactions to skip. The default value is 0.")
    include_original_description: Optional[bool] = Field(default=None, description="Include the raw unparsed transaction description from the financial institution. This field is disabled by default. If you need this information in addition to the parsed data provided, contact your Plaid Account Manager, or submit a [Support request](https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/product-functionality) .")
    include_personal_finance_category: Optional[bool] = Field(default=None, description="Include the [`personal_finance_category`](https://plaid.com/docs/api/products/transactions/#transactions-get-response-transactions-personal-finance-category) object in the response.  See the [`taxonomy csv file`](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) for a full list of personal finance categories.  We’re introducing Category Rules - a new beta endpoint that will enable you to change the `personal_finance_category` for a transaction based on your users’ needs. When rules are set, the selected category will override the Plaid provided category. To learn more, send a note to transactions-feedback@plaid.com.")

    @field_validator("count")
    @classmethod
    def count_max(cls, value):
        assert value <= 500
        return value

    @field_validator("count")
    @classmethod
    def count_min(cls, value):
        assert value >= 1
        return value

    @field_validator("offset")
    @classmethod
    def offset_min(cls, value):
        assert value >= 0
        return value

TransactionsGetRequestOptions.update_forward_refs()
