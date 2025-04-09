# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.transaction_stream import TransactionStream




class TransactionsRecurringGetResponse(BaseModel):
    """TransactionsRecurringGetResponse defines the response schema for `/transactions/recurring/get`"""


    inflow_streams: List[TransactionStream] = Field( description="An array of depository transaction streams.")
    outflow_streams: List[TransactionStream] = Field( description="An array of expense transaction streams.")
    updated_datetime: datetime = Field( description="Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDTHH:mm:ssZ`) indicating the last time transaction streams for the given account were updated on")
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

TransactionsRecurringGetResponse.update_forward_refs()
