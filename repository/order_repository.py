from typing import Dict, Optional, List, Union

from databases.interfaces import Record

from database import database
from model.order import Order


def _to_order(record: Record) -> Order:
    return Order(
        order_id=record["order_id"],
        customer_id=record["customer_id"],
        item_name=record["item_name"],
        price=record["price"]
    )


async def create_order(order: Order) -> str:
    query = """
    INSERT INTO orders ( customer_id, item_name, price)
    VALUES (:customer_id, :item_name, :price)
    """

    values: Dict[str, Union[str, float]] = {
        "customer_id": order.customer_id,
        "item_name": order.item_name,
        "price": order.price
    }

    await database.execute(query, values)
    return "order created successfully"


async def update_order_by_id(order_id: int, order: Order) -> str:
    query = """
    update orders 
    set customer_id = :customer_id, 
    item_name = :item_name, 
    price = :price 
    where order_id = :order_id
    """

    values: Dict[str, Union[str, float]] = {
        "customer_id": order.customer_id,
        "item_name": order.item_name,
        "price": order.price,
        "order_id": order_id
    }

    await database.execute(query, values)
    return f"order with id: {order_id} updated successfully"


async def get_order_by_id(order_id: int) -> Optional[Order]:
    query = """
    select * from orders where order_id = :order_id
    """

    values: Dict[str, int] = {
        "order_id": order_id
    }

    record: Optional[Record] = await database.fetch_one(query, values)
    return _to_order(record) if record else None


async def get_all_orders() -> List[Order]:
    query = """
    select * from orders
    """

    records: List[Record] = await database.fetch_all(query)
    return [_to_order(record) for record in records]


async def delete_order_by_id(order_id: int) -> str:
    query = """
    delete from orders where order_id = :order_id
    """

    values: Dict[str, int] = {
        "order_id": order_id
    }

    await database.execute(query, values)
    return "order deleted successfully"