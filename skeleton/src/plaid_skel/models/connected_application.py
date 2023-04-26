# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.scopes_nullable import ScopesNullable




class ConnectedApplication(BaseModel):
    """Describes the connected application for a particular end user."""


    application_id: str = Field( description="This field will map to the application ID that is returned from /item/applications/list, or provided to the institution in an oauth redirect.")
    name: str = Field( description="The name of the application")
    display_name: Optional[str] = Field(default=None, description="A human-readable name of the application for display purposes")
    logo_url: Optional[str] = Field(default=None, description="A URL that links to the application logo image.")
    application_url: Optional[str] = Field(default=None, description="The URL for the application's website")
    reason_for_access: Optional[str] = Field(default=None, description="A string provided by the connected app stating why they use their respective enabled products.")
    created_at: date = Field( description="The date this application was linked in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format in UTC.")
    scopes: Optional[ScopesNullable] = Field(default=None,)

ConnectedApplication.update_forward_refs()
