# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.partner_end_customer_o_auth_institution_environments import PartnerEndCustomerOAuthInstitutionEnvironments




class PartnerEndCustomerOAuthInstitution(BaseModel):
    """The OAuth registration information for an institution."""


    name: Optional[str] = Field(default=None,)
    institution_id: Optional[str] = Field(default=None,)
    environments: Optional[PartnerEndCustomerOAuthInstitutionEnvironments] = Field(default=None,)
    production_enablement_date: Optional[str] = Field(default=None, description="The date on which the end customer's application was approved by the institution, or an empty string if their application has not yet been approved.")
    classic_disablement_date: Optional[str] = Field(default=None, description="The date on which non-OAuth Item adds will no longer be supported for this institution, or an empty string if no such date has been set by the institution.")

PartnerEndCustomerOAuthInstitution.update_forward_refs()
