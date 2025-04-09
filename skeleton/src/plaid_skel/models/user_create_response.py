# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class UserCreateResponse(BaseModel):
    """UserCreateResponse defines the response schema for `/user/create`"""


    user_token: str = Field( description="The user token associated with the User data is being requested for.")
    user_id: str = Field( description="The Plaid `user_id` of the User associated with this webhook, warning, or error.")
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

UserCreateResponse.update_forward_refs()
