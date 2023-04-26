# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class AssetReportAuditCopyCreateResponse(BaseModel):
    """AssetReportAuditCopyCreateResponse defines the response schema for `/asset_report/audit_copy/get`"""


    audit_copy_token: str = Field( description="A token that can be shared with a third party auditor to allow them to obtain access to the Asset Report. This token should be stored securely.")
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

AssetReportAuditCopyCreateResponse.update_forward_refs()
