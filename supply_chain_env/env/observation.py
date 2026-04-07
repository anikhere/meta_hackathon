from pydantic import BaseModel, Field


class Observation(BaseModel):
    inventory: int = Field(..., ge=0, description="Current inventory level")
    demand: int = Field(..., ge=0, description="Current step demand")

    def to_dict(self):
        return self.model_dump()
