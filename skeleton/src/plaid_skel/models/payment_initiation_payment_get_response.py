# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.external_payment_refund_details import ExternalPaymentRefundDetails
from plaid_skel.models.external_payment_schedule_get import ExternalPaymentScheduleGet
from plaid_skel.models.payment_amount import PaymentAmount
from plaid_skel.models.payment_amount_refunded import PaymentAmountRefunded
from plaid_skel.models.payment_initiation_payment_status import PaymentInitiationPaymentStatus
from plaid_skel.models.payment_scheme import PaymentScheme
from plaid_skel.models.sender_bacs_nullable import SenderBACSNullable




class PaymentInitiationPaymentGetResponse(BaseModel):
    """PaymentInitiationPaymentGetResponse defines the response schema for `/payment_initation/payment/get`"""


    payment_id: str = Field( description="The ID of the payment. Like all Plaid identifiers, the `payment_id` is case sensitive.")
    amount: PaymentAmount = Field()
    status: PaymentInitiationPaymentStatus = Field()
    recipient_id: str = Field( description="The ID of the recipient")
    reference: str = Field( description="A reference for the payment.")
    adjusted_reference: Optional[str] = Field(default=None, description="The value of the reference sent to the bank after adjustment to pass bank validation rules.")
    last_status_update: datetime = Field( description="The date and time of the last time the `status` was updated, in IS0 8601 format")
    schedule: Optional[ExternalPaymentScheduleGet] = Field(default=None,)
    refund_details: Optional[ExternalPaymentRefundDetails] = Field(default=None,)
    bacs: Optional[SenderBACSNullable] = Field(default=None,)
    iban: Optional[str] = Field(default=None, description="The International Bank Account Number (IBAN) for the sender, if specified in the `/payment_initiation/payment/create` call.")
    refund_ids: Optional[List[str]] = Field(default=None, description="Refund IDs associated with the payment.")
    amount_refunded: Optional[PaymentAmountRefunded] = Field(default=None,)
    wallet_id: Optional[str] = Field(default=None, description="The EMI (E-Money Institution) wallet that this payment is associated with, if any. This wallet is used as an intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests.")
    scheme: Optional[PaymentScheme] = Field(default=None,)
    adjusted_scheme: Optional[PaymentScheme] = Field(default=None,)
    consent_id: Optional[str] = Field(default=None, description="The payment consent ID that this payment was initiated with. Is present only when payment was initiated using the payment consent.")
    transaction_id: Optional[str] = Field(default=None, description="The transaction ID that this payment is associated with, if any. This is present only when a payment was initiated using virtual accounts.")
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

PaymentInitiationPaymentGetResponse.update_forward_refs()
