# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.credit1099_filer import Credit1099Filer
from plaid_skel.models.credit1099_payer import Credit1099Payer
from plaid_skel.models.credit1099_recipient import Credit1099Recipient
from plaid_skel.models.credit_document_metadata import CreditDocumentMetadata
from plaid_skel.models.form1099_type import Form1099Type




class Credit1099(BaseModel):
    """An object representing an end user's 1099 tax form"""


    document_id: Optional[str] = Field(default=None, description="An identifier of the document referenced by the document metadata.")
    document_metadata: Optional[CreditDocumentMetadata] = Field(default=None,)
    form_1099_type: Optional[Form1099Type] = Field(default=None,)
    recipient: Optional[Credit1099Recipient] = Field(default=None,)
    payer: Optional[Credit1099Payer] = Field(default=None,)
    filer: Optional[Credit1099Filer] = Field(default=None,)
    tax_year: Optional[str] = Field(default=None, description="Tax year of the tax form.")
    rents: Optional[float] = Field(default=None, description="Amount in rent by payer.")
    royalties: Optional[float] = Field(default=None, description="Amount in royalties by payer.")
    other_income: Optional[float] = Field(default=None, description="Amount in other income by payer.")
    federal_income_tax_withheld: Optional[float] = Field(default=None, description="Amount of federal income tax withheld from payer.")
    fishing_boat_proceeds: Optional[float] = Field(default=None, description="Amount of fishing boat proceeds from payer.")
    medical_and_healthcare_payments: Optional[float] = Field(default=None, description="Amount of medical and healthcare payments from payer.")
    nonemployee_compensation: Optional[float] = Field(default=None, description="Amount of nonemployee compensation from payer.")
    substitute_payments_in_lieu_of_dividends_or_interest: Optional[float] = Field(default=None, description="Amount of substitute payments made by payer.")
    payer_made_direct_sales_of_5000_or_more_of_consumer_products_to_buyer: Optional[str] = Field(default=None, description="Whether or not payer made direct sales over $5000 of consumer products.")
    crop_insurance_proceeds: Optional[float] = Field(default=None, description="Amount of crop insurance proceeds.")
    excess_golden_parachute_payments: Optional[float] = Field(default=None, description="Amount of golden parachute payments made by payer.")
    gross_proceeds_paid_to_an_attorney: Optional[float] = Field(default=None, description="Amount of gross proceeds paid to an attorney by payer.")
    section_409a_deferrals: Optional[float] = Field(default=None, description="Amount of 409A deferrals earned by payer.")
    section_409a_income: Optional[float] = Field(default=None, description="Amount of 409A income earned by payer.")
    state_tax_withheld: Optional[float] = Field(default=None, description="Amount of state tax withheld of payer for primary state.")
    state_tax_withheld_lower: Optional[float] = Field(default=None, description="Amount of state tax withheld of payer for secondary state.")
    payer_state_number: Optional[str] = Field(default=None, description="Primary state ID.")
    payer_state_number_lower: Optional[str] = Field(default=None, description="Secondary state ID.")
    state_income: Optional[float] = Field(default=None, description="State income reported for primary state.")
    state_income_lower: Optional[float] = Field(default=None, description="State income reported for secondary state.")
    transactions_reported: Optional[str] = Field(default=None, description="One of the values will be provided Payment card Third party network")
    pse_name: Optional[str] = Field(default=None, description="Name of the PSE (Payment Settlement Entity).")
    pse_telephone_number: Optional[str] = Field(default=None, description="Formatted (XXX) XXX-XXXX. Phone number of the PSE (Payment Settlement Entity).")
    gross_amount: Optional[float] = Field(default=None, description="Gross amount reported.")
    card_not_present_transaction: Optional[float] = Field(default=None, description="Amount in card not present transactions.")
    merchant_category_code: Optional[str] = Field(default=None, description="Merchant category of filer.")
    number_of_payment_transactions: Optional[str] = Field(default=None, description="Number of payment transactions made.")
    january_amount: Optional[float] = Field(default=None, description="Amount reported for January.")
    february_amount: Optional[float] = Field(default=None, description="Amount reported for February.")
    march_amount: Optional[float] = Field(default=None, description="Amount reported for March.")
    april_amount: Optional[float] = Field(default=None, description="Amount reported for April.")
    may_amount: Optional[float] = Field(default=None, description="Amount reported for May.")
    june_amount: Optional[float] = Field(default=None, description="Amount reported for June.")
    july_amount: Optional[float] = Field(default=None, description="Amount reported for July.")
    august_amount: Optional[float] = Field(default=None, description="Amount reported for August.")
    september_amount: Optional[float] = Field(default=None, description="Amount reported for September.")
    october_amount: Optional[float] = Field(default=None, description="Amount reported for October.")
    november_amount: Optional[float] = Field(default=None, description="Amount reported for November.")
    december_amount: Optional[float] = Field(default=None, description="Amount reported for December.")
    primary_state: Optional[str] = Field(default=None, description="Primary state of business.")
    secondary_state: Optional[str] = Field(default=None, description="Secondary state of business.")
    primary_state_id: Optional[str] = Field(default=None, description="Primary state ID.")
    secondary_state_id: Optional[str] = Field(default=None, description="Secondary state ID.")
    primary_state_income_tax: Optional[float] = Field(default=None, description="State income tax reported for primary state.")
    secondary_state_income_tax: Optional[float] = Field(default=None, description="State income tax reported for secondary state.")

Credit1099.update_forward_refs()
