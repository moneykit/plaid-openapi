# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class TransferTestClock(BaseModel):
    """Defines the test clock for a transfer."""


    test_clock_id: str = Field( description="Plaid’s unique identifier for a test clock.")
    virtual_time: datetime_ = Field( description="The virtual timestamp on the test clock. This will be of the form `2006-01-02T15:04:05Z`.")

TransferTestClock.update_forward_refs()
