# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.reporting_information import ReportingInformation
from plaid_skel.models.service_product_fulfillment import ServiceProductFulfillment
from plaid_skel.models.verification_of_asset_response import VerificationOfAssetResponse




class VerificationOfAsset(BaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#verification_of_asset"
            }
        }

    reporting_information: ReportingInformation = Field()
    service_product_fulfillment: ServiceProductFulfillment = Field()
    verification_of_asset_response: VerificationOfAssetResponse = Field()

VerificationOfAsset.update_forward_refs()
