# main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Input model
class input_item(BaseModel):
    name: str
    description: str
    price: float

# Output model
class output_item(BaseModel):
    id: int
    name: str
    description: str
    price_with_tax: float

def modify_input(input: input_item):
    return input.name + " (modified)"



@app.post("/",response_model=output_item)
async def create_item(item: input_item):
    item_id = 1  # Example static ID
    price_with_tax = item.price * 1.2  # Example tax calculation
    modified_name = modify_input(item)
    return {
        "id": item_id,
        "name": modified_name,
        "description": item.description,
        "price_with_tax": price_with_tax
    }


