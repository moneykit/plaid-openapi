# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.income_verification_source_type import IncomeVerificationSourceType
from plaid_skel.models.link_token_create_request_income_verification_bank_income import LinkTokenCreateRequestIncomeVerificationBankIncome
from plaid_skel.models.link_token_create_request_income_verification_payroll_income import LinkTokenCreateRequestIncomeVerificationPayrollIncome
from plaid_skel.models.link_token_create_request_user_stated_income_source import LinkTokenCreateRequestUserStatedIncomeSource




class LinkTokenCreateRequestIncomeVerification(BaseModel):
    """Specifies options for initializing Link for use with the Income product. This field is required if `income_verification` is included in the `products` array."""


    income_verification_id: Optional[str] = Field(default=None, description="The `income_verification_id` of the verification instance, as provided by `/income/verification/create`.")
    asset_report_id: Optional[str] = Field(default=None, description="The `asset_report_id` of an asset report associated with the user, as provided by `/asset_report/create`. Providing an `asset_report_id` is optional and can be used to verify the user through a streamlined flow. If provided, the bank linking flow will be skipped.")
    precheck_id: Optional[str] = Field(default=None, description="The ID of a precheck created with `/income/verification/precheck`. Will be used to improve conversion of the income verification flow by streamlining the Link interface presented to the end user.")
    access_tokens: Optional[List[str]] = Field(default=None, description="An array of access tokens corresponding to Items that a user has previously connected with. Data from these institutions will be cross-referenced with document data received during the Document Income flow to help verify that the uploaded documents are accurate. If the `transactions` product was not initialized for these Items during link, it will be initialized after this Link session.  This field should only be used with the `payroll` income source type.")
    income_source_types: Optional[List[IncomeVerificationSourceType]] = Field(default=None, description="The types of source income data that users will be permitted to share. Options include `bank` and `payroll`. Currently you can only specify one of these options.")
    bank_income: Optional[LinkTokenCreateRequestIncomeVerificationBankIncome] = Field(default=None,)
    payroll_income: Optional[LinkTokenCreateRequestIncomeVerificationPayrollIncome] = Field(default=None,)
    stated_income_sources: Optional[List[LinkTokenCreateRequestUserStatedIncomeSource]] = Field(default=None, description="A list of user stated income sources")

LinkTokenCreateRequestIncomeVerification.update_forward_refs()
