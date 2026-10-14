# ci-cd-demo-python

Demo de pipeline CI/CD con GitHub Actions, Docker y pytest.

## Estructura

- `src/` — Código fuente (FastAPI + calculadora)
- `tests/unit/` — Pruebas unitarias con pytest
- `.github/workflows/github-actions.yml` — Pipeline CI/CD

## Ejecución local

    pip install -r requirements-dev.txt
    pytest tests/unit/ -v --cov=src
    uvicorn src.main:app --reload

## Pipeline

1. **build-and-test**: instala deps y ejecuta pytest con cobertura.
2. **docker-build**: construye y publica imagen en GHCR.
3. **deploy**: despliega vía SSH con docker compose.

## Secrets requeridos

| Secret | Descripción |
|--------|-------------|
| `SSH_HOST` | IP/hostname del servidor |
| `SSH_USER` | Usuario SSH |
| `SSH_PRIVATE_KEY` | Clave privada SSH |
