# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.

from enum import Enum

from pydantic import GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue


class AccountSubtype(str, Enum):
    _401A = "401a"
    _401K = "401k"
    _403B = "403B"
    _457B = "457b"
    _529 = "529"
    BROKERAGE = "brokerage"
    CASH_ISA = "cash isa"
    CRYPTO_EXCHANGE = "crypto exchange"
    EDUCATION_SAVINGS_ACCOUNT = "education savings account"
    EBT = "ebt"
    FIXED_ANNUITY = "fixed annuity"
    GIC = "gic"
    HEALTH_REIMBURSEMENT_ARRANGEMENT = "health reimbursement arrangement"
    HSA = "hsa"
    ISA = "isa"
    IRA = "ira"
    LIF = "lif"
    LIFE_INSURANCE = "life insurance"
    LIRA = "lira"
    LRIF = "lrif"
    LRSP = "lrsp"
    NON_CUSTODIAL_WALLET = "non-custodial wallet"
    NON_TAXABLE_BROKERAGE_ACCOUNT = "non-taxable brokerage account"
    OTHER = "other"
    OTHER_INSURANCE = "other insurance"
    OTHER_ANNUITY = "other annuity"
    PRIF = "prif"
    RDSP = "rdsp"
    RESP = "resp"
    RLIF = "rlif"
    RRIF = "rrif"
    PENSION = "pension"
    PROFIT_SHARING_PLAN = "profit sharing plan"
    RETIREMENT = "retirement"
    ROTH = "roth"
    ROTH_401K = "roth 401k"
    RRSP = "rrsp"
    SEP_IRA = "sep ira"
    SIMPLE_IRA = "simple ira"
    SIPP = "sipp"
    STOCK_PLAN = "stock plan"
    THRIFT_SAVINGS_PLAN = "thrift savings plan"
    TFSA = "tfsa"
    TRUST = "trust"
    UGMA = "ugma"
    UTMA = "utma"
    VARIABLE_ANNUITY = "variable annuity"
    CREDIT_CARD = "credit card"
    PAYPAL = "paypal"
    CD = "cd"
    CHECKING = "checking"
    SAVINGS = "savings"
    MONEY_MARKET = "money market"
    PREPAID = "prepaid"
    AUTO = "auto"
    BUSINESS = "business"
    COMMERCIAL = "commercial"
    CONSTRUCTION = "construction"
    CONSUMER = "consumer"
    HOME_EQUITY = "home equity"
    LOAN = "loan"
    MORTGAGE = "mortgage"
    OVERDRAFT = "overdraft"
    LINE_OF_CREDIT = "line of credit"
    STUDENT = "student"
    CASH_MANAGEMENT = "cash management"
    KEOGH = "keogh"
    MUTUAL_FUND = "mutual fund"
    RECURRING = "recurring"
    REWARDS = "rewards"
    SAFE_DEPOSIT = "safe deposit"
    SARSEP = "sarsep"
    PAYROLL = "payroll"

    # Nullable OpenAPI enum
    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema: dict, handler: GetJsonSchemaHandler) -> JsonSchemaValue:
        schema = handler(field_schema)
        schema["nullable"] = True
        return schema
