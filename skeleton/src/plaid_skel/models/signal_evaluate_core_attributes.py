# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class SignalEvaluateCoreAttributes(BaseModel):
    """The core attributes object contains additional data that can be used to assess the ACH return risk. Examples of data include:  `days_since_first_plaid_connection`: The number of days since the first time the Item was connected to an application via Plaid `plaid_connections_count_7d`: The number of times the Item has been connected to applications via Plaid over the past 7 days `plaid_connections_count_30d`: The number of times the Item has been connected to applications via Plaid over the past 30 days `total_plaid_connections_count`: The number of times the Item has been connected to applications via Plaid `is_savings_or_money_market_account`: Indicates whether the ACH transaction funding account is a savings/money market account  For the full list and detailed documentation of core attributes available, or to request that core attributes not be returned, contact Sales or your Plaid account manager"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#signal_evaluate_core_attributes"
            }
        }

    unauthorized_transactions_count_7d: Optional[int] = Field(default=None, description="We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 7 days from the account that will be debited.")
    unauthorized_transactions_count_30d: Optional[int] = Field(default=None, description="We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 30 days from the account that will be debited.")
    unauthorized_transactions_count_60d: Optional[int] = Field(default=None, description="We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 60 days from the account that will be debited.")
    unauthorized_transactions_count_90d: Optional[int] = Field(default=None, description="We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 90 days from the account that will be debited.")
    nsf_overdraft_transactions_count_7d: Optional[int] = Field(default=None, description="We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 7 days from the account that will be debited.")
    nsf_overdraft_transactions_count_30d: Optional[int] = Field(default=None, description="We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 30 days from the account that will be debited.")
    nsf_overdraft_transactions_count_60d: Optional[int] = Field(default=None, description="We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 60 days from the account that will be debited.")
    nsf_overdraft_transactions_count_90d: Optional[int] = Field(default=None, description="We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 90 days from the account that will be debited.")
    days_since_first_plaid_connection: Optional[int] = Field(default=None, description="The number of days since the first time the Item was connected to an application via Plaid")
    plaid_connections_count_7d: Optional[int] = Field(default=None, description="The number of times the Item has been connected to applications via Plaid over the past 7 days")
    plaid_connections_count_30d: Optional[int] = Field(default=None, description="The number of times the Item has been connected to applications via Plaid over the past 30 days")
    total_plaid_connections_count: Optional[int] = Field(default=None, description="The total number of times the Item has been connected to applications via Plaid")
    is_savings_or_money_market_account: Optional[bool] = Field(default=None, description="Indicates if the ACH transaction funding account is a savings/money market account")
    total_credit_transactions_amount_10d: Optional[float] = Field(default=None, description="The total credit (inflow) transaction amount over the past 10 days from the account that will be debited")
    total_debit_transactions_amount_10d: Optional[float] = Field(default=None, description="The total debit (outflow) transaction amount over the past 10 days from the account that will be debited")
    p50_credit_transactions_amount_28d: Optional[float] = Field(default=None, description="The 50th percentile of all credit (inflow) transaction amounts over the past 28 days from the account that will be debited")
    p50_debit_transactions_amount_28d: Optional[float] = Field(default=None, description="The 50th percentile of all debit (outflow) transaction amounts over the past 28 days from the account that will be debited")
    p95_credit_transactions_amount_28d: Optional[float] = Field(default=None, description="The 95th percentile of all credit (inflow) transaction amounts over the past 28 days from the account that will be debited")
    p95_debit_transactions_amount_28d: Optional[float] = Field(default=None, description="The 95th percentile of all debit (outflow) transaction amounts over the past 28 days from the account that will be debited")
    days_with_negative_balance_count_90d: Optional[int] = Field(default=None, description="The number of days within the past 90 days when the account that will be debited had a negative end-of-day available balance")
    p90_eod_balance_30d: Optional[float] = Field(default=None, description="The 90th percentile of the end-of-day available balance over the past 30 days of the account that will be debited")
    p90_eod_balance_60d: Optional[float] = Field(default=None, description="The 90th percentile of the end-of-day available balance over the past 60 days of the account that will be debited")
    p90_eod_balance_90d: Optional[float] = Field(default=None, description="The 90th percentile of the end-of-day available balance over the past 90 days of the account that will be debited")
    p10_eod_balance_30d: Optional[float] = Field(default=None, description="The 10th percentile of the end-of-day available balance over the past 30 days of the account that will be debited")
    p10_eod_balance_60d: Optional[float] = Field(default=None, description="The 10th percentile of the end-of-day available balance over the past 60 days of the account that will be debited")
    p10_eod_balance_90d: Optional[float] = Field(default=None, description="The 10th percentile of the end-of-day available balance over the past 90 days of the account that will be debited")
    available_balance: Optional[float] = Field(default=None, description="Available balance, as of the `balance_last_updated` time. The available balance is the current balance less any outstanding holds or debits that have not yet posted to the account.")
    current_balance: Optional[float] = Field(default=None, description="Current balance, as of the `balance_last_updated` time. The current balance is the total amount of funds in the account.")
    balance_last_updated: Optional[datetime] = Field(default=None, description="Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DDTHH:mm:ssZ) indicating the last time that the balance for the given account has been updated.")
    phone_change_count_28d: Optional[int] = Field(default=None, description="The number of times the account's phone numbers on file have changed over the past 28 days")
    phone_change_count_90d: Optional[int] = Field(default=None, description="The number of times the account's phone numbers on file have changed over the past 90 days")
    email_change_count_28d: Optional[int] = Field(default=None, description="The number of times the account's email addresses on file have changed over the past 28 days")
    email_change_count_90d: Optional[int] = Field(default=None, description="The number of times the account's email addresses on file have changed over the past 90 days")
    address_change_count_28d: Optional[int] = Field(default=None, description="The number of times the account's addresses on file have changed over the past 28 days")
    address_change_count_90d: Optional[int] = Field(default=None, description="The number of times the account's addresses on file have changed over the past 90 days")
    plaid_non_oauth_authentication_attempts_count_3d: Optional[int] = Field(default=None, description="The number of non-OAuth authentication attempts via Plaid for this bank account over the past 3 days")
    plaid_non_oauth_authentication_attempts_count_7d: Optional[int] = Field(default=None, description="The number of non-OAuth authentication attempts via Plaid for this bank account over the past 7 days")
    plaid_non_oauth_authentication_attempts_count_30d: Optional[int] = Field(default=None, description="The number of non-OAuth authentication attempts via Plaid for this bank account over the past 30 days")
    failed_plaid_non_oauth_authentication_attempts_count_3d: Optional[int] = Field(default=None, description="The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 3 days")
    failed_plaid_non_oauth_authentication_attempts_count_7d: Optional[int] = Field(default=None, description="The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 7 days")
    failed_plaid_non_oauth_authentication_attempts_count_30d: Optional[int] = Field(default=None, description="The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 30 days")
    debit_transactions_count_10d: Optional[int] = Field(default=None, description="The total number of debit (outflow) transactions over the past 10 days from the account that will be debited")
    credit_transactions_count_10d: Optional[int] = Field(default=None, description="The total number of credit (inflow) transactions over the past 10 days from the account that will be debited")
    debit_transactions_count_30d: Optional[int] = Field(default=None, description="The total number of debit (outflow) transactions over the past 30 days from the account that will be debited")
    credit_transactions_count_30d: Optional[int] = Field(default=None, description="The total number of credit (inflow) transactions over the past 30 days from the account that will be debited")
    debit_transactions_count_60d: Optional[int] = Field(default=None, description="The total number of debit (outflow) transactions over the past 60 days from the account that will be debited")
    credit_transactions_count_60d: Optional[int] = Field(default=None, description="The total number of credit (inflow) transactions over the past 60 days from the account that will be debited")
    debit_transactions_count_90d: Optional[int] = Field(default=None, description="The total number of debit (outflow) transactions over the past 90 days from the account that will be debited")
    credit_transactions_count_90d: Optional[int] = Field(default=None, description="The total number of credit (inflow) transactions over the past 90 days from the account that will be debited")
    total_debit_transactions_amount_30d: Optional[float] = Field(default=None, description="The total debit (outflow) transaction amount over the past 30 days from the account that will be debited")
    total_credit_transactions_amount_30d: Optional[float] = Field(default=None, description="The total credit (inflow) transaction amount over the past 30 days from the account that will be debited")
    total_debit_transactions_amount_60d: Optional[float] = Field(default=None, description="The total debit (outflow) transaction amount over the past 60 days from the account that will be debited")
    total_credit_transactions_amount_60d: Optional[float] = Field(default=None, description="The total credit (inflow) transaction amount over the past 60 days from the account that will be debited")
    total_debit_transactions_amount_90d: Optional[float] = Field(default=None, description="The total debit (outflow) transaction amount over the past 90 days from the account that will be debited")
    total_credit_transactions_amount_90d: Optional[float] = Field(default=None, description="The total credit (inflow) transaction amount over the past 90 days from the account that will be debited")
    p50_eod_balance_30d: Optional[float] = Field(default=None, description="The 50th percentile of the end-of-day available balance over the past 30 days of the account that will be debited")
    p50_eod_balance_60d: Optional[float] = Field(default=None, description="The 50th percentile of the end-of-day available balance over the past 60 days of the account that will be debited")
    p50_eod_balance_90d: Optional[float] = Field(default=None, description="The 50th percentile of the end-of-day available balance over the past 90 days of the account that will be debited")
    p50_eod_balance_31d_to_60d: Optional[float] = Field(default=None, description="The 50th percentile of the end-of-day available balance between day 31 and day 60 over the past 60 days of the account that will be debited")
    p50_eod_balance_61d_to_90d: Optional[float] = Field(default=None, description="The 50th percentile of the end-of-day available balance between day 61 and day 90 over the past 60 days of the account that will be debited")
    p90_eod_balance_31d_to_60d: Optional[float] = Field(default=None, description="The 90th percentile of the end-of-day available balance between day 31 and day 60 over the past 60 days of the account that will be debited")
    p90_eod_balance_61d_to_90d: Optional[float] = Field(default=None, description="The 90th percentile of the end-of-day available balance between day 61 and day 90 over the past 60 days of the account that will be debited")
    p10_eod_balance_31d_to_60d: Optional[float] = Field(default=None, description="The 10th percentile of the end-of-day available balance between day 31 and day 60 over the past 60 days of the account that will be debited")
    p10_eod_balance_61d_to_90d: Optional[float] = Field(default=None, description="The 10th percentile of the end-of-day available balance between day 61 and day 90 over the past 60 days of the account that will be debited")
    transactions_last_updated: Optional[datetime] = Field(default=None, description="Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DDTHH:mm:ssZ) indicating the last time that the transactions for the given account have been updated.")

SignalEvaluateCoreAttributes.update_forward_refs()
