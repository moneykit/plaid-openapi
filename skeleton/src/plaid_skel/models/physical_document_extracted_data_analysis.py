# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.document_date_of_birth_match_code import DocumentDateOfBirthMatchCode
from plaid_skel.models.document_name_match_code import DocumentNameMatchCode
from plaid_skel.models.expiration_date import ExpirationDate
from plaid_skel.models.issuing_country import IssuingCountry




class PhysicalDocumentExtractedDataAnalysis(BaseModel):
    """Analysis of the data extracted from the submitted document."""

    class Config:
        schema_extra = {"nullable": True}

    name: DocumentNameMatchCode = Field()
    date_of_birth: DocumentDateOfBirthMatchCode = Field()
    expiration_date: ExpirationDate = Field()
    issuing_country: IssuingCountry = Field()

PhysicalDocumentExtractedDataAnalysis.update_forward_refs()
