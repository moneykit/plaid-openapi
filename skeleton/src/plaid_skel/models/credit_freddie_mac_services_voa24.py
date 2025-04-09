# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.credit_freddie_mac_service_voa24 import CreditFreddieMacServiceVOA24




class CreditFreddieMacServicesVOA24(BaseModel):
    """A collection of objects that describe requests and responses for services."""


    service: CreditFreddieMacServiceVOA24 = Field()

CreditFreddieMacServicesVOA24.update_forward_refs()
