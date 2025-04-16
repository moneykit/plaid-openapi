# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.client_provided_enriched_transaction import ClientProvidedEnrichedTransaction




class TransactionsEnrichGetResponse(BaseModel):
    """TransactionsEnrichGetResponse defines the response schema for `/transactions/enrich`."""


    enriched_transactions: List[ClientProvidedEnrichedTransaction] = Field( description="A list of enriched transactions.")
    request_id: Optional[str] = Field(default=None, description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

TransactionsEnrichGetResponse.update_forward_refs()
