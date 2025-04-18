# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.address import Address
from plaid_skel.models.pslf_status import PSLFStatus
from plaid_skel.models.student_loan_repayment_model import StudentLoanRepaymentModel
from plaid_skel.models.student_loan_status import StudentLoanStatus




class LiabilityOverride(BaseModel):
    """Used to configure Sandbox test data for the Liabilities product"""


    type: str = Field( description="The type of the liability object, either `credit` or `student`. Mortgages are not currently supported in the custom Sandbox.")
    purchase_apr: float = Field( description="The purchase APR percentage value. For simplicity, this is the only interest rate used to calculate interest charges. Can only be set if `type` is `credit`.")
    cash_apr: float = Field( description="The cash APR percentage value. Can only be set if `type` is `credit`.")
    balance_transfer_apr: float = Field( description="The balance transfer APR percentage value. Can only be set if `type` is `credit`.")
    special_apr: float = Field( description="The special APR percentage value. Can only be set if `type` is `credit`.")
    last_payment_amount: float = Field( description="Override the `last_payment_amount` field. Can only be set if `type` is `credit`.")
    minimum_payment_amount: float = Field( description="Override the `minimum_payment_amount` field. Can only be set if `type` is `credit` or `student`.")
    is_overdue: bool = Field( description="Override the `is_overdue` field")
    origination_date: date_ = Field( description="The date on which the loan was initially lent, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format. Can only be set if `type` is `student`.")
    principal: float = Field( description="The original loan principal. Can only be set if `type` is `student`.")
    nominal_apr: float = Field( description="The interest rate on the loan as a percentage. Can only be set if `type` is `student`.")
    interest_capitalization_grace_period_months: float = Field( description="If set, interest capitalization begins at the given number of months after loan origination. By default interest is never capitalized. Can only be set if `type` is `student`.")
    repayment_model: StudentLoanRepaymentModel = Field()
    expected_payoff_date: date_ = Field( description="Override the `expected_payoff_date` field. Can only be set if `type` is `student`.")
    guarantor: str = Field( description="Override the `guarantor` field. Can only be set if `type` is `student`.")
    is_federal: bool = Field( description="Override the `is_federal` field. Can only be set if `type` is `student`.")
    loan_name: str = Field( description="Override the `loan_name` field. Can only be set if `type` is `student`.")
    loan_status: StudentLoanStatus = Field()
    payment_reference_number: str = Field( description="Override the `payment_reference_number` field. Can only be set if `type` is `student`.")
    pslf_status: PSLFStatus = Field()
    repayment_plan_description: str = Field( description="Override the `repayment_plan.description` field. Can only be set if `type` is `student`.")
    repayment_plan_type: str = Field( description="Override the `repayment_plan.type` field. Can only be set if `type` is `student`. Possible values are: `\"extended graduated\"`, `\"extended standard\"`, `\"graduated\"`, `\"income-contingent repayment\"`, `\"income-based repayment\"`, `\"interest only\"`, `\"other\"`, `\"pay as you earn\"`, `\"revised pay as you earn\"`, or `\"standard\"`.")
    sequence_number: str = Field( description="Override the `sequence_number` field. Can only be set if `type` is `student`.")
    servicer_address: Address = Field()

LiabilityOverride.update_forward_refs()
