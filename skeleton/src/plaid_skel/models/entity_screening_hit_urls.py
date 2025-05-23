# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class EntityScreeningHitUrls(BaseModel):
    """URLs associated with the entity screening hit"""


    url: AnyUrl = Field( description="An 'http' or 'https' URL (must begin with either of those).")

EntityScreeningHitUrls.update_forward_refs()
