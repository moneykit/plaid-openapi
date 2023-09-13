# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401
from plaid_skel.models.signal_decision_outcome import SignalDecisionOutcome
from plaid_skel.models.signal_payment_method import SignalPaymentMethod




class SignalDecisionReportRequest(BaseModel):
    """SignalDecisionReportRequest defines the request schema for `/signal/decision/report`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    client_transaction_id: str = Field( description="Must be the same as the `client_transaction_id` supplied when calling `/signal/evaluate`")
    initiated: bool = Field( description="`true` if the ACH transaction was initiated, `false` otherwise.  This field must be returned as a boolean. If formatted incorrectly, this will result in an [`INVALID_FIELD`](/docs/errors/invalid-request/#invalid_field) error.")
    days_funds_on_hold: Optional[int] = Field(default=None, description="The actual number of days (hold time) since the ACH debit transaction that you wait before making funds available to your customers. The holding time could affect the ACH return rate.  For example, use 0 if you make funds available to your customers instantly or the same day following the debit transaction, or 1 if you make funds available the next day following the debit initialization.")
    decision_outcome: Optional[SignalDecisionOutcome] = Field(default=None,)
    payment_method: Optional[SignalPaymentMethod] = Field(default=None,)
    amount_instantly_available: Optional[float] = Field(default=None, description="The amount (in USD) made available to your customers instantly following the debit transaction. It could be a partial amount of the requested transaction (example: 102.05).")

    @field_validator("client_transaction_id")
    @classmethod
    def client_transaction_id_min_length(cls, value):
        assert len(value) >= 1
        return value

    @field_validator("client_transaction_id")
    @classmethod
    def client_transaction_id_max_length(cls, value):
        assert len(value) <= 36
        return value

    @field_validator("days_funds_on_hold")
    @classmethod
    def days_funds_on_hold_min(cls, value):
        assert value >= 0
        return value

SignalDecisionReportRequest.update_forward_refs()
