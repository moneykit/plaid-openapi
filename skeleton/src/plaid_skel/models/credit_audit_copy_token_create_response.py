# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class CreditAuditCopyTokenCreateResponse(BaseModel):
    """CreditAuditCopyTokenCreateResponse defines the response schema for `/credit/audit_copy_token/get`"""


    audit_copy_token: str = Field( description="A token that can be shared with a third party auditor, which allows them to fetch the Asset Reports attached to the token. This token should be stored securely.")
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

CreditAuditCopyTokenCreateResponse.update_forward_refs()
