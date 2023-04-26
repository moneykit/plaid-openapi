# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class DepositSwitchTargetAccount(BaseModel):
    """The deposit switch destination account"""


    account_number: str = Field( description="Account number for deposit switch destination")
    routing_number: str = Field( description="Routing number for deposit switch destination")
    account_name: str = Field( description="The name of the deposit switch destination account, as it will be displayed to the end user in the Deposit Switch interface. It is not required to match the name used in online banking.")
    account_subtype: str = Field( description="The account subtype of the account, either `checking` or `savings`.")

DepositSwitchTargetAccount.update_forward_refs()
