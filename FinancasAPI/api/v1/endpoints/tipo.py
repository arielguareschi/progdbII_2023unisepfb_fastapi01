from typing import List
from fastapi import APIRouter

from models.tipo_model import TipoModel
from core.database import connection


router = APIRouter()

@router.get('/', response_model=List[TipoModel])
async def get_tipos():
    cursor = connection.cursor(dictionary=True)
    cursor.execute("select * from tipo")
    results = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return results