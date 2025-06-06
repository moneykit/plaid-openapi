# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class LinkDeliveryCreateResponse(BaseModel):
    """LinkDeliveryCreateResponse defines the response schema for `/link_delivery/create`"""


    link_delivery_url: str = Field( description="The URL to the Link Delivery session, which will be delivered by the specified delivery method.")
    link_delivery_session_id: str = Field( description="The ID for the Link Delivery session. Same as the `link_token` string excluding the \"link-{env}-\" prefix.")
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

LinkDeliveryCreateResponse.update_forward_refs()
