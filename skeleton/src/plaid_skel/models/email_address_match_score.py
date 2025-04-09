# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class EmailAddressMatchScore(BaseModel):
    """Score found by matching email provided by the API with the email on the account at the financial institution. 100 is a perfect match and 0 is a no match. If the account contains multiple owners, the maximum match score is filled."""
    model_config = ConfigDict(json_schema_extra={"nullable": True})

    score: Optional[int] = Field(default=None, description="Match score for normalized email. 100 is a perfect match and 0 is a no match. If the email is missing from either the API or financial institution, this is empty.")

EmailAddressMatchScore.update_forward_refs()
