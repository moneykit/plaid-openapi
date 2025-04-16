# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401
from plaid_skel.models.documentary_verification import DocumentaryVerification
from plaid_skel.models.identity_verification_status import IdentityVerificationStatus
from plaid_skel.models.identity_verification_step_summary import IdentityVerificationStepSummary
from plaid_skel.models.identity_verification_template_reference import IdentityVerificationTemplateReference
from plaid_skel.models.identity_verification_user_data import IdentityVerificationUserData
from plaid_skel.models.kyc_check_details import KYCCheckDetails
from plaid_skel.models.risk_check_details import RiskCheckDetails




class IdentityVerification(BaseModel):
    """A identity verification attempt represents a customer's attempt to verify their identity, reflecting the required steps for completing the session, the results for each step, and information collected in the process."""


    id: str = Field( description="ID of the associated Identity Verification attempt.")
    client_user_id: str = Field( description="An identifier to help you connect this object to your internal systems. For example, your database ID corresponding to this object.")
    created_at: datetime_ = Field( description="An ISO8601 formatted timestamp.")
    completed_at: Optional[datetime_] = Field(default=None, description="An ISO8601 formatted timestamp.")
    previous_attempt_id: Optional[str] = Field(default=None, description="The ID for the Identity Verification preceding this session. This field will only be filled if the current Identity Verification is a retry of a previous attempt.")
    shareable_url: Optional[str] = Field(default=None, description="A shareable URL that can be sent directly to the user to complete verification")
    template: IdentityVerificationTemplateReference = Field()
    user: IdentityVerificationUserData = Field()
    status: IdentityVerificationStatus = Field()
    steps: IdentityVerificationStepSummary = Field()
    documentary_verification: Optional[DocumentaryVerification] = Field(default=None,)
    kyc_check: Optional[KYCCheckDetails] = Field(default=None,)
    risk_check: Optional[RiskCheckDetails] = Field(default=None,)
    watchlist_screening_id: Optional[str] = Field(default=None, description="ID of the associated screening.")
    redacted_at: Optional[datetime_] = Field(default=None, description="An ISO8601 formatted timestamp.")

    @field_validator("client_user_id")
    @classmethod
    def client_user_id_min_length(cls, value):
        assert len(value) >= 1
        return value

IdentityVerification.update_forward_refs()
