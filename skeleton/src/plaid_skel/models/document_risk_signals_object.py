# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.multi_document_risk_signal import MultiDocumentRiskSignal
from plaid_skel.models.single_document_risk_signal import SingleDocumentRiskSignal




class DocumentRiskSignalsObject(BaseModel):
    """Object containing fraud risk data for a set of income documents."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#document_risk_signals_object"
            }
        }

    account_id: Optional[str] = Field(default=None, description="ID of the payroll provider account.")
    single_document_risk_signals: List[SingleDocumentRiskSignal] = Field( description="Array of document metadata and associated risk signals per document")
    multi_document_risk_signals: List[MultiDocumentRiskSignal] = Field( description="Array of risk signals computed from a set of uploaded documents and the associated documents' metadata")

DocumentRiskSignalsObject.update_forward_refs()
