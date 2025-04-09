# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class NameMatchScore(BaseModel):
    """Score found by matching name provided by the API with the name on the account at the financial institution. If the account contains multiple owners, the maximum match score is filled."""
    model_config = ConfigDict(json_schema_extra={"nullable": True})

    score: Optional[int] = Field(default=None, description="Represents the match score for name. 100 is a perfect score, 85-99 means a strong match, 50-84 is a partial match, less than 50 is a weak match and 0 is a complete mismatch. If the name is missing from either the API or financial institution, this is empty.")
    is_first_name_or_last_name_match: Optional[bool] = Field(default=None, description="first or last name completely matched, likely a family member")
    is_nickname_match: Optional[bool] = Field(default=None, description="nickname matched, example Jennifer and Jenn.")
    is_business_name_detected: Optional[bool] = Field(default=None, description="Is `true` if the name on either of the names that was matched for the score contained strings indicative of a business name, such as \"CORP\", \"LLC\", \"INC\", or \"LTD\". A `true` result generally indicates the entity is a business. However, a `false` result does not mean the entity is not a business, as some businesses do not use these strings in the names used for their financial institution accounts.")

NameMatchScore.update_forward_refs()
