# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.credit_session_error import CreditSessionError
from plaid_skel.models.credit_session_results import CreditSessionResults




class CreditSession(BaseModel):
    """Metadata and results for a Link session"""


    link_session_id: Optional[str] = Field(default=None, description="The unique identifier associated with the Link session. This identifier matches the `link_session_id` returned in the onSuccess/onExit callbacks.")
    session_start_time: Optional[datetime_] = Field(default=None, description="The time when the Link session started")
    results: Optional[CreditSessionResults] = Field(default=None,)
    errors: Optional[List[CreditSessionError]] = Field(default=None, description="The set of errors that occurred during the Link session.")

CreditSession.update_forward_refs()
