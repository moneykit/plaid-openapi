# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.health_incident import HealthIncident
from plaid_skel.models.product_status import ProductStatus




class InstitutionStatus(BaseModel):
    """The status of an institution is determined by the health of its Item logins, Transactions updates, Investments updates, Liabilities updates, Auth requests, Balance requests, Identity requests, Investments requests, and Liabilities requests. A login attempt is conducted during the initial Item add in Link. If there is not enough traffic to accurately calculate an institution's status, Plaid will return null rather than potentially inaccurate data.  Institution status is accessible in the Dashboard and via the API using the `/institutions/get_by_id` endpoint with the `include_status` option set to true. Note that institution status is not available in the Sandbox environment. """
    model_config = ConfigDict(json_schema_extra={"nullable": True})

    item_logins: Optional[ProductStatus] = Field(default=None,)
    transactions_updates: Optional[ProductStatus] = Field(default=None,)
    auth: Optional[ProductStatus] = Field(default=None,)
    identity: Optional[ProductStatus] = Field(default=None,)
    investments_updates: Optional[ProductStatus] = Field(default=None,)
    liabilities_updates: Optional[ProductStatus] = Field(default=None,)
    liabilities: Optional[ProductStatus] = Field(default=None,)
    investments: Optional[ProductStatus] = Field(default=None,)
    health_incidents: Optional[List[HealthIncident]] = Field(default=None, description="Details of recent health incidents associated with the institution.")

InstitutionStatus.update_forward_refs()
