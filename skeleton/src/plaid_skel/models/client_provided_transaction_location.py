# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class ClientProvidedTransactionLocation(BaseModel):
    """A representation of where a transaction took place.  Use this field to pass in structured location information you may have about your transactions. Providing location data is optional but can increase result quality. If you have unstructured location information, it may be appended to the `description` field."""


    country: Optional[str] = Field(default=None, description="The country where the transaction occurred.")
    region: Optional[str] = Field(default=None, description="The region or state where the transaction occurred.")
    city: Optional[str] = Field(default=None, description="The city where the transaction occurred.")
    address: Optional[str] = Field(default=None, description="The street address where the transaction occurred.")
    postal_code: Optional[str] = Field(default=None, description="The postal code where the transaction occurred.")

ClientProvidedTransactionLocation.update_forward_refs()
