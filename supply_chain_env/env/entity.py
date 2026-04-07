from dataclasses import dataclass
@dataclass
class State:
    inventory:int
    money:int
    demand:int