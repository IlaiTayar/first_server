

from pydantic import BaseModel, Field


class Customer(BaseModel):
    customer_id: int = Field(
        default=0,
        json_schema_extra={"readOnly": True}
    )
    first_name: str
    last_name: str
    email: str