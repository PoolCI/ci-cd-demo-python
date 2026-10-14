"""API REST mínima con FastAPI que expone la calculadora."""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.calculator import add, subtract, multiply, divide

app = FastAPI(title="Calculadora API", version="0.1.0")


class Operation(BaseModel):
    a: float
    b: float


@app.get("/health")
def health():
    """Healthcheck para Docker y balanceadores de carga."""
    return {"status": "ok"}


@app.post("/add")
def api_add(op: Operation):
    return {"result": add(op.a, op.b)}


@app.post("/subtract")
def api_subtract(op: Operation):
    return {"result": subtract(op.a, op.b)}


@app.post("/multiply")
def api_multiply(op: Operation):
    return {"result": multiply(op.a, op.b)}


@app.post("/divide")
def api_divide(op: Operation):
    try:
        return {"result": divide(op.a, op.b)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
