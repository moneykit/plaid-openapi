# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.credit_freddie_mac_reporting_information_voa24 import CreditFreddieMacReportingInformationVOA24
from plaid_skel.models.credit_freddie_mac_verification_of_asset_response_voe25 import CreditFreddieMacVerificationOfAssetResponseVOE25
from plaid_skel.models.service_product_fulfillment import ServiceProductFulfillment




class CreditFreddieMacVerificationOfAssetVOE25(BaseModel):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#credit_freddie_mac_verification_of_asset_voe25"
            }
        }

    reporting_information: CreditFreddieMacReportingInformationVOA24 = Field()
    service_product_fulfillment: ServiceProductFulfillment = Field()
    verification_of_asset_response: CreditFreddieMacVerificationOfAssetResponseVOE25 = Field()

CreditFreddieMacVerificationOfAssetVOE25.update_forward_refs()
