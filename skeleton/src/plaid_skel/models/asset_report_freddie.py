# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.loans import Loans
from plaid_skel.models.parties import Parties
from plaid_skel.models.services import Services




class AssetReportFreddie(BaseModel):
    """An object representing an Asset Report with Freddie Mac schema."""


    loans: Loans = Field()
    parties: Parties = Field()
    services: Services = Field()

AssetReportFreddie.update_forward_refs()
