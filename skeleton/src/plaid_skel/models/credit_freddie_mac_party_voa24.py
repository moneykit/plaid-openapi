# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.credit_freddie_mac_party_individual_voa24 import CreditFreddieMacPartyIndividualVOA24
from plaid_skel.models.roles import Roles
from plaid_skel.models.taxpayer_identifiers import TaxpayerIdentifiers




class CreditFreddieMacPartyVOA24(BaseModel):
    """A collection of information about a single party to a transaction. Included direct participants like the borrower and seller as well as indirect participants such as the flood certificate provider."""


    individual: CreditFreddieMacPartyIndividualVOA24 = Field()
    roles: Roles = Field()
    taxpayer_identifiers: TaxpayerIdentifiers = Field()

CreditFreddieMacPartyVOA24.update_forward_refs()
