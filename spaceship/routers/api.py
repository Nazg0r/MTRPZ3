from fastapi import APIRouter
from numpy import random
router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}


@router.get('/multMatrix')
def get_matrix_multiplication():
    matrix_a = random.randint(0, 100, size=(10, 10))
    matrix_b = random.randint(0, 100, size=(10, 10))
    product = matrix_a @ matrix_b
    
    return {
        "matrix_a": str(matrix_a.tolist()),
        "matrix_b": str(matrix_b.tolist()),
        "product": str(product.tolist())
    }