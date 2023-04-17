# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class DepositSwitchGetResponse(BaseModel):
    """DepositSwitchGetResponse defines the response schema for `/deposit_switch/get`"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#deposit_switch_get_response"
            }
        }

    deposit_switch_id: str = Field( description="The ID of the deposit switch.")
    target_account_id: Optional[str] = Field(default=None, description="The ID of the bank account the direct deposit was switched to.")
    target_item_id: Optional[str] = Field(default=None, description="The ID of the Item the direct deposit was switched to.")
    state: str = Field( description=" The state, or status, of the deposit switch.  - `initialized` – The deposit switch has been initialized with the user entering the information required to submit the deposit switch request.  - `processing` – The deposit switch request has been submitted and is being processed.  - `completed` – The user's employer has fulfilled the deposit switch request.  - `error` – There was an error processing the deposit switch request.")
    switch_method: Optional[str] = Field(default=None, description="The method used to make the deposit switch.  - `instant` – User instantly switched their direct deposit to a new or existing bank account by connecting their payroll or employer account.  - `mail` – User requested that Plaid contact their employer by mail to make the direct deposit switch.  - `pdf` – User generated a PDF or email to be sent to their employer with the information necessary to make the deposit switch.'")
    account_has_multiple_allocations: Optional[bool] = Field(default=None, description="When `true`, user’s direct deposit goes to multiple banks. When false, user’s direct deposit only goes to the target account. Always `null` if the deposit switch has not been completed.")
    is_allocated_remainder: Optional[bool] = Field(default=None, description="When `true`, the target account is allocated the remainder of direct deposit after all other allocations have been deducted. When `false`, user’s direct deposit is allocated as a percent or amount. Always `null` if the deposit switch has not been completed.")
    percent_allocated: Optional[float] = Field(default=None, description="The percentage of direct deposit allocated to the target account. Always `null` if the target account is not allocated a percentage or if the deposit switch has not been completed or if `is_allocated_remainder` is true.")
    amount_allocated: Optional[float] = Field(default=None, description="The dollar amount of direct deposit allocated to the target account. Always `null` if the target account is not allocated an amount or if the deposit switch has not been completed.")
    employer_name: Optional[str] = Field(default=None, description="The name of the employer selected by the user. If the user did not select an employer, the value returned is `null`.")
    employer_id: Optional[str] = Field(default=None, description="The ID of the employer selected by the user. If the user did not select an employer, the value returned is `null`.")
    institution_name: Optional[str] = Field(default=None, description="The name of the institution selected by the user. If the user did not select an institution, the value returned is `null`.")
    institution_id: Optional[str] = Field(default=None, description="The ID of the institution selected by the user. If the user did not select an institution, the value returned is `null`.")
    date_created: date = Field( description="[ISO 8601](https://wikipedia.org/wiki/ISO_8601) date the deposit switch was created. ")
    date_completed: Optional[date] = Field(default=None, description="[ISO 8601](https://wikipedia.org/wiki/ISO_8601) date the deposit switch was completed. Always `null` if the deposit switch has not been completed. ")
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

DepositSwitchGetResponse.update_forward_refs()
