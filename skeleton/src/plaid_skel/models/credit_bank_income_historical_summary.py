# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.credit_amount_with_currency import CreditAmountWithCurrency
from plaid_skel.models.credit_bank_income_transaction import CreditBankIncomeTransaction




class CreditBankIncomeHistoricalSummary(BaseModel):
    """The end user's monthly summary for the income source(s)."""


    total_amount: Optional[float] = Field(default=None, description="Total amount of earnings for the income source(s) of the user for the month in the summary. This may return an incorrect value if the summary includes income sources in multiple currencies. Please use [`total_amounts`](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-items-bank-income-sources-historical-summary-total-amounts) instead.")
    iso_currency_code: Optional[str] = Field(default=None, description="The ISO 4217 currency code of the amount or balance. Please use [`total_amounts`](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-items-bank-income-sources-historical-summary-total-amounts) instead.")
    unofficial_currency_code: Optional[str] = Field(default=None, description="The unofficial currency code associated with the amount or balance. Always `null` if `iso_currency_code` is non-null. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries. Please use [`total_amounts`](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-items-bank-income-sources-historical-summary-total-amounts) instead.")
    total_amounts: Optional[List[CreditAmountWithCurrency]] = Field(default=None, description="Total amount of earnings for the income source(s) of the user for the month in the summary. This can contain multiple amounts, with each amount denominated in one unique currency.")
    start_date: Optional[date_] = Field(default=None, description="The start date of the period covered in this monthly summary. This date will be the first day of the month, unless the month being covered is a partial month because it is the first month included in the summary and the date range being requested does not begin with the first day of the month. The date will be returned in an ISO 8601 format (YYYY-MM-DD).")
    end_date: Optional[date_] = Field(default=None, description="The end date of the period included in this monthly summary. This date will be the last day of the month, unless the month being covered is a partial month because it is the last month included in the summary and the date range being requested does not end with the last day of the month. The date will be returned in an ISO 8601 format (YYYY-MM-DD).")
    transactions: Optional[List[CreditBankIncomeTransaction]] = Field(default=None,)

CreditBankIncomeHistoricalSummary.update_forward_refs()
