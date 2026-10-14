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
3. **deploy**: desactivado (requiere servidor SSH). Ver instrucciones en el workflow.

## Estado del pipeline

| Job | Estado | Descripción |
|-----|--------|-------------|
| `build-and-test` | ✅ Activo | Ejecuta pytest con cobertura |
| `docker-build`   | ✅ Activo | Publica imagen en GHCR |
| `deploy`         | ⏸️ Desactivado | Requiere servidor SSH (ver instrucciones en el workflow) |

### ¿Cómo activar el deploy?

1. Conseguir un servidor con Docker + docker-compose.
   Opciones gratuitas recomendadas: Oracle Cloud Free Tier, AWS EC2 t3.micro.
2. Generar par de claves SSH y copiar la pública al servidor.
3. Configurar los secrets `SSH_HOST`, `SSH_USER`, `SSH_PRIVATE_KEY` en GitHub.
4. Editar `.github/workflows/github-actions.yml`, cambiar `if: false` por
   la condición de rama y descomentar los pasos marcados con `# DEPLOY-ACTIVO`.

## Secrets requeridos

Ninguno para el pipeline actual. El job `deploy` está desactivado, así que
los secrets `SSH_HOST`, `SSH_USER` y `SSH_PRIVATE_KEY` solo serán necesarios
cuando se active el despliegue.
