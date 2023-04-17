# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.webhook_environment_values import WebhookEnvironmentValues




class RecurringCancelledWebhook(BaseModel):
    """Fired when a recurring transfer is cancelled by Plaid."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#recurring_cancelled_webhook"
            }
        }

    webhook_type: str = Field( description="`TRANSFER`")
    webhook_code: str = Field( description="`RECURRING_CANCELLED`")
    recurring_transfer_id: str = Field( description="Plaid’s unique identifier for a recurring transfer.")
    environment: WebhookEnvironmentValues = Field()

RecurringCancelledWebhook.update_forward_refs()
