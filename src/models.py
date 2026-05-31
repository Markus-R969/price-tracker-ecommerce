from pydantic import BaseModel, Field
import datetime

class Product(BaseModel):
    url: str
    name: str
    price: float
    currency: str = "GBP"
    scraped_at: str = Field(default_factory=lambda: datetime.datetime.now().isoformat())