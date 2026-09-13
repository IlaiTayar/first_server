from typing import Optional

from pydantic import BaseModel


class Order(BaseModel):
    order_id: Optional[int] = None
    customer_id: int
    item_name: str
    price: float