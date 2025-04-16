# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.transfer_authorization_decision import TransferAuthorizationDecision
from plaid_skel.models.transfer_authorization_decision_rationale import TransferAuthorizationDecisionRationale
from plaid_skel.models.transfer_authorization_guarantee_decision import TransferAuthorizationGuaranteeDecision
from plaid_skel.models.transfer_authorization_guarantee_decision_rationale import TransferAuthorizationGuaranteeDecisionRationale
from plaid_skel.models.transfer_authorization_proposed_transfer import TransferAuthorizationProposedTransfer




class TransferAuthorization(BaseModel):
    """Contains the authorization decision for a proposed transfer."""


    id: str = Field( description="Plaid’s unique identifier for a transfer authorization.")
    created: datetime_ = Field( description="The datetime representing when the authorization was created, in the format `2006-01-02T15:04:05Z`.")
    decision: TransferAuthorizationDecision = Field()
    decision_rationale: Optional[TransferAuthorizationDecisionRationale] = Field(default=None,)
    guarantee_decision: Optional[TransferAuthorizationGuaranteeDecision] = Field(default=None,)
    guarantee_decision_rationale: Optional[TransferAuthorizationGuaranteeDecisionRationale] = Field(default=None,)
    proposed_transfer: TransferAuthorizationProposedTransfer = Field()

TransferAuthorization.update_forward_refs()
