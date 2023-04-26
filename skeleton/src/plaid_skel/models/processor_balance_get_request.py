# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.processor_balance_get_request_options import ProcessorBalanceGetRequestOptions




class ProcessorBalanceGetRequest(BaseModel):
    """ProcessorBalanceGetRequest defines the request schema for `/processor/balance/get`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    processor_token: str = Field( description="The processor token obtained from the Plaid integration partner. Processor tokens are in the format: `processor-<environment>-<identifier>`")
    options: Optional[ProcessorBalanceGetRequestOptions] = Field(default=None,)

ProcessorBalanceGetRequest.update_forward_refs()
