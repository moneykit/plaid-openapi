# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.plaid_error import PlaidError
from plaid_skel.models.webhook_environment_values import WebhookEnvironmentValues




class NewAccountsAvailableWebhook(BaseModel):
    """Fired when Plaid detects a new account for Items created or updated with [Account Select v2](https://plaid.com/docs/link/customization/#account-select). Upon receiving this webhook, you can prompt your users to share new accounts with you through [Account Select v2 update mode](https://plaid.com/docs/link/update-mode/#using-update-mode-to-request-new-accounts)."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#new_accounts_available_webhook"
            }
        }

    webhook_type: Optional[str] = Field(default=None, description="`ITEM`")
    webhook_code: Optional[str] = Field(default=None, description="`NEW_ACCOUNTS_AVAILABLE`")
    item_id: Optional[str] = Field(default=None, description="The `item_id` of the Item associated with this webhook, warning, or error")
    error: Optional[PlaidError] = Field(default=None,)
    environment: Optional[WebhookEnvironmentValues] = Field(default=None,)

NewAccountsAvailableWebhook.update_forward_refs()
