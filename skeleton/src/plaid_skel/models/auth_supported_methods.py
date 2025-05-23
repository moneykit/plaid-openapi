# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class AuthSupportedMethods(BaseModel):
    """Metadata specifically related to which auth methods an institution supports."""
    model_config = ConfigDict(json_schema_extra={"nullable": True})

    instant_auth: bool = Field( description="Indicates if instant auth is supported.")
    instant_match: bool = Field( description="Indicates if instant match is supported.")
    automated_micro_deposits: bool = Field( description="Indicates if automated microdeposits are supported.")

AuthSupportedMethods.update_forward_refs()
