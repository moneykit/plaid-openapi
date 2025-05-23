# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.account_access import AccountAccess
from plaid_skel.models.product_access import ProductAccess




class Scopes(BaseModel):
    """The scopes object"""


    product_access: Optional[ProductAccess] = Field(default=None,)
    accounts: Optional[List[AccountAccess]] = Field(default=None,)
    new_accounts: Optional[bool] = Field(default=None, description="Allow access to newly opened accounts as they are opened. If unset, defaults to `true`.")

Scopes.update_forward_refs()
