# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.plaid_error import PlaidError
from plaid_skel.models.webhook_environment_values import WebhookEnvironmentValues




class ItemErrorWebhook(BaseModel):
    """Fired when an error is encountered with an Item. The error can be resolved by having the user go through Link’s update mode."""


    webhook_type: str = Field( description="`ITEM`")
    webhook_code: str = Field( description="`ERROR`")
    item_id: str = Field( description="The `item_id` of the Item associated with this webhook, warning, or error")
    error: Optional[PlaidError] = Field(default=None,)
    environment: WebhookEnvironmentValues = Field()

ItemErrorWebhook.update_forward_refs()
