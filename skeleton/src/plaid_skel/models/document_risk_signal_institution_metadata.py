# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class DocumentRiskSignalInstitutionMetadata(BaseModel):
    """An object which contains additional metadata about the institution used to compute the verification attribute"""
    model_config = ConfigDict(json_schema_extra={"nullable": True})

    item_id: str = Field( description="The `item_id` of the Item associated with this webhook, warning, or error")

DocumentRiskSignalInstitutionMetadata.update_forward_refs()
