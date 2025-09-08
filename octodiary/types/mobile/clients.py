#                 © Copyright 2023
#          Licensed under the MIT License
#        https://opensource.org/licenses/MIT
#           https://github.com/OctoDiary

from typing import Any, Optional

from pydantic import Field

from octodiary.types.model import DT, Type


class ClientId(Type):
    contract_id: int = Field(alias="contractId")
    staff_id: Optional[int] = Field(..., alias="staffId")
    person_id: Optional[str] = Field(..., alias="personId")


class Organization(Type):
    name: Optional[str] = None
    type: Optional[str] = None
    address: Optional[str] = None


class ExpenseConstraints(Type):
    balance_threshold: Optional[int] = Field(..., alias="balanceThreshold")
    expense_day_limit: Optional[int] = Field(..., alias="expenseDayLimit")


class Clients(Type):
    client_id: ClientId = Field(alias="clientId")
    organization: Organization
    preorder_allowed: Optional[bool] = Field(..., alias="preorderAllowed")
    balance: Optional[int] = None
    foodbox_allowed: Optional[bool] = Field(..., alias="foodboxAllowed")
    foodbox_available: Optional[bool] = Field(..., alias="foodboxAvailable")
    preorder_available: Optional[bool] = Field(..., alias="preorderAvailable")
    expense_constraints: ExpenseConstraints = Field(alias="expenseConstraints")
    rnipsc: Optional[str] = None

    class Config:
        populate_by_name = True