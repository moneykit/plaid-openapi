# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.link_delivery_delivery_method import LinkDeliveryDeliveryMethod




class LinkDeliveryCommunicationMethod(BaseModel):
    """The communication method containing both the type and address to send the URL."""


    method: Optional[LinkDeliveryDeliveryMethod] = Field(default=None,)
    address: Optional[str] = Field(default=None, description="The phone number / email address that link delivery sessions are delivered to. Phone numbers must be in E.164 format.")

LinkDeliveryCommunicationMethod.update_forward_refs()
