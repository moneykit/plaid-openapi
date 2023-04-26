# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.party_individual import PartyIndividual
from plaid_skel.models.roles import Roles
from plaid_skel.models.taxpayer_identifiers import TaxpayerIdentifiers




class Party(BaseModel):
    """A collection of information about a single party to a transaction. Included direct participants like the borrower and seller as well as indirect participants such as the flood certificate provider."""


    individual: PartyIndividual = Field()
    roles: Roles = Field()
    taxpayer_identifiers: TaxpayerIdentifiers = Field()

Party.update_forward_refs()
