# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.link_delivery_metadata import LinkDeliveryMetadata




class LinkUserDeliveryStatusWebhook(BaseModel):
    """Webhook indicating that the status of the delivery of the hosted link session to a user"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#link_user_delivery_status_webhook"
            }
        }

    webhook_type: str = Field( description="`LINK_DELIVERY`")
    webhook_code: str = Field( description="`DELIVERY_STATUS`")
    link_delivery_session_id: str = Field( description="The ID of the link delivery session.")
    timestamp: str = Field( description="Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format.")
    link_delivery_metadata: LinkDeliveryMetadata = Field()

LinkUserDeliveryStatusWebhook.update_forward_refs()
