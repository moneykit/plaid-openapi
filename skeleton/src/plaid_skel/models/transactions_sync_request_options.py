# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class TransactionsSyncRequestOptions(BaseModel):
    """An optional object to be used with the request. If specified, `options` must not be `null`."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#transactions_sync_request_options"
            }
        }

    include_original_description: Optional[bool] = Field(default=None, description="Include the raw unparsed transaction description from the financial institution. This field is disabled by default. If you need this information in addition to the parsed data provided, contact your Plaid Account Manager.")
    include_personal_finance_category: Optional[bool] = Field(default=None, description="Include the [`personal_finance_category`](https://plaid.com/docs/api/products/transactions/#transactions-sync-response-added-personal-finance-category) object in the response.  See the [`taxonomy csv file`](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) for a full list of personal finance categories.  We’re introducing Category Rules - a new beta endpoint that will enable you to change the `personal_finance_category` for a transaction based on your users’ needs. When rules are set, the selected category will override the Plaid provided category. To learn more, send a note to transactions-feedback@plaid.com.")
    include_logo_and_counterparty_beta: Optional[bool] = Field(default=None, description="Include counterparties and extra merchant fields in the transaction. This field is disabled by default. If you need this information in addition to the parsed data provided, contact your Plaid Account Manager.")

TransactionsSyncRequestOptions.update_forward_refs()
