# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.fdx_party_registry import FDXPartyRegistry
from plaid_skel.models.fdx_party_type import FDXPartyType




class FDXParty(BaseModel):
    """FDX Participant - an entity or person that is a part of a FDX API transaction"""


    name: str = Field( description="Human recognizable common name")
    type: FDXPartyType = Field()
    home_uri: Optional[AnyUrl] = Field(default=None, description="URI for party, where an end user could learn more about the company or application involved in the data sharing chain")
    logo_uri: Optional[AnyUrl] = Field(default=None, description="URI for a logo asset to be displayed to the end user")
    registry: Optional[FDXPartyRegistry] = Field(default=None,)
    registered_entity_name: Optional[str] = Field(default=None, description="Registered name of party")
    registered_entity_id: Optional[str] = Field(default=None, description="Registered id of party")

FDXParty.update_forward_refs()
