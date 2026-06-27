from fastapi import FastAPI

app = FastAPI()


@app.get("/api/v1/orders/1")
def get_order():
    return {
        "id": 1,
        "user_id": 123,
        "product": "Laptop",
        "quantity": 2,
        "status": "CREATED"
    }