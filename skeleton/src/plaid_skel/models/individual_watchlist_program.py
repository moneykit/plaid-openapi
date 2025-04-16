# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401
from plaid_skel.models.individual_watchlist_code import IndividualWatchlistCode
from plaid_skel.models.program_name_sensitivity import ProgramNameSensitivity
from plaid_skel.models.watchlist_screening_audit_trail import WatchlistScreeningAuditTrail




class IndividualWatchlistProgram(BaseModel):
    """A program that configures the active lists, search parameters, and other behavior for initial and ongoing screening of individuals."""


    id: str = Field( description="ID of the associated program.")
    created_at: datetime_ = Field( description="An ISO8601 formatted timestamp.")
    is_rescanning_enabled: bool = Field( description="Indicator specifying whether the program is enabled and will perform daily rescans.")
    lists_enabled: list[IndividualWatchlistCode] = Field( description="Watchlists enabled for the associated program")
    name: str = Field( description="A name for the program to define its purpose. For example, \"High Risk Individuals\", \"US Cardholders\", or \"Applicants\".")
    name_sensitivity: ProgramNameSensitivity = Field()
    audit_trail: WatchlistScreeningAuditTrail = Field()
    is_archived: bool = Field( description="Archived programs are read-only and cannot screen new customers nor participate in ongoing monitoring.")

    @field_validator("name")
    @classmethod
    def name_min_length(cls, value):
        assert len(value) >= 1
        return value

IndividualWatchlistProgram.update_forward_refs()
