from pydantic import BaseModel

class CarPrice(BaseModel):
    brand: str
    model: str
    year: int
    fuelType: str
    transmission: str
    kmDriven: float
    ownerType: str
    mileage: float
    engineCC: float
    conditionRating: float
    originalPrice: float
    daysToSell: int
    carAge: int
    demandScore: float
    brandPopularityScore: float
    premiumCar: str