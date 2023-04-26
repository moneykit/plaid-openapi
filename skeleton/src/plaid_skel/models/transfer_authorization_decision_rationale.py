# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.transfer_authorization_decision_rationale_code import TransferAuthorizationDecisionRationaleCode




class TransferAuthorizationDecisionRationale(BaseModel):
    """The rationale for Plaid's decision regarding a proposed transfer. It is always set for `declined` decisions, and may or may not be null for `approved` decisions."""

    class Config:
        schema_extra = {"nullable": True}

    code: TransferAuthorizationDecisionRationaleCode = Field()
    description: str = Field( description="A human-readable description of the code associated with a transfer approval or transfer decline.")

TransferAuthorizationDecisionRationale.update_forward_refs()
