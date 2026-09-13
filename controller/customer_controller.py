from typing import Optional, List

from fastapi import APIRouter, HTTPException

from model.customer import Customer
from repository import customer_repository

router: APIRouter = APIRouter(
    prefix="/customer",
    tags=["customer"]
)

@router.post("/create_customer", status_code=201)
async def create_customer(customer: Customer) -> str:
    return await customer_repository.create_customer(customer)


@router.put("/update_customer-{customer_id}", response_model=Optional[Customer] ,status_code=200)
async def update_customer_by_id(customer_id: int, customer: Customer) -> Optional[Customer]:
    existing_customer: Optional[Customer] = await customer_repository.get_customer_by_id(customer_id)
    if not existing_customer:
        raise HTTPException(status_code=404, detail="Customer with id: {customer_id} not found")
    return await customer_repository.update_customer_by_id(customer_id, customer)


@router.get("/get_customer-{customer_id}", response_model=Customer, status_code=200)
async def get_customer_by_id(customer_id: int) -> Optional[Customer]:
    customer:Optional[Customer] = await customer_repository.get_customer_by_id(customer_id)

    if not customer:
        raise HTTPException(status_code=404, detail=f"Customer with id: {customer_id} not found")

    return customer


@router.get("/get_all_customers",response_model=List[Customer], status_code=200)
async def get_all_customers() -> List[Customer]:
    return await customer_repository.get_all_customers()

@router.delete("/delete_customer-{customer_id}", status_code=200)
async def delete_customer_by_id(customer_id: int) -> str:
    customer: Optional[Customer] = await customer_repository.get_customer_by_id(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer with id: {customer_id} not found")
    return await customer_repository.delete_customer_by_id(customer_id)