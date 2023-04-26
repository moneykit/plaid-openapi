# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.identity_update_types import IdentityUpdateTypes
from plaid_skel.models.plaid_error import PlaidError
from plaid_skel.models.webhook_environment_values import WebhookEnvironmentValues




class IdentityDefaultUpdateWebhook(BaseModel):
    """Fired when a change to identity data has been detected on an Item. Items are checked for identity updates every 30-90 days. We recommend that upon receiving this webhook you make another call to `/identity/get` to fetch the user's latest identity data."""


    webhook_type: str = Field( description="`IDENTITY`")
    webhook_code: str = Field( description="`DEFAULT_UPDATE`")
    item_id: str = Field( description="The `item_id` of the Item associated with this webhook, warning, or error")
    account_ids_with_updated_identity: Dict[str, List[IdentityUpdateTypes]] = Field( description="An object with keys of `account_id`'s that are mapped to their respective identity attributes that changed.  Example: `{ \"XMBvvyMGQ1UoLbKByoMqH3nXMj84ALSdE5B58\": [\"PHONES\"] }` ")
    error: Optional[PlaidError] = Field(default=None,)
    environment: WebhookEnvironmentValues = Field()

IdentityDefaultUpdateWebhook.update_forward_refs()
