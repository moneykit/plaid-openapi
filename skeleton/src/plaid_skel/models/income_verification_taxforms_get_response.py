# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.document_metadata import DocumentMetadata
from plaid_skel.models.plaid_error import PlaidError
from plaid_skel.models.taxform import Taxform




class IncomeVerificationTaxformsGetResponse(BaseModel):
    """IncomeVerificationTaxformsGetResponse defines the response schema for `/income/verification/taxforms/get`"""


    request_id: Optional[str] = Field(default=None, description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")
    document_metadata: List[DocumentMetadata] = Field()
    taxforms: List[Taxform] = Field( description="A list of forms.")
    error: Optional[PlaidError] = Field(default=None,)

IncomeVerificationTaxformsGetResponse.update_forward_refs()
