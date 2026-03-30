"""Starter code for the Building REST APIs with FastAPI assignment."""

from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Student API")


class Item(BaseModel):
    id: int
    name: str
    category: str


items: List[Item] = [
    Item(id=1, name="Sample Item", category="demo")
]


@app.get("/")
def root():
    return {"message": "Welcome to your FastAPI assignment API"}


@app.get("/items")
def get_items():
    # TODO: Return all items.
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    # TODO: Find and return a single item by id.
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items")
def create_item(item: Item):
    # TODO: Add duplicate id checks before appending.
    items.append(item)
    return {"message": "Item created", "item": item}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # TODO: Remove an item by id and return a status message.
    for i, item in enumerate(items):
        if item.id == item_id:
            removed = items.pop(i)
            return {"message": "Item deleted", "item": removed}
    raise HTTPException(status_code=404, detail="Item not found")
