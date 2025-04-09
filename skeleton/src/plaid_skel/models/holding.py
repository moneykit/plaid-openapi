# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class Holding(BaseModel):
    """A securities holding at an institution."""


    account_id: str = Field( description="The Plaid `account_id` associated with the holding.")
    security_id: str = Field( description="The Plaid `security_id` associated with the holding. Security data is not specific to a user's account; any user who held the same security at the same financial institution at the same time would have identical security data. The `security_id` for the same security will typically be the same across different institutions, but this is not guaranteed. The `security_id` does not typically change, but may change if inherent details of the security change due to a corporate action, for example, in the event of a ticker symbol change or CUSIP change.")
    institution_price: float = Field( description="The last price given by the institution for this security.")
    institution_price_as_of: Optional[date_] = Field(default=None, description="The date at which `institution_price` was current.")
    institution_price_datetime: Optional[datetime_] = Field(default=None, description="Date and time at which `institution_price` was current, in ISO 8601 format (YYYY-MM-DDTHH:mm:ssZ).  This field is returned for select financial institutions and comes as provided by the institution. It may contain default time values (such as 00:00:00). ")
    institution_value: float = Field( description="The value of the holding, as reported by the institution.")
    cost_basis: Optional[float] = Field(default=None, description="The original total value of the holding. This field is calculated by Plaid as the sum of the purchase price of all of the shares in the holding.")
    quantity: float = Field( description="The total quantity of the asset held, as reported by the financial institution. If the security is an option, `quantity` will reflect the total number of options (typically the number of contracts multiplied by 100), not the number of contracts.")
    iso_currency_code: Optional[str] = Field(default=None, description="The ISO-4217 currency code of the holding. Always `null` if `unofficial_currency_code` is non-`null`.")
    unofficial_currency_code: Optional[str] = Field(default=None, description="The unofficial currency code associated with the holding. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s. ")

Holding.update_forward_refs()
