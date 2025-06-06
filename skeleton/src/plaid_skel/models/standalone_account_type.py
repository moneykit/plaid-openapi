# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class StandaloneAccountType(BaseModel):
    """The schema below describes the various `types` and corresponding `subtypes` that Plaid recognizes and reports for financial institution accounts."""


    depository: str = Field( description="An account type holding cash, in which funds are deposited. Supported products for `depository` accounts are: Auth (`checking` and `savings` types only), Balance, Transactions, Identity, Payment Initiation, and Assets.")
    credit: str = Field( description="A credit card type account. Supported products for `credit` accounts are: Balance, Transactions, Identity, and Liabilities.")
    loan: str = Field( description="A loan type account. Supported products for `loan` accounts are: Balance, Liabilities, and Transactions.")
    investment: str = Field( description="An investment account. Supported products for `investment` accounts are: Balance and Investments. In API versions 2018-05-22 and earlier, this type is called `brokerage`.")
    other: str = Field( description="Other or unknown account type. Supported products for `other` accounts are: Balance, Transactions, Identity, and Assets.")

StandaloneAccountType.update_forward_refs()
