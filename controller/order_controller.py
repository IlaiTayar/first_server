from typing import List, Optional

from fastapi import APIRouter, HTTPException

from model.order import Order
from service import order_service

router = APIRouter(
    prefix="/order",
    tags=["order"]
)


@router.post("/create_order", status_code=201)
async def create_order(order: Order) -> str:

    return await order_service.create_order(order)


@router.put("/update_order-{order_id}", status_code=200)
async def update_order_by_id(order_id: int, order: Order) -> str:

    result: Optional[str] = await order_service.update_order_by_id(order_id, order)
    if not result:
        raise HTTPException(status_code=404, detail=f"Order with id: {order_id} not found")

    return result


@router.get("/get_order-{order_id}", response_model=Order ,status_code=200)
async def get_order_by_id(order_id: int) -> Order:
    result: Optional[Order] = await order_service.get_order_by_id(order_id)

    if not result:
        raise HTTPException(status_code=404, detail=f"Order with id: {order_id} not found")

    return result


@router.get("/get_order_by_customer-{customer_id}", response_model=List[Order] ,status_code=200)
async def get_order_by_customer_id(customer_id: int) -> List[Order]:
    result: Optional[List[Order]] = await order_service.get_orders_by_customer_id(customer_id)
    if not result:
        raise HTTPException(status_code=404, detail=f"Customer with id: {customer_id} not found")

    return result


@router.get("/get_all_orders", response_model=List[Order],status_code=200)
async def get_all_orders() -> List[Order]:

    return await order_service.get_all_orders()


@router.delete("/delete_order-{order_id}", status_code=200)
async def delete_order_by_id(order_id: int) -> str:
    result: Optional[str] = await order_service.delete_order_by_id(order_id)

    if not result:
        raise HTTPException(status_code=404, detail=f"Order with id: {order_id} not found")

    return result