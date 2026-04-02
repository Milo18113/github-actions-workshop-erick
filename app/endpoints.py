from fastapi import FastAPI
from pydantic import BaseModel
from .calculator import sum, resta, multiply

app = FastAPI(title="Calculator API", version="1.0.0")

class OperationRequest(BaseModel):
    a: int
    b: int

class OperationResponse(BaseModel):
    result: int

@app.post("/sum", response_model=OperationResponse)
def sum_endpoint(request: OperationRequest):
    """Suma dos números"""
    result = sum(request.a, request.b)
    return OperationResponse(result=result)

@app.post("/resta", response_model=OperationResponse)
def resta_endpoint(request: OperationRequest):
    """Resta dos números"""
    result = resta(request.a, request.b)
    return OperationResponse(result=result)

@app.post("/multiplicacion", response_model=OperationResponse)
def multiply_endpoint(request: OperationRequest):
    """Multiplica dos números"""
    result = multiply(request.a, request.b)
    return OperationResponse(result=result)
