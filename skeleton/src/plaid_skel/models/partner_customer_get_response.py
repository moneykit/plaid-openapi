# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.partner_end_customer import PartnerEndCustomer




class PartnerCustomerGetResponse(BaseModel):
    """Response schema for `/partner/customer/get`."""


    end_customer: Optional[PartnerEndCustomer] = Field(default=None,)
    request_id: Optional[str] = Field(default=None, description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

PartnerCustomerGetResponse.update_forward_refs()
