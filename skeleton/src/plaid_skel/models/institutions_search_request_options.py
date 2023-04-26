# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.institutions_search_payment_initiation_options import InstitutionsSearchPaymentInitiationOptions




class InstitutionsSearchRequestOptions(BaseModel):
    """An optional object to filter `/institutions/search` results."""


    oauth: Optional[bool] = Field(default=None, description="Limit results to institutions with or without mandatory OAuth login flows. Note that institutions will only have `oauth` set to `true` if *all* Items associated with that institution are required to use OAuth flows; institutions in a state of migration to OAuth may have the `oauth` attribute set to `false` even if they support OAuth.")
    include_optional_metadata: Optional[bool] = Field(default=None, description="When true, return the institution's homepage URL, logo and primary brand color.")
    include_auth_metadata: Optional[bool] = Field(default=None, description="When `true`, returns metadata related to the Auth product indicating which auth methods are supported.")
    include_payment_initiation_metadata: Optional[bool] = Field(default=None, description="When `true`, returns metadata related to the Payment Initiation product indicating which payment configurations are supported.")
    payment_initiation: Optional[InstitutionsSearchPaymentInitiationOptions] = Field(default=None,)

InstitutionsSearchRequestOptions.update_forward_refs()
