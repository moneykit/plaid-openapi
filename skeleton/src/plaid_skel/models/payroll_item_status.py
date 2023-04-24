# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class PayrollItemStatus(BaseModel):
    """Details about the status of the payroll item."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#payroll_item_status"
            }
            , "nullable": True,
        }

    processing_status: Optional[str] = Field(default=None, description="Denotes the processing status for the verification.  `UNKNOWN`: The processing status could not be determined.  `PROCESSING_COMPLETE`: The processing has completed and the user has approved for sharing. The data is available to be retrieved.  `PROCESSING`: The verification is still processing. The data is not available yet.  `FAILED`: The processing failed to complete successfully.  `APPROVAL_STATUS_PENDING`: The processing has completed but the user has not yet approved the sharing of the data.")

PayrollItemStatus.update_forward_refs()
