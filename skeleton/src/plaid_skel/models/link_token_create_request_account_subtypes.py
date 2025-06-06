# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.link_token_create_credit_filter import LinkTokenCreateCreditFilter
from plaid_skel.models.link_token_create_depository_filter import LinkTokenCreateDepositoryFilter
from plaid_skel.models.link_token_create_investment_filter import LinkTokenCreateInvestmentFilter
from plaid_skel.models.link_token_create_loan_filter import LinkTokenCreateLoanFilter




class LinkTokenCreateRequestAccountSubtypes(BaseModel):
    """By default, Link will only display account types that are compatible with all products supplied in the `products` parameter of `/link/token/create`. You can further limit the accounts shown in Link by using `account_filters` to specify the account subtypes to be shown in Link. Only the specified subtypes will be shown. This filtering applies to both the Account Select view (if enabled) and the Institution Select view. Institutions that do not support the selected subtypes will be omitted from Link. To indicate that all subtypes should be shown, use the value `\"all\"`. If the `account_filters` filter is used, any account type for which a filter is not specified will be entirely omitted from Link.  For a full list of valid types and subtypes, see the [Account schema](https://plaid.com/docs/api/accounts#account-type-schema).  For institutions using OAuth, the filter will not affect the list of institutions or accounts shown by the bank in the OAuth window. """


    depository: Optional[LinkTokenCreateDepositoryFilter] = Field(default=None,)
    credit: Optional[LinkTokenCreateCreditFilter] = Field(default=None,)
    loan: Optional[LinkTokenCreateLoanFilter] = Field(default=None,)
    investment: Optional[LinkTokenCreateInvestmentFilter] = Field(default=None,)

LinkTokenCreateRequestAccountSubtypes.update_forward_refs()
