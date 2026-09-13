from decimal import Decimal

from pydantic import BaseModel, Field


class Order(BaseModel):
    order_id: int = Field(
        default=0,
        json_schema_extra={"readOnly": True}
    )
    customer_id: int
    item_name: str
    price: Decimal