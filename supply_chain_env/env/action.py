from pydantic import BaseModel, Field
from enum import Enum
from typing import Literal


class ActionType(str, Enum):
    ORDER_SMALL = "order_small"
    ORDER_LARGE = "order_large"
    DO_NOTHING = "do_nothing"


class Action(BaseModel):
    action: ActionType = Field(..., description="Action to take")

    @classmethod
    def from_string(cls, action: str) -> 'Action':
        return cls(action=ActionType(action))


ORDER_SMALL = ActionType.ORDER_SMALL
ORDER_LARGE = ActionType.ORDER_LARGE
DO_NOTHING = ActionType.DO_NOTHING
ACTIONS = [ORDER_SMALL, ORDER_LARGE, DO_NOTHING]
