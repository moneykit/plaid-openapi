# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class TransferDevice(BaseModel):
    """Information about the device being used to initiate the authorization."""


    ip_address: str = Field( description="The IP address of the device being used to initiate the authorization.")
    user_agent: str = Field( description="The user agent of the device being used to initiate the authorization.")

TransferDevice.update_forward_refs()
