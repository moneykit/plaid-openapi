# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.credit_amount_with_currency import CreditAmountWithCurrency
from plaid_skel.models.credit_bank_income_historical_summary import CreditBankIncomeHistoricalSummary




class CreditBankIncomeSummary(BaseModel):
    """Summary for bank income across all income sources and items (max history of 730 days)."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#credit_bank_income_summary"
            }
        }

    total_amount: Optional[float] = Field(default=None, description="Total amount of earnings across all the income sources in the end user's Items for the days requested by the client. This may return an incorrect value if the summary includes income sources in multiple currencies. Please use [`total_amounts`](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-bank-income-summary-total-amounts) instead.")
    iso_currency_code: Optional[str] = Field(default=None, description="The ISO 4217 currency code of the amount or balance. Please use [`total_amounts`](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-bank-income-summary-total-amounts) instead.")
    unofficial_currency_code: Optional[str] = Field(default=None, description="The unofficial currency code associated with the amount or balance. Always `null` if `iso_currency_code` is non-null. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries. Please use [`total_amounts`](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-bank-income-summary-total-amounts) instead.")
    total_amounts: Optional[List[CreditAmountWithCurrency]] = Field(default=None, description="Total amount of earnings across all the income sources in the end user's Items for the days requested by the client. This can contain multiple amounts, with each amount denominated in one unique currency.")
    start_date: Optional[date] = Field(default=None, description="The earliest date within the days requested in which all income sources identified by Plaid appear in a user's account. The date will be returned in an ISO 8601 format (YYYY-MM-DD).")
    end_date: Optional[date] = Field(default=None, description="The latest date in which all income sources identified by Plaid appear in the user's account. The date will be returned in an ISO 8601 format (YYYY-MM-DD).")
    income_sources_count: Optional[int] = Field(default=None, description="Number of income sources per end user.")
    income_categories_count: Optional[int] = Field(default=None, description="Number of income categories per end user.")
    income_transactions_count: Optional[int] = Field(default=None, description="Number of income transactions per end user.")
    historical_summary: Optional[List[CreditBankIncomeHistoricalSummary]] = Field(default=None,)

CreditBankIncomeSummary.update_forward_refs()
