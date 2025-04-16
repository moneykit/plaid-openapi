# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.webhook_environment_values import WebhookEnvironmentValues




class ScreeningStatusUpdatedWebhook(BaseModel):
    """Fired when an individual screening status has changed, which can occur manually via the dashboard or during ongoing monitoring."""


    webhook_type: str = Field( description="`SCREENING`")
    webhook_code: str = Field( description="`STATUS_UPDATED`")
    screening_id: str = Field( description="The ID of the associated screening.")
    environment: WebhookEnvironmentValues = Field()

ScreeningStatusUpdatedWebhook.update_forward_refs()
