# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.weak_alias_determination import WeakAliasDetermination




class IndividualScreeningHitNames(BaseModel):
    """Name information for the associated individual watchlist hit"""


    full: str = Field( description="The full name of the individual, including all parts.")
    is_primary: bool = Field( description="Primary names are those most commonly used to refer to this person. Only one name will ever be marked as primary.")
    weak_alias_determination: WeakAliasDetermination = Field()

IndividualScreeningHitNames.update_forward_refs()
