# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.webhook_environment_values import WebhookEnvironmentValues




class RecurringTransactionsUpdateWebhook(BaseModel):
    """Fired when recurring transactions data is updated. This includes when a new recurring stream is detected or when a new transaction is added to an existing recurring stream. The `RECURRING_TRANSACTIONS_UPDATE` webhook will also fire when one or more attributes of the recurring stream changes, which is usually a result of the addition, update, or removal of transactions to the stream.  After receipt of this webhook, the updated data can be fetched from `/transactions/recurring/get`."""


    webhook_type: str = Field( description="`TRANSACTIONS`")
    webhook_code: str = Field( description="`RECURRING_TRANSACTIONS_UPDATE`")
    item_id: str = Field( description="The `item_id` of the Item associated with this webhook, warning, or error")
    account_ids: List[str] = Field( description="A list of `account_ids` for accounts that have new or updated recurring transactions data.")
    environment: WebhookEnvironmentValues = Field()

RecurringTransactionsUpdateWebhook.update_forward_refs()
