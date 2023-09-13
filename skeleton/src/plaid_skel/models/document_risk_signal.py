# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.document_risk_signal_institution_metadata import DocumentRiskSignalInstitutionMetadata




class DocumentRiskSignal(BaseModel):
    """Details about a certain reason as to why a document could potentially be fraudulent."""
    model_config = ConfigDict(json_schema_extra={"nullable": True})

    type: Optional[str] = Field(default=None, description="The result from the risk signal check.")
    field: Optional[str] = Field(default=None, description="The field which the risk signal was computed for")
    has_fraud_risk: Optional[bool] = Field(default=None, description="A flag used to quickly identify if the signal indicates that this field is authentic or fraudulent")
    institution_metadata: Optional[DocumentRiskSignalInstitutionMetadata] = Field(default=None,)
    expected_value: Optional[str] = Field(default=None, description="The expected value of the field, as seen on the document")
    actual_value: Optional[str] = Field(default=None, description="The derived value obtained in the risk signal calculation process for this field")
    signal_description: Optional[str] = Field(default=None, description="A human-readable explanation providing more detail into the particular risk signal")
    page_number: Optional[int] = Field(default=None, description="The relevant page associated with the risk signal")

DocumentRiskSignal.update_forward_refs()
