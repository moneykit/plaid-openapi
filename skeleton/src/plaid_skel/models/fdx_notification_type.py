# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.

from enum import Enum


class FDXNotificationType(str, Enum):
    CONSENT_REVOKED = "CONSENT_REVOKED"
    CONSENT_UPDATED = "CONSENT_UPDATED"
    CUSTOM = "CUSTOM"
    SERVICE = "SERVICE"
    BALANCE = "BALANCE"
    PLANNED_OUTAGE = "PLANNED_OUTAGE"
