# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.link_delivery_account import LinkDeliveryAccount
from plaid_skel.models.link_delivery_institution import LinkDeliveryInstitution
from plaid_skel.models.link_delivery_webhook_callback_type import LinkDeliveryWebhookCallbackType
from plaid_skel.models.link_event_name import LinkEventName




class LinkCallbackMetadata(BaseModel):
    """Information related to the callback from the hosted Link session."""


    callback_type: Optional[LinkDeliveryWebhookCallbackType] = Field(default=None,)
    event_name: Optional[LinkEventName] = Field(default=None,)
    status: Optional[str] = Field(default=None, description="Indicates where in the flow the Link user exited")
    link_session_id: Optional[str] = Field(default=None, description="A unique identifier associated with a user's actions and events through the Link flow. Include this identifier when opening a support ticket for faster turnaround.")
    request_id: Optional[str] = Field(default=None, description="The request ID for the last request made by Link. This can be shared with Plaid Support to expedite investigation.")
    institution: Optional[LinkDeliveryInstitution] = Field(default=None,)
    accounts: Optional[List[LinkDeliveryAccount]] = Field(default=None, description="A list of accounts attached to the connected Item. If Account Select is enabled via the developer dashboard, accounts will only include selected accounts.")

LinkCallbackMetadata.update_forward_refs()
