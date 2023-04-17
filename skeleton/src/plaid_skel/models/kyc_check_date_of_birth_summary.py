# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.match_summary_code import MatchSummaryCode




class KYCCheckDateOfBirthSummary(BaseModel):
    """Result summary object specifying how the `date_of_birth` field matched."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#kyc_check_date_of_birth_summary"
            }
        }

    summary: MatchSummaryCode = Field()

KYCCheckDateOfBirthSummary.update_forward_refs()
