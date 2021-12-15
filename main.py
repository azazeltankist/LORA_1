from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.post("/webhook")
def webhook(item):
    print(item)
    return {"success": True}


@app.post("/webhook/uplink")
def uplink(item: dict):
    print(item)
    return {"success": True}
