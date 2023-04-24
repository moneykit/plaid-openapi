# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.

from enum import Enum


class IdentityVerificationStepStatus(str, Enum):
    SUCCESS = "success"
    ACTIVE = "active"
    FAILED = "failed"
    WAITING_FOR_PREREQUISITE = "waiting_for_prerequisite"
    NOT_APPLICABLE = "not_applicable"
    SKIPPED = "skipped"
    EXPIRED = "expired"
    CANCELED = "canceled"
    PENDING_REVIEW = "pending_review"
    MANUALLY_APPROVED = "manually_approved"
    MANUALLY_REJECTED = "manually_rejected"
