import os

import psycopg2
from fastapi import FastAPI

app = FastAPI(title="LEDS Agenda")


@app.get("/")
def home():
    return {
        "mensagem": "API LEDS Agenda em execução",
        "ambiente": os.getenv("APP_ENV", "development"),
    }


@app.get("/banco")
def verificar_banco():
    try:
        conexao = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST", "db"),
            port=os.getenv("POSTGRES_PORT", "5432"),
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
        )

        cursor = conexao.cursor()
        cursor.execute("SELECT version();")
        versao = cursor.fetchone()[0]

        cursor.close()
        conexao.close()

        return {
            "status": "Banco conectado",
            "versao": versao,
        }

    except Exception as erro:
        return {
            "status": "Erro ao conectar ao banco",
            "erro": str(erro),
        }