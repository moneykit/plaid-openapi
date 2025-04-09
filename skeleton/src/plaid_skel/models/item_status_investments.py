# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class ItemStatusInvestments(BaseModel):
    """Information about the last successful and failed investments update for the Item."""
    model_config = ConfigDict(json_schema_extra={"nullable": True})

    last_successful_update: Optional[datetime] = Field(default=None, description="[ISO 8601](https://wikipedia.org/wiki/ISO_8601) timestamp of the last successful investments update for the Item. The status will update each time Plaid successfully connects with the institution, regardless of whether any new data is available in the update.")
    last_failed_update: Optional[datetime] = Field(default=None, description="[ISO 8601](https://wikipedia.org/wiki/ISO_8601) timestamp of the last failed investments update for the Item. The status will update each time Plaid fails an attempt to connect with the institution, regardless of whether any new data is available in the update.")

ItemStatusInvestments.update_forward_refs()
