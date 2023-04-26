# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class MFA(BaseModel):
    """Specifies the multi-factor authentication settings to use with this test account"""


    type: str = Field( description="Possible values are `device`, `selections`, or `questions`.  If value is `device`, the MFA answer is `1234`.  If value is `selections`, the MFA answer is always the first option.  If value is `questions`, the MFA answer is  `answer_<i>_<j>` for the j-th question in the i-th round, starting from 0. For example, the answer to the first question in the second round is `answer_1_0`.")
    question_rounds: float = Field( description="Number of rounds of questions. Required if value of `type` is `questions`. ")
    questions_per_round: float = Field( description="Number of questions per round. Required if value of `type` is `questions`. If value of type is `selections`, default value is 2.")
    selection_rounds: float = Field( description="Number of rounds of selections, used if `type` is `selections`. Defaults to 1.")
    selections_per_question: float = Field( description="Number of available answers per question, used if `type` is `selection`. Defaults to 2. ")

MFA.update_forward_refs()
