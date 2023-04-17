# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.products import Products




class InstitutionsGetRequestOptions(BaseModel):
    """An optional object to filter `/institutions/get` results."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#institutions_get_request_options"
            }
        }

    products: Optional[List[Products]] = Field(default=None, description="Filter the Institutions based on which products they support. ")
    routing_numbers: Optional[List[str]] = Field(default=None, description="Specify an array of routing numbers to filter institutions. The response will only return institutions that match all of the routing numbers in the array. Routing number records used for this matching are not comprehensive; failure to match a given routing number to an institution does not mean that the institution is unsupported by Plaid.")
    oauth: Optional[bool] = Field(default=None, description="Limit results to institutions with or without mandatory OAuth login flows. Note that institutions will only have `oauth` set to `true` if *all* Items associated with that institution are required to use OAuth flows; institutions in a state of migration to OAuth may have the `oauth` attribute set to `false` even if they support OAuth.")
    include_optional_metadata: Optional[bool] = Field(default=None, description="When `true`, return the institution's homepage URL, logo and primary brand color.  Note that Plaid does not own any of the logos shared by the API, and that by accessing or using these logos, you agree that you are doing so at your own risk and will, if necessary, obtain all required permissions from the appropriate rights holders and adhere to any applicable usage guidelines. Plaid disclaims all express or implied warranties with respect to the logos.")
    include_auth_metadata: Optional[bool] = Field(default=None, description="When `true`, returns metadata related to the Auth product indicating which auth methods are supported.")
    include_payment_initiation_metadata: Optional[bool] = Field(default=None, description="When `true`, returns metadata related to the Payment Initiation product indicating which payment configurations are supported.")

InstitutionsGetRequestOptions.update_forward_refs()
