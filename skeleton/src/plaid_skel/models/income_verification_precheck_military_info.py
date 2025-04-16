# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class IncomeVerificationPrecheckMilitaryInfo(BaseModel):
    """Data about military info in the income verification precheck."""
    model_config = ConfigDict(json_schema_extra={"nullable": True})

    is_active_duty: Optional[bool] = Field(default=None, description="Is the user currently active duty in the US military")
    branch: Optional[str] = Field(default=None, description="If the user is currently serving in the US military, the branch of the military in which they are serving Valid values: 'AIR FORCE', 'ARMY', 'COAST GUARD', 'MARINES', 'NAVY', 'UNKNOWN'")

IncomeVerificationPrecheckMilitaryInfo.update_forward_refs()
