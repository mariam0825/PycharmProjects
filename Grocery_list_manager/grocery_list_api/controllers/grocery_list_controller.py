from fastapi import APIRouter, Depends, HTTPException, status
from uuid import UUID
from models.grocery_list import GroceryItem, GroceryItemCreate, GroceryItemUpdate
from services.grocery_list_service import GroceryItemService, GroceryItemNotFoundError
from dependencies import get_grocery_item_service

router = APIRouter(prefix="/grocery-items", tags=["Grocery Items"])
@router.post(
    "/",
    response_model=GroceryItem,
    status_code=status.HTTP_201_CREATED
)
def create_grocery_item(
    payload: GroceryItemCreate,
    service: GroceryItemService = Depends(get_grocery_item_service),
):
    return service.create_grocery_item(payload)

@router.get("/", response_model=list[GroceryItem])
def list_grocery_items(
    service: GroceryItemService = Depends(get_grocery_item_service)
):
    return service.list_grocery_items()


@router.get("/{item_id}", response_model=GroceryItem)
def get_grocery_item(
    item_id: UUID,
    service: GroceryItemService = Depends(get_grocery_item_service),
):
    try:
        return service.get_grocery_item(item_id)

    except GroceryItemNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
@router.patch("/{item_id}", response_model=GroceryItem)
def update_grocery_item(
    item_id: UUID,
    payload: GroceryItemUpdate,
    service: GroceryItemService = Depends(get_grocery_item_service),
):
    try:
        return service.update_grocery_item(item_id, payload)
    except GroceryItemNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_grocery_item(
    item_id: UUID,
    service: GroceryItemService = Depends(get_grocery_item_service),
):
    try:
        service.delete_grocery_item(item_id)
    except GroceryItemNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))
