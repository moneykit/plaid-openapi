# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class RemovedTransaction(BaseModel):
    """A representation of a removed transaction"""


    transaction_id: Optional[str] = Field(default=None, description="The ID of the removed transaction.")

RemovedTransaction.update_forward_refs()
