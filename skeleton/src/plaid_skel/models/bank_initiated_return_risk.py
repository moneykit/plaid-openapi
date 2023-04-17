# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class BankInitiatedReturnRisk(BaseModel):
    """The object contains a risk score and a risk tier that evaluate the transaction return risk because an account is overdrawn or because an ineligible account is used. Common return codes in this category include: \"R01\", \"R02\", \"R03\", \"R04\", \"R06\", \"R08\",  \"R09\", \"R13\", \"R16\", \"R17\", \"R20\", \"R23\". These returns have a turnaround time of 2 banking days."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#bank_initiated_return_risk"
            }
        }

    score: int = Field( description="A score from 1-99 that indicates the transaction return risk: a higher risk score suggests a higher return likelihood.")
    risk_tier: int = Field( description="In the `bank_initiated_return_risk` object, there are eight risk tiers corresponding to the scores:   1: Predicted bank-initiated return incidence rate between 0.0% - 0.5%   2: Predicted bank-initiated return incidence rate between 0.5% - 1.5%   3: Predicted bank-initiated return incidence rate between 1.5% - 3%   4: Predicted bank-initiated return incidence rate between 3% - 5%   5: Predicted bank-initiated return incidence rate between 5% - 10%   6: Predicted bank-initiated return incidence rate between 10% - 15%   7: Predicted bank-initiated return incidence rate between 15% and 50%   8: Predicted bank-initiated return incidence rate greater than 50% ")

    @validator("score")
    def score_max(cls, value):
        assert value <= 99
        return value

    @validator("score")
    def score_min(cls, value):
        assert value >= 1
        return value

    @validator("risk_tier")
    def risk_tier_max(cls, value):
        assert value <= 8
        return value

    @validator("risk_tier")
    def risk_tier_min(cls, value):
        assert value >= 1
        return value

BankInitiatedReturnRisk.update_forward_refs()
