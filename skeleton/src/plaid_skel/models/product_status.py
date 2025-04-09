# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.product_status_breakdown import ProductStatusBreakdown




class ProductStatus(BaseModel):
    """A representation of the status health of a request type. Auth requests, Balance requests, Identity requests, Investments requests, Liabilities requests, Transactions updates, Investments updates, Liabilities updates, and Item logins each have their own status object."""
    model_config = ConfigDict(json_schema_extra={"nullable": True})

    status: str = Field( description="This field is deprecated in favor of the `breakdown` object, which provides more granular institution health data.  `HEALTHY`: the majority of requests are successful `DEGRADED`: only some requests are successful `DOWN`: all requests are failing")
    last_status_change: datetime = Field( description="[ISO 8601](https://wikipedia.org/wiki/ISO_8601) formatted timestamp of the last status change for the institution. ")
    breakdown: ProductStatusBreakdown = Field()

ProductStatus.update_forward_refs()
