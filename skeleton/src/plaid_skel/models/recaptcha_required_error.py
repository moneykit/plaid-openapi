# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class RecaptchaRequiredError(BaseModel):
    """The request was flagged by Plaid's fraud system, and requires additional verification to ensure they are not a bot."""


    error_type: str = Field( description="RECAPTCHA_ERROR")
    error_code: str = Field( description="RECAPTCHA_REQUIRED")
    display_message: str = Field()
    http_code: str = Field( description="400")
    link_user_experience: str = Field( description="Your user will be prompted to solve a Google reCAPTCHA challenge in the Link Recaptcha pane. If they solve the challenge successfully, the user's request is resubmitted and they are directed to the next Item creation step.")
    common_causes: str = Field( description="Plaid's fraud system detects abusive traffic and considers a variety of parameters throughout Item creation requests. When a request is considered risky or possibly fraudulent, Link presents a reCAPTCHA for the user to solve.")
    troubleshooting_steps: str = Field( description="Link will automatically guide your user through reCAPTCHA verification. As a general rule, we recommend instrumenting basic fraud monitoring to detect and protect your website from spam and abuse.  If your user cannot verify their session, please submit a Support ticket with the following identifiers: `link_session_id` or `request_id`")

RecaptchaRequiredError.update_forward_refs()
