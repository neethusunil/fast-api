from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

#create an object
app = FastAPI() 

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

inventory = {
    
}

#path parameters
@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The ID of the item that you would like to view")):
    return inventory[item_id]

#query parameters
@app.get("/get-by-name")
def get_item(test: int,name: Optional[str] = None ):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data": "Not found"}


#request body
@app.post("/create-item/{item-id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists."}
    inventory[item_id] = item
    return inventory[item_id]
    
@app.put("/update-item/{item_id")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {"Error": "Item ID doe not exists."}
    if item.name != None:
        inventory[item_id].name= item.name 
    if item.price != None:
        inventory[item_id].price= item.price 
    if item.brand != None:
        inventory[item_id].brand= item.brand 
    return inventory[item_id]
