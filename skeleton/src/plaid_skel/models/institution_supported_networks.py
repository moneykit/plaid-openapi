# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.transfer_capabilities_get_rtp import TransferCapabilitiesGetRTP




class InstitutionSupportedNetworks(BaseModel):
    """Contains the RTP network and types supported by the linked Item's institution."""


    rtp: TransferCapabilitiesGetRTP = Field()

InstitutionSupportedNetworks.update_forward_refs()
