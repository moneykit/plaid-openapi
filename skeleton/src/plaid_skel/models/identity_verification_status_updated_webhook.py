# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.webhook_environment_values import WebhookEnvironmentValues




class IdentityVerificationStatusUpdatedWebhook(BaseModel):
    """Fired when the status of an identity verification has been updated, which can be triggered via the dashboard or the API."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#identity_verification_status_updated_webhook"
            }
        }

    webhook_type: str = Field( description="`IDENTITY_VERIFICATION`")
    webhook_code: str = Field( description="`STATUS_UPDATED`")
    identity_verification_id: str = Field( description="The ID of the associated Identity Verification attempt.")
    environment: WebhookEnvironmentValues = Field()

IdentityVerificationStatusUpdatedWebhook.update_forward_refs()
