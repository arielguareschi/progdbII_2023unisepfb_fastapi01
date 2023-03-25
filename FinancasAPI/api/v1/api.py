from fastapi import APIRouter

from api.v1.endpoints import (
    lancamento,
    saldodiario,
    tipo
)


api_router = APIRouter()
api_router.include_router(lancamento.router,
                          prefix='/lancamento',
                          tags=['Lançamentos'])
api_router.include_router(saldodiario.router,
                          prefix='/saldodiario',
                          tags=['Saldo Diario'])
api_router.include_router(tipo.router,
                          prefix='/tipo',
                          tags=['Tipo'])
