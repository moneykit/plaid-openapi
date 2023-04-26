# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class IdentityVerificationRetryRequestStepsObject(BaseModel):
    """Instructions for the `custom` retry strategy specifying which steps should be required or skipped.   Note:   This field must be provided when the retry strategy is `custom` and must be omitted otherwise.  Custom retries override settings in your Plaid Template. For example, if your Plaid Template has `verify_sms` disabled, a custom retry with `verify_sms` enabled will still require the step.  The `selfie_check` step is currently not supported on the sandbox server. Sandbox requests will silently disable the `selfie_check` step when provided."""

    class Config:
        schema_extra = {"nullable": True}

    verify_sms: bool = Field( description="A boolean field specifying whether the new session should require or skip the `verify_sms` step.")
    kyc_check: bool = Field( description="A boolean field specifying whether the new session should require or skip the `kyc_check` step.")
    documentary_verification: bool = Field( description="A boolean field specifying whether the new session should require or skip the `documentary_verification` step.")
    selfie_check: bool = Field( description="A boolean field specifying whether the new session should require or skip the `selfie_check` step.")

IdentityVerificationRetryRequestStepsObject.update_forward_refs()
