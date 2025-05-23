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




class HistoricalUpdateWebhook(BaseModel):
    """Fired when an Item's historical transaction pull is completed and Plaid has prepared as much historical transaction data as possible for the Item. Once this webhook has been fired, transaction data beyond the most recent 30 days can be fetched for the Item. If [Account Select v2](https://plaid.com/docs/link/customization/#account-select) is enabled, this webhook will also be fired if account selections for the Item are updated, with `new_transactions` set to the number of net new transactions pulled after the account selection update.  This webhook is intended for use with `/transactions/get`; if you are using the newer `/transactions/sync` endpoint, this webhook will still be fired to maintain backwards compatibility, but it is recommended to listen for and respond to the `SYNC_UPDATES_AVAILABLE` webhook instead."""


    webhook_type: str = Field( description="`TRANSACTIONS`")
    webhook_code: str = Field( description="`HISTORICAL_UPDATE`")
    error: Optional[PlaidError] = Field(default=None,)
    new_transactions: float = Field( description="The number of new, unfetched transactions available")
    item_id: str = Field( description="The `item_id` of the Item associated with this webhook, warning, or error")
    environment: WebhookEnvironmentValues = Field()

HistoricalUpdateWebhook.update_forward_refs()
