# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.plaid_error import PlaidError
from plaid_skel.models.webhook_environment_values import WebhookEnvironmentValues




class DefaultUpdateWebhook(BaseModel):
    """Fired when new transaction data is available for an Item. Plaid will typically check for new transaction data several times a day.  This webhook is intended for use with `/transactions/get`; if you are using the newer `/transactions/sync` endpoint, this webhook will still be fired to maintain backwards compatibility, but it is recommended to listen for and respond to the `SYNC_UPDATES_AVAILABLE` webhook instead. """


    webhook_type: str = Field( description="`TRANSACTIONS`")
    webhook_code: str = Field( description="`DEFAULT_UPDATE`")
    error: Optional[PlaidError] = Field(default=None,)
    new_transactions: float = Field( description="The number of new transactions detected since the last time this webhook was fired.")
    item_id: str = Field( description="The `item_id` of the Item the webhook relates to.")
    environment: WebhookEnvironmentValues = Field()

DefaultUpdateWebhook.update_forward_refs()
