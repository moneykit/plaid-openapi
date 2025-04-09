# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.document_authenticity_match_code import DocumentAuthenticityMatchCode
from plaid_skel.models.image_quality import ImageQuality
from plaid_skel.models.physical_document_extracted_data_analysis import PhysicalDocumentExtractedDataAnalysis




class DocumentAnalysis(BaseModel):
    """High level descriptions of how the associated document was processed. If a document fails verification, the details in the `analysis` object should help clarify why the document was rejected."""


    authenticity: DocumentAuthenticityMatchCode = Field()
    image_quality: ImageQuality = Field()
    extracted_data: Optional[PhysicalDocumentExtractedDataAnalysis] = Field(default=None,)

DocumentAnalysis.update_forward_refs()
