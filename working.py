from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

#create an object
app = FastAPI() 

class Item(BaseModel):
    name: str
    price: float
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
    
