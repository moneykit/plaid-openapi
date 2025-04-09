# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.asset_transaction_category_type import AssetTransactionCategoryType
from plaid_skel.models.asset_transaction_type import AssetTransactionType




class AssetTransactionDetail(BaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""


    asset_transaction_unique_identifier: str = Field( description="A vendor created unique Identifier.")
    asset_transaction_amount: float = Field( description="Asset Transaction Amount.")
    asset_transaction_date: date_ = Field( description="Asset Transaction Date.")
    asset_transaction_post_date: date_ = Field( description="Asset Transaction Post Date.")
    asset_transaction_type: AssetTransactionType = Field()
    asset_transaction_paid_by_name: Optional[str] = Field(default=None, description="Populate with who did the transaction.")
    asset_transaction_type_additional_description: Optional[str] = Field(default=None, description="FI Provided - examples are atm, cash, check, credit, debit, deposit, directDebit, directDeposit, dividend, fee, interest, other, payment, pointOfSale, repeatPayment, serviceCharge, transfer.")
    asset_transaction_category_type: Optional[AssetTransactionCategoryType] = Field(default=None,)
    financial_institution_transaction_identifier: Optional[str] = Field(default=None, description="FI provided Transaction Identifier.")

AssetTransactionDetail.update_forward_refs()
