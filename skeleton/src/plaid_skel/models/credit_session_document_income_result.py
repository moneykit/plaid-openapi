# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class CreditSessionDocumentIncomeResult(BaseModel):
    """The details of a document income verification in Link"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#credit_session_document_income_result"
            }
        }

    num_paystubs_uploaded: int = Field( description="The number of paystubs uploaded by the user.")
    num_w2s_uploaded: int = Field( description="The number of w2s uploaded by the user.")

CreditSessionDocumentIncomeResult.update_forward_refs()
