# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class BankTransferSweep(BaseModel):
    """BankTransferSweep describes a sweep transfer."""


    id: str = Field( description="Identifier of the sweep.")
    created_at: datetime_ = Field( description="The datetime when the sweep occurred, in RFC 3339 format.")
    amount: str = Field( description="The amount of the sweep.")
    iso_currency_code: str = Field( description="The currency of the sweep, e.g. \"USD\".")

BankTransferSweep.update_forward_refs()
