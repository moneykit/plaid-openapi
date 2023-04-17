# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.document_risk_signal import DocumentRiskSignal
from plaid_skel.models.document_risk_summary import DocumentRiskSummary
from plaid_skel.models.risk_signal_document_reference import RiskSignalDocumentReference




class SingleDocumentRiskSignal(BaseModel):
    """Object containing all risk signals and relevant metadata for a single document"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#single_document_risk_signal"
            }
        }

    document_reference: RiskSignalDocumentReference = Field()
    risk_signals: List[DocumentRiskSignal] = Field( description="Array of attributes that indicate whether or not there is fraud risk with a document")
    risk_summary: DocumentRiskSummary = Field()

SingleDocumentRiskSignal.update_forward_refs()
