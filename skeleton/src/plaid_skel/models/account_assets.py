# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.account_balance import AccountBalance
from plaid_skel.models.account_subtype import AccountSubtype
from plaid_skel.models.account_type import AccountType
from plaid_skel.models.asset_report_transaction import AssetReportTransaction
from plaid_skel.models.historical_balance import HistoricalBalance
from plaid_skel.models.owner import Owner
from plaid_skel.models.ownership_type import OwnershipType




class AccountAssets(BaseModel):
    """Asset information about an account"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#account_assets"
            }
        }

    account_id: str = Field( description="Plaid’s unique identifier for the account. This value will not change unless Plaid can't reconcile the account with the data returned by the financial institution. This may occur, for example, when the name of the account changes. If this happens a new `account_id` will be assigned to the account.  The `account_id` can also change if the `access_token` is deleted and the same credentials that were used to generate that `access_token` are used to generate a new `access_token` on a later date. In that case, the new `account_id` will be different from the old `account_id`.  If an account with a specific `account_id` disappears instead of changing, the account is likely closed. Closed accounts are not returned by the Plaid API.  Like all Plaid identifiers, the `account_id` is case sensitive.")
    balances: AccountBalance = Field()
    mask: Optional[str] = Field(default=None, description="The last 2-4 alphanumeric characters of an account's official account number. Note that the mask may be non-unique between an Item's accounts, and it may also not match the mask that the bank displays to the user.")
    name: str = Field( description="The name of the account, either assigned by the user or by the financial institution itself")
    official_name: Optional[str] = Field(default=None, description="The official name of the account as given by the financial institution")
    type: AccountType = Field()
    subtype: Optional[AccountSubtype] = Field(default=None,)
    verification_status: Optional[str] = Field(default=None, description="The current verification status of an Auth Item initiated through Automated or Manual micro-deposits.  Returned for Auth Items only.  `pending_automatic_verification`: The Item is pending automatic verification  `pending_manual_verification`: The Item is pending manual micro-deposit verification. Items remain in this state until the user successfully verifies the two amounts.  `automatically_verified`: The Item has successfully been automatically verified   `manually_verified`: The Item has successfully been manually verified  `verification_expired`: Plaid was unable to automatically verify the deposit within 7 calendar days and will no longer attempt to validate the Item. Users may retry by submitting their information again through Link.  `verification_failed`: The Item failed manual micro-deposit verification because the user exhausted all 3 verification attempts. Users may retry by submitting their information again through Link.   ")
    persistent_account_id: Optional[str] = Field(default=None, description="A unique and persistent identifier for accounts that can be used to trace multiple instances of the same account across different Items for depository accounts. This is currently an opt-in field and only supported for Chase Items.")
    days_available: float = Field( description="The duration of transaction history available for this Item, typically defined as the time since the date of the earliest transaction in that account. Only returned by Assets endpoints.")
    transactions: List[AssetReportTransaction] = Field( description="Transaction history associated with the account. Only returned by Assets endpoints. Transaction history returned by endpoints such as `/transactions/get` or `/investments/transactions/get` will be returned in the top-level `transactions` field instead.")
    owners: List[Owner] = Field( description="Data returned by the financial institution about the account owner or owners. Only returned by Identity or Assets endpoints. For business accounts, the name reported may be either the name of the individual or the name of the business, depending on the institution. Multiple owners on a single account will be represented in the same `owner` object, not in multiple owner objects within the array. In API versions 2018-05-22 and earlier, the `owners` object is not returned, and instead identity information is returned in the top level `identity` object. For more details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2019-05-29)")
    ownership_type: Optional[OwnershipType] = Field(default=None,)
    historical_balances: List[HistoricalBalance] = Field( description="Calculated data about the historical balances on the account. Only returned by Assets endpoints and currently not supported by `brokerage` or `investment` accounts.")

AccountAssets.update_forward_refs()
