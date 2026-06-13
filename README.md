# LEDS Agenda — Ambiente de Desenvolvimento

## Descrição

Este projeto utiliza Docker Compose para executar:

- uma aplicação Python com FastAPI;
- um banco de dados PostgreSQL.

O ambiente de desenvolvimento utiliza `docker-compose.override.yml`, bind mount e hot reload.

## Preparar o ambiente

Copie o arquivo de exemplo:

```bash
cp .env.example .env
```

O arquivo `.env` não deve ser enviado ao GitHub.

## Subir o ambiente

```bash
docker compose up --build
```

Para executar em segundo plano:

```bash
docker compose up --build -d
```

## Acessar a aplicação

API:

```text
http://localhost:8000
```

Documentação Swagger:

```text
http://localhost:8000/docs
```

Verificação do banco:

```text
http://localhost:8000/banco
```

## Verificar os serviços

```bash
docker compose ps
```

## Visualizar logs

Logs de todos os serviços:

```bash
docker compose logs -f
```

Logs da API:

```bash
docker compose logs -f api
```

Logs do banco:

```bash
docker compose logs -f db
```

## Hot reload

A pasta local `src` é montada dentro do contêiner:

```yaml
volumes:
  - ./src:/app/src
```

Ao alterar e salvar o arquivo `src/main.py`, a aplicação reinicia automaticamente.

## Encerrar os contêineres

```bash
docker compose down
```

## Remover os volumes

Use apenas quando desejar apagar os dados locais do PostgreSQL:

```bash
docker compose down -v
```