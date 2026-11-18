from pydantic import BaseModel, Field


class CropPrediction(BaseModel):

    State: str = Field(...)

    District: str = Field(...)

    Market: str = Field(..., min_length=2, max_length=100)

    Commodity: str = Field(..., min_length=2, max_length=50)

    Variety: str = Field(..., min_length=2, max_length=100)

    Grade: str = Field(..., min_length=1, max_length=50)