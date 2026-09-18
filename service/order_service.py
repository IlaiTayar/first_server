from typing import Optional, List

from model.customer import Customer
from model.order import Order
from repository import order_repository, customer_repository


async def create_order(order: Order) -> str:

    return await order_repository.create_order(order)


async def update_order_by_id(order_id: int, order: Order) -> Optional[str]:
    existing_order: Optional[Order] = await order_repository.get_order_by_id(order_id)

    if not existing_order:
        return None

    return await order_repository.update_order_by_id(order_id, order)


async def get_order_by_id(order_id: int) -> Optional[Order]:
    order: Optional[Order] = await order_repository.get_order_by_id(order_id)

    if not order:
        return None

    return order


async def get_orders_by_customer_id(customer_id: int) -> Optional[List[Order]]:
    customer: Optional[Customer] = await customer_repository.get_customer_by_id(customer_id)
    if not customer:
        return None
    return await order_repository.get_orders_by_customer_id(customer_id)


async def get_all_orders() -> List[Order]:

    return await order_repository.get_all_orders()


async def delete_order_by_id(order_id: int) -> Optional[str]:
    order: Optional[Order] = await order_repository.get_order_by_id(order_id)

    if not order:
        return None

    return await order_repository.delete_order_by_id(order_id)