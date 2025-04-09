# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class AssetReportAuditCopyRemoveResponse(BaseModel):
    """AssetReportAuditCopyRemoveResponse defines the response schema for `/asset_report/audit_copy/remove`"""


    removed: bool = Field( description="`true` if the Audit Copy was successfully removed.")
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

AssetReportAuditCopyRemoveResponse.update_forward_refs()
