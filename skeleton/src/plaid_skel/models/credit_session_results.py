# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.credit_session_bank_employment_result import CreditSessionBankEmploymentResult
from plaid_skel.models.credit_session_bank_income_result import CreditSessionBankIncomeResult
from plaid_skel.models.credit_session_document_income_result import CreditSessionDocumentIncomeResult
from plaid_skel.models.credit_session_item_add_result import CreditSessionItemAddResult
from plaid_skel.models.credit_session_payroll_income_result import CreditSessionPayrollIncomeResult




class CreditSessionResults(BaseModel):
    """The set of results for a Link session."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#credit_session_results"
            }
        }

    item_add_results: Optional[List[CreditSessionItemAddResult]] = Field(default=None, description="The set of Item adds for the Link session.")
    bank_income_results: Optional[List[CreditSessionBankIncomeResult]] = Field(default=None, description="The set of bank income verifications for the Link session.")
    bank_employment_results: Optional[List[CreditSessionBankEmploymentResult]] = Field(default=None, description="The set of bank employment verifications for the Link session.")
    payroll_income_results: Optional[List[CreditSessionPayrollIncomeResult]] = Field(default=None, description="The set of payroll income verifications for the Link session.")
    document_income_results: Optional[CreditSessionDocumentIncomeResult] = Field(default=None,)

CreditSessionResults.update_forward_refs()
