# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class TransferConfigurationGetResponse(BaseModel):
    """Defines the response schema for `/transfer/configuration/get`"""


    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")
    max_single_transfer_amount: str = Field( description="The max limit of dollar amount of a single transfer (decimal string with two digits of precision e.g. \"10.00\").")
    max_daily_credit_amount: str = Field( description="The max limit of sum of dollar amount of credit transfers in last 24 hours (decimal string with two digits of precision e.g. \"10.00\").")
    max_daily_debit_amount: str = Field( description="The max limit of sum of dollar amount of debit transfers in last 24 hours (decimal string with two digits of precision e.g. \"10.00\").")
    max_monthly_amount: str = Field( description="The max limit of sum of dollar amount of credit and debit transfers in one calendar month (decimal string with two digits of precision e.g. \"10.00\").")
    iso_currency_code: str = Field( description="The currency of the dollar amount, e.g. \"USD\".")

TransferConfigurationGetResponse.update_forward_refs()
