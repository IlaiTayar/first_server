from typing import Optional, List



from model.customer import Customer, CustomerStatus
from repository import customer_repository, order_repository





async def create_customer(customer: Customer) -> Optional[str]:
    for e_customer in await customer_repository.get_all_customers():
        if customer.email == e_customer.email:
            return None

    if customer.status == CustomerStatus.VIP:
        vip_customers: List[Customer] = await customer_repository.get_customer_by_status(CustomerStatus.VIP)
        if len(vip_customers) >= 10:
            return "MAXED"

    return await customer_repository.create_customer(customer)


async def update_customer_by_id(customer_id: int, customer: Customer) -> Optional[str]:
    existing_customer: Optional[Customer] = await customer_repository.get_customer_by_id(customer_id)

    if not existing_customer:
        return None

    if customer.status == CustomerStatus.VIP:
        vip_customers: List[Customer] = await customer_repository.get_customer_by_status(CustomerStatus.VIP)
        if len(vip_customers) >= 10:
            return "MAXED"

    return await customer_repository.update_customer_by_id(customer_id, customer)


async def get_customer_by_id(customer_id: int) -> Optional[Customer]:
    customer:Optional[Customer] = await customer_repository.get_customer_by_id(customer_id)

    if not customer:
        return None

    return customer


async def get_all_customers() -> List[Customer]:
    return await customer_repository.get_all_customers()


async def delete_customer_by_id(customer_id: int) -> Optional[str]:
    existing_customer: Optional[Customer] = await customer_repository.get_customer_by_id(customer_id)
    if not existing_customer:
        return None

    customer_orders = await order_repository.get_orders_by_customer_id(customer_id)
    for order in customer_orders:
        order_id = order.order_id
        await order_repository.delete_order_by_id(order_id)

    return await customer_repository.delete_customer_by_id(customer_id)