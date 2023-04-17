# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.document_risk_signal import DocumentRiskSignal
from plaid_skel.models.risk_signal_document_reference import RiskSignalDocumentReference




class MultiDocumentRiskSignal(BaseModel):
    """Object containing risk signals and relevant metadata for a set of uploaded documents"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#multi_document_risk_signal"
            }
        }

    document_references: List[RiskSignalDocumentReference] = Field( description="Array of objects containing attributes that could indicate if a document is fraudulent")
    risk_signals: List[DocumentRiskSignal] = Field( description="Array of attributes that indicate whether or not there is fraud risk with a set of documents")

MultiDocumentRiskSignal.update_forward_refs()
