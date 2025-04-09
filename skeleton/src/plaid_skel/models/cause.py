# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.plaid_error_type import PlaidErrorType




class Cause(BaseModel):
    """An error object and associated `item_id` used to identify a specific Item and error when a batch operation operating on multiple Items has encountered an error in one of the Items."""


    error_type: PlaidErrorType = Field()
    error_code: str = Field( description="The particular error code. Safe for programmatic use.")
    error_message: str = Field( description="A developer-friendly representation of the error code. This may change over time and is not safe for programmatic use.")
    display_message: Optional[str] = Field(default=None, description="A user-friendly representation of the error code. `null` if the error is not related to user action.  This may change over time and is not safe for programmatic use.")
    request_id: Optional[str] = Field(default=None, description="A unique ID identifying the request, to be used for troubleshooting purposes. This field will be omitted in errors provided by webhooks.")
    causes: Optional[List[object]] = Field(default=None, description="In the Assets product, a request can pertain to more than one Item. If an error is returned for such a request, `causes` will return an array of errors containing a breakdown of these errors on the individual Item level, if any can be identified.  `causes` will only be provided for the `error_type` `ASSET_REPORT_ERROR`. `causes` will also not be populated inside an error nested within a `warning` object.")
    status: Optional[float] = Field(default=None, description="The HTTP status code associated with the error. This will only be returned in the response body when the error information is provided via a webhook.")
    documentation_url: Optional[str] = Field(default=None, description="The URL of a Plaid documentation page with more information about the error")
    suggested_action: Optional[str] = Field(default=None, description="Suggested steps for resolving the error")
    item_id: str = Field( description="The `item_id` of the Item associated with this webhook, warning, or error")

Cause.update_forward_refs()
