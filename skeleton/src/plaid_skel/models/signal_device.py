# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class SignalDevice(BaseModel):
    """Details about the end user's device"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#signal_device"
            }
        }

    ip_address: Optional[str] = Field(default=None, description="The IP address of the device that initiated the transaction")
    user_agent: Optional[str] = Field(default=None, description="The user agent of the device that initiated the transaction (e.g. \"Mozilla/5.0\")")

SignalDevice.update_forward_refs()
