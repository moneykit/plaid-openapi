# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.webhook_environment_values import WebhookEnvironmentValues




class AutomaticallyVerifiedWebhook(BaseModel):
    """Fired when an Item is verified via automated micro-deposits. We recommend communicating to your users when this event is received to notify them that their account is verified and ready for use."""


    webhook_type: str = Field( description="`AUTH`")
    webhook_code: str = Field( description="`AUTOMATICALLY_VERIFIED`")
    account_id: str = Field( description="The `account_id` of the account associated with the webhook")
    item_id: str = Field( description="The `item_id` of the Item associated with this webhook, warning, or error")
    environment: WebhookEnvironmentValues = Field()

AutomaticallyVerifiedWebhook.update_forward_refs()
