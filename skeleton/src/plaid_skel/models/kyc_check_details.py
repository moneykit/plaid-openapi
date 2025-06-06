# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.kyc_check_address_summary import KYCCheckAddressSummary
from plaid_skel.models.kyc_check_date_of_birth_summary import KYCCheckDateOfBirthSummary
from plaid_skel.models.kyc_check_id_number_summary import KYCCheckIDNumberSummary
from plaid_skel.models.kyc_check_name_summary import KYCCheckNameSummary
from plaid_skel.models.kyc_check_phone_summary import KYCCheckPhoneSummary




class KYCCheckDetails(BaseModel):
    """Additional information for the `kyc_check` step. This field will be `null` unless `steps.kyc_check` has reached a terminal state of either `success` or `failed`."""
    model_config = ConfigDict(json_schema_extra={"nullable": True})

    status: str = Field( description="The outcome status for the associated Identity Verification attempt's `kyc_check` step. This field will always have the same value as `steps.kyc_check`.")
    address: KYCCheckAddressSummary = Field()
    name: KYCCheckNameSummary = Field()
    date_of_birth: KYCCheckDateOfBirthSummary = Field()
    id_number: KYCCheckIDNumberSummary = Field()
    phone_number: KYCCheckPhoneSummary = Field()

KYCCheckDetails.update_forward_refs()
