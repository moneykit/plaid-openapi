# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.credit_filter import CreditFilter
from plaid_skel.models.depository_filter import DepositoryFilter
from plaid_skel.models.investment_filter import InvestmentFilter
from plaid_skel.models.loan_filter import LoanFilter




class LinkTokenAccountFilters(BaseModel):
    """By default, Link will provide limited account filtering: it will only display Institutions that are compatible with all products supplied in the `products` parameter of `/link/token/create`, and, if `auth` is specified in the `products` array, will also filter out accounts other than `checking` and `savings` accounts on the Account Select pane. You can further limit the accounts shown in Link by using `account_filters` to specify the account subtypes to be shown in Link. Only the specified subtypes will be shown. This filtering applies to both the Account Select view (if enabled) and the Institution Select view. Institutions that do not support the selected subtypes will be omitted from Link. To indicate that all subtypes should be shown, use the value `\"all\"`. If the `account_filters` filter is used, any account type for which a filter is not specified will be entirely omitted from Link. For a full list of valid types and subtypes, see the [Account schema](https://plaid.com/docs/api/accounts#account-type-schema).  For institutions using OAuth, the filter will not affect the list of accounts shown by the bank in the OAuth window. """


    depository: Optional[DepositoryFilter] = Field(default=None,)
    credit: Optional[CreditFilter] = Field(default=None,)
    loan: Optional[LoanFilter] = Field(default=None,)
    investment: Optional[InvestmentFilter] = Field(default=None,)

LinkTokenAccountFilters.update_forward_refs()
