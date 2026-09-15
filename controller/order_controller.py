from typing import List, Optional

from fastapi import APIRouter, HTTPException

from model.customer import Customer
from model.order import Order
from repository import order_repository, customer_repository

router = APIRouter(
    prefix="/order",
    tags=["order"]
)


@router.post("/create_order", status_code=201)
async def create_order(order: Order) -> str:
    customer: Optional[Customer] = await customer_repository.get_customer_by_id(order.customer_id)

    if not customer:
        raise HTTPException(status_code=404, detail=f"Customer with id: {order.customer_id} not found")

    return await order_repository.create_order(order)


@router.put("/update_order-{order_id}", status_code=200)
async def update_order(order_id: int, order: Order) -> str:
    existing_order = await order_repository.get_order_by_id(order_id)

    if not existing_order:
        raise HTTPException(status_code=404, detail=f"Order with id: {order_id} not found")

    return await order_repository.update_order_by_id(order_id, order)


@router.get("/get_order-{order_id}", response_model=Order ,status_code=200)
async def get_order_by_id(order_id: int) -> Order:
    order: Optional[Order] = await order_repository.get_order_by_id(order_id)

    if not order:
        raise HTTPException(status_code=404, detail=f"Order with id: {order_id} not found")

    return order


@router.get("/get_order_by_customer-{customer_id}", response_model=List[Order] ,status_code=200)
async def get_order_by_customer(customer_id: int) -> List[Order]:
    customer: Optional[Customer] = await customer_repository.get_customer_by_id(customer_id)

    if not customer:
        raise HTTPException(status_code=404, detail=f"Customer with id: {customer_id} not found")

    return await order_repository.get_orders_by_customer_id(customer_id)

@router.get("/get_all_orders", response_model=List[Order],status_code=200)
async def get_all_orders() -> List[Order]:

    return await order_repository.get_all_orders()


@router.delete("/delete_order-{order_id}", status_code=200)
async def delete_order_by_id(order_id: int) -> str:
    order: Optional[Order] = await order_repository.get_order_by_id(order_id)

    if not order:
        raise HTTPException(status_code=404, detail=f"Order with id: {order_id} not found")

    return await order_repository.delete_order_by_id(order_id)