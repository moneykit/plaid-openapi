# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.credit_freddie_mac_verification_of_assets_voa24 import CreditFreddieMacVerificationOfAssetsVOA24
from plaid_skel.models.credit_freddie_verification_of_employment_voe25 import CreditFreddieVerificationOfEmploymentVOE25




class CreditFreddieMacReportsGetResponse(BaseModel):
    """CreditFreddieMacReportsGetResponse defines the response schema for `/credit/freddie_mac/reports/get`"""


    voa: Optional[CreditFreddieMacVerificationOfAssetsVOA24] = Field(default=None,)
    voe: Optional[CreditFreddieVerificationOfEmploymentVOE25] = Field(default=None,)
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

CreditFreddieMacReportsGetResponse.update_forward_refs()
