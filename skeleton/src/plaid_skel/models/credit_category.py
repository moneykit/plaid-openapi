# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class CreditCategory(BaseModel):
    """Information describing the intent of the transaction. Most relevant for credit use cases, but not limited to such use cases. Please reach out to your account manager or sales representative if you would like to receive this field.  See the [`taxonomy csv file`](https://plaid.com/documents/credit-category-taxonomy.csv) for a full list of credit categories."""
    model_config = ConfigDict(json_schema_extra={"nullable": True})

    primary: str = Field( description="A high level category that communicates the broad category of the transaction.")
    detailed: str = Field( description="A granular category conveying the transaction's intent. This field can also be used as a unique identifier for the category.")

CreditCategory.update_forward_refs()
