from typing import Dict, Optional, List, Any, Union

from databases.interfaces import Record

from database import database
from model.customer import Customer


def _to_customer(record: Record) -> Customer:
    return Customer(
        customer_id=record["customer_id"],
        first_name=record["first_name"],
        last_name=record["last_name"],
        email=record["email"],
    )


async def create_customer(customer: Customer) -> str:
    query: str = """
    INSERT INTO customer (first_name, last_name, email)
    VALUES (:first_name, :last_name, :email)
    """

    values: Dict[str, str] = {
        "first_name": customer.first_name,
        "last_name": customer.last_name,
        "email": customer.email,
    }

    await database.execute(query, values)
    return "customer created successfully"


async def update_customer_by_id(customer_id: int, customer: Customer) -> str:
    query: str = """ 
    UPDATE customer
    SET first_name = :first_name, 
    last_name = :last_name, 
    email = :email
    WHERE customer_id = :customer_id
    """

    values: Dict[str, Union[str, int]] = {
        "first_name": customer.first_name,
        "last_name": customer.last_name,
        "email": customer.email,
        "customer_id": customer_id,
    }

    await database.execute(query, values)
    return f"customer with id: {customer_id} updated successfully"
    
    
async def get_customer_by_id(customer_id: int) -> Optional[Customer]:
    query: str = """
    SELECT * FROM customer WHERE customer_id = :customer_id
    """

    values: Dict[str, int] = {
        "customer_id": customer_id,
    }

    record: Optional[Record] = await database.fetch_one(query, values)
    return _to_customer(record) if record else None


async def get_all_customers() -> List[Customer]:
    query: str = """
    SELECT * FROM customer
    """

    records: List[Record] = await database.fetch_all(query)
    return [_to_customer(record) for record in records]


async def delete_customer_by_id(customer_id: int) -> str:
    query: str = """
    DELETE FROM customer WHERE customer_id = :customer_id
    """

    values: Dict[str, int] = {
        "customer_id": customer_id,
    }

    await database.execute(query, values)
    return "customer deleted successfully"