# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class WatchlistScreeningHitLocations(BaseModel):
    """Location information for the associated individual watchlist hit"""


    full: str = Field( description="The full location string, potentially including elements like street, city, postal codes and country codes. Note that this is not necessarily a complete or well-formatted address.")
    country: str = Field( description="Valid, capitalized, two-letter ISO code representing the country of this object. Must be in ISO 3166-1 alpha-2 form.")

    @validator("country")
    def country_min_length(cls, value):
        assert len(value) >= 2
        return value

WatchlistScreeningHitLocations.update_forward_refs()
