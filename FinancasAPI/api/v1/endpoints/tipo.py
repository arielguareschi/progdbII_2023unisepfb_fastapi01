from typing import List
from fastapi import APIRouter, status

from models.tipo_model import TipoModel
from core.database import connection


router = APIRouter()


@router.get('/', response_model=List[TipoModel])
async def get_tipos():
    cursor = connection.cursor(dictionary=True)
    cursor.execute("select * from tipo")
    results = cursor.fetchall()

    cursor.close()
    #connection.close()
    return results


@router.get('/{tipo_id}', response_model=TipoModel)
async def get_tipo(tipo_id: int):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("select * from tipo where id = %s", [tipo_id])
    result = cursor.fetchone()

    cursor.close()
    #connection.close()
    return result


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=TipoModel)
async def post_tipo(tipo: TipoModel):
    sql = "insert into tipo (descricao, tipo) values (%s, %s)"
    valores = [tipo.descricao, tipo.tipo]

    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, valores)
    connection.commit()

    last_id = cursor.lastrowid
    cursor.execute("select * from tipo where id = %s", [last_id])
    result = cursor.fetchone()

    cursor.close()
    #connection.close()
    return result
