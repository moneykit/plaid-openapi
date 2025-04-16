# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.transfer_authorization_guarantee_decision_rationale_code import TransferAuthorizationGuaranteeDecisionRationaleCode




class TransferAuthorizationGuaranteeDecisionRationale(BaseModel):
    """The rationale for Plaid's decision to not guarantee a transfer. Will be `null` unless `guarantee_decision` is `NOT_GUARANTEED`."""
    model_config = ConfigDict(json_schema_extra={"nullable": True})

    code: TransferAuthorizationGuaranteeDecisionRationaleCode = Field()
    description: str = Field( description="A human-readable description of why the transfer cannot be guaranteed.")

TransferAuthorizationGuaranteeDecisionRationale.update_forward_refs()
