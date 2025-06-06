# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.partner_end_customer_o_auth_institution_application_status import PartnerEndCustomerOAuthInstitutionApplicationStatus




class PartnerEndCustomerOAuthInstitutionEnvironments(BaseModel):
    """Registration statuses by environment."""


    development: Optional[PartnerEndCustomerOAuthInstitutionApplicationStatus] = Field(default=None,)
    production: Optional[PartnerEndCustomerOAuthInstitutionApplicationStatus] = Field(default=None,)

PartnerEndCustomerOAuthInstitutionEnvironments.update_forward_refs()
