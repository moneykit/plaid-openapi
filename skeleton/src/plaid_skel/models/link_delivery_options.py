# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.link_delivery_recipient import LinkDeliveryRecipient




class LinkDeliveryOptions(BaseModel):
    """Optional metadata related to the link delivery session"""


    recipient: Optional[LinkDeliveryRecipient] = Field(default=None,)

LinkDeliveryOptions.update_forward_refs()
