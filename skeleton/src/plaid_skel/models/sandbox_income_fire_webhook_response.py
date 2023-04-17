# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class SandboxIncomeFireWebhookResponse(BaseModel):
    """SandboxIncomeFireWebhookResponse defines the response schema for `/sandbox/income/fire_webhook`"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#sandbox_income_fire_webhook_response"
            }
        }

    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

SandboxIncomeFireWebhookResponse.update_forward_refs()
