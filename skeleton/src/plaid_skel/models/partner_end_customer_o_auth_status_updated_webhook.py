# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.partner_end_customer_o_auth_status_updated_values import PartnerEndCustomerOAuthStatusUpdatedValues
from plaid_skel.models.webhook_environment_values import WebhookEnvironmentValues




class PartnerEndCustomerOAuthStatusUpdatedWebhook(BaseModel):
    """The webhook of type `PARTNER` and code `END_CUSTOMER_OAUTH_STATUS_UPDATED` will be fired when a partner's end customer has an update on their OAuth registration status with an institution."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#partner_end_customer_o_auth_status_updated_webhook"
            }
        }

    webhook_type: str = Field( description="`PARTNER`")
    webhook_code: str = Field( description="`END_CUSTOMER_OAUTH_STATUS_UPDATED`")
    end_customer_client_id: str = Field( description="The client ID of the end customer")
    environment: WebhookEnvironmentValues = Field()
    institution_id: str = Field( description="The institution ID")
    institution_name: str = Field( description="The institution name")
    status: PartnerEndCustomerOAuthStatusUpdatedValues = Field()

PartnerEndCustomerOAuthStatusUpdatedWebhook.update_forward_refs()
