# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class BankTransferMigrateAccountResponse(BaseModel):
    """Defines the response schema for `/bank_transfer/migrate_account`"""


    access_token: str = Field( description="The Plaid `access_token` for the newly created Item.")
    account_id: str = Field( description="The Plaid `account_id` for the newly created Item.")
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

BankTransferMigrateAccountResponse.update_forward_refs()
