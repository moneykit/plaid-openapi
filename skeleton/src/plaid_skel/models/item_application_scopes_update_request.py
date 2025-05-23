# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.scopes import Scopes
from plaid_skel.models.scopes_context import ScopesContext




class ItemApplicationScopesUpdateRequest(BaseModel):
    """ItemApplicationScopesUpdateRequest defines the request schema for `/item/application/scopes/update`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    access_token: str = Field( description="The access token associated with the Item data is being requested for.")
    application_id: str = Field( description="This field will map to the application ID that is returned from /item/applications/list, or provided to the institution in an oauth redirect.")
    scopes: Scopes = Field()
    state: Optional[str] = Field(default=None, description="When scopes are updated during enrollment, this field must be populated with the state sent to the partner in the OAuth Login URI. This field is required when the context is `ENROLLMENT`.")
    context: ScopesContext = Field()

ItemApplicationScopesUpdateRequest.update_forward_refs()
