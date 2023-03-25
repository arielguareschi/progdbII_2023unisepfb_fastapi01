import mysql.connector as mysql
from core.configs import settings

connection = mysql.connect(
    host=settings.DB_HOST,
    user=settings.DB_USER,
    password=settings.DB_PASS,
    database=settings.DB_NAME
)
