# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class TransferIntentGetFailureReason(BaseModel):
    """The reason for a failed transfer intent. Returned only if the transfer intent status is `failed`. Null otherwise."""

    class Config:
        schema_extra = {"nullable": True}

    error_type: Optional[str] = Field(default=None, description="A broad categorization of the error.")
    error_code: Optional[str] = Field(default=None, description="A code representing the reason for a failed transfer intent (i.e., an API error or the authorization being declined).")
    error_message: Optional[str] = Field(default=None, description="A human-readable description of the code associated with a failed transfer intent.")

TransferIntentGetFailureReason.update_forward_refs()
