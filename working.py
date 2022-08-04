from fastapi import FastAPI, Path
from typing import Optional

#create an object
app = FastAPI() 

inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Milma"
    }
}

#path parameters
@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The ID of the item that you would like to view", gt=0, lt=2)):
    return inventory[item_id]

#query parameters
@app.get("/get-by-name")
def get_item(test: int,name: Optional[str] = None ):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not found"}
