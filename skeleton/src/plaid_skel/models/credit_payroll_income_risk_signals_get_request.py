# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class CreditPayrollIncomeRiskSignalsGetRequest(BaseModel):
    """CreditPayrollIncomeRiskSignalsGetRequest defines the request schema for `/beta/credit/payroll_income/risk_signals/get`"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#credit_payroll_income_risk_signals_get_request"
            }
        }

    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    user_token: Optional[str] = Field(default=None, description="The user token associated with the User data is being requested for.")

CreditPayrollIncomeRiskSignalsGetRequest.update_forward_refs()
