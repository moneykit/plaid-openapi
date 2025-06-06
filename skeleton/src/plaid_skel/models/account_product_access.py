# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class AccountProductAccess(BaseModel):
    """Allow the application to access specific products on this account"""


    account_data: Optional[bool] = Field(default=None, description="Allow the application to access account data. Only used by certain partners. If relevant to the partner and unset, defaults to `true`.")
    statements: Optional[bool] = Field(default=None, description="Allow the application to access bank statements. Only used by certain partners. If relevant to the partner and unset, defaults to `true`.")
    tax_documents: Optional[bool] = Field(default=None, description="Allow the application to access tax documents. Only used by certain partners. If relevant to the partner and unset, defaults to `true`.")

AccountProductAccess.update_forward_refs()
