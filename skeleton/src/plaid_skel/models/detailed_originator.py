# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.transfer_diligence_status import TransferDiligenceStatus




class DetailedOriginator(BaseModel):
    """Originator and their status."""


    client_id: str = Field( description="Originator’s client ID.")
    transfer_diligence_status: TransferDiligenceStatus = Field()
    company_name: str = Field()

DetailedOriginator.update_forward_refs()
