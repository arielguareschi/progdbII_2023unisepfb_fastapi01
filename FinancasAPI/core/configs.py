from pydantic import BaseSettings


class Settings(BaseSettings):
    '''
        Configuracoes basicas da API
    '''
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 