# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.action_state import ActionState
from plaid_skel.models.activity_type import ActivityType
from plaid_skel.models.scopes_nullable import ScopesNullable




class Activity(BaseModel):
    """Describes a consent activity."""


    activity: ActivityType = Field()
    initiated_date: str = Field( description="The date and time this activity was initiated [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format in UTC.")
    id: str = Field( description="A unique identifier for the activity")
    initiator: str = Field( description="Application ID of the client who initiated the activity.")
    state: ActionState = Field()
    target_application_id: Optional[str] = Field(default=None, description="This field will map to the application ID that is returned from /item/applications/list, or provided to the institution in an oauth redirect.")
    scopes: Optional[ScopesNullable] = Field(default=None,)

Activity.update_forward_refs()
