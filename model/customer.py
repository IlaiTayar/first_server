from typing import Optional

from pydantic import BaseModel, Field


class Customer(BaseModel):
    customer_id: Optional[int] = None
    first_name: str
    last_name: str
    email: str