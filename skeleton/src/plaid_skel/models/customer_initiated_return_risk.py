# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401




class CustomerInitiatedReturnRisk(BaseModel):
    """The object contains a risk score and a risk tier that evaluate the transaction return risk of an unauthorized debit. Common return codes in this category include: \"R05\", \"R07\", \"R10\", \"R11\", \"R29\". These returns typically have a return time frame of up to 60 calendar days. During this period, the customer of financial institutions can dispute a transaction as unauthorized."""


    score: int = Field( description="A score from 1-99 that indicates the transaction return risk: a higher risk score suggests a higher return likelihood.")
    risk_tier: int = Field( description="A tier corresponding to the projected likelihood that the transaction, if initiated, will be subject to a return.  In the `customer_initiated_return_risk` object, there are five risk tiers corresponding to the scores:   1: Predicted customer-initiated return incidence rate between 0.00% - 0.02%   2: Predicted customer-initiated return incidence rate between 0.02% - 0.05%   3: Predicted customer-initiated return incidence rate between 0.05% - 0.1%   4: Predicted customer-initiated return incidence rate between 0.1% - 0.5%   5: Predicted customer-initiated return incidence rate greater than 0.5% ")

    @field_validator("score")
    @classmethod
    def score_max(cls, value):
        assert value <= 99
        return value

    @field_validator("score")
    @classmethod
    def score_min(cls, value):
        assert value >= 1
        return value

    @field_validator("risk_tier")
    @classmethod
    def risk_tier_max(cls, value):
        assert value <= 5
        return value

    @field_validator("risk_tier")
    @classmethod
    def risk_tier_min(cls, value):
        assert value >= 1
        return value

CustomerInitiatedReturnRisk.update_forward_refs()
