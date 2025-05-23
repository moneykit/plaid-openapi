# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class ItemImportRequestOptions(BaseModel):
    """An optional object to configure `/item/import` request."""


    webhook: Optional[str] = Field(default=None, description="Specifies a webhook URL to associate with an Item. Plaid fires a webhook if credentials fail. ")

ItemImportRequestOptions.update_forward_refs()
