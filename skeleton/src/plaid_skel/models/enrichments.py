# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.counterparty import Counterparty
from plaid_skel.models.personal_finance_category import PersonalFinanceCategory
from plaid_skel.models.recurrence import Recurrence




class Enrichments(BaseModel):
    """A grouping of the Plaid produced transaction enrichment fields."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#enrichments"
            }
        }

    check_number: Optional[str] = Field(default=None, description="The check number of the transaction. This field is only populated for check transactions.")
    counterparties: List[Counterparty] = Field( description="The counterparties present in the transaction. Counterparties, such as the merchant or the financial institution, are extracted by Plaid from the raw description.")
    entity_id: Optional[str] = Field(default=None, description="A unique, stable, Plaid-generated id that maps to the primary counterparty.")
    legacy_category_id: Optional[str] = Field(default=None, description="The ID of the legacy category to which this transaction belongs. For a full list of legacy categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget).  We recommend using the `personal_finance_category` for transaction categorization to obtain the best results.")
    legacy_category: Optional[List[str]] = Field(default=None, description="A hierarchical array of the legacy categories to which this transaction belongs. For a full list of legacy categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget).  We recommend using the `personal_finance_category` for transaction categorization to obtain the best results.")
    logo_url: Optional[str] = Field(default=None, description="The URL of a logo associated with this transaction, if available. The logo is formatted as a 100x100 pixel PNG file.")
    merchant_name: Optional[str] = Field(default=None, description="The name of the primary counterparty, such as the merchant or the financial institution, as extracted by Plaid from the raw description.")
    personal_finance_category: Optional[PersonalFinanceCategory] = Field(default=None,)
    personal_finance_category_icon_url: str = Field( description="A link to the icon associated with the primary personal finance category. The logo will always be 100x100 pixels.")
    recurrence: Optional[Recurrence] = Field(default=None,)
    website: Optional[str] = Field(default=None, description="The website associated with this transaction.")

Enrichments.update_forward_refs()
