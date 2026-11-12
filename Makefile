# OrtesisLab. Requisitos: GNU Make, Docker, uv y Python 3.14.
# Las recetas se ejecutan en el shell (cmd.exe o sh). La infraestructura
# local son cinco objetivos; el comportamiento esta en scripts/BaseLocal.py.
# Alembic no forma parte de esos cinco: lo aplican `up` y `migrar`.

.DEFAULT_GOAL := help
.NOTPARALLEL:

PYTHON ?= uv run python
export ENV_FILE ?= apps/db/.env
export DB_NAME ?= ortesislab_dev
export DB_ADMIN ?= ortesislab_admin
export BUCKET ?= ortesislab
export FILE
export CONFIRM
export ACCION

.PHONY: help install up web worker migrar empaquetar test test-blender lint \
	db-up db-down db-estado db-respaldo db-reset

help:
	@echo "Objetivos:"
	@echo "  install                  Python 3.14, dependencias y .env de ejemplo si faltan"
	@echo "  up                       db-up y alembic upgrade head"
	@echo "  web                      Reflex en http://localhost:3000"
	@echo "  worker                   Cola de generacion. UNA_VEZ=1 procesa y termina"
	@echo "  migrar                   alembic upgrade head"
	@echo "  empaquetar               ZIP del complemento de Blender"
	@echo "  test                     unittest de tests/"
	@echo "  test-blender             Empaqueta y ejecuta las dos pruebas de Blender"
	@echo "  lint                     ruff check del repositorio"
	@echo "Base de datos, cinco objetivos:"
	@echo "  db-up                    PostgreSQL, MinIO, Redis, bucket y OIDC de pruebas"
	@echo "  db-down                  Retira contenedores y conserva volumenes"
	@echo "                           ACCION=parar los detiene. ACCION=destruir CONFIRM=ELIMINAR borra volumenes"
	@echo "  db-estado                Salud de PostgreSQL, MinIO y Redis"
	@echo "                           ACCION=logs  ACCION=consola"
	@echo "  db-respaldo FILE=x.dump  Copia metadatos y objetos del bucket"
	@echo "                           ACCION=restaurar FILE=x.dump CONFIRM=RESTAURAR los devuelve"
	@echo "  db-reset CONFIRM=ELIMINAR Recrea ortesislab_dev vacia. Despues, make migrar"

install:
	uv python install 3.14
	uv sync --locked --all-groups
	@$(PYTHON) -c "from pathlib import Path; pares=((Path('apps/db/.env.example'), Path('apps/db/.env')), (Path('.env.example'), Path('.env'))); [print('Copiado', a, 'a', b) or b.write_bytes(a.read_bytes()) for a, b in pares if a.is_file() and not b.exists()]"

up: db-up migrar

web:
	uv run --directory apps/web reflex run

worker:
	uv run python scripts/EjecutarTrabajador.py $(if $(UNA_VEZ),--una-vez,)

migrar:
	uv run alembic upgrade head

empaquetar:
	uv run python scripts/EmpaquetarBlender.py

test:
	uv run python -m unittest discover -s tests -p "test_*.py"

test-blender: empaquetar
	blender --factory-startup --background --python-exit-code 1 --python tests/blender/blender_superficie_abierta.py
	blender --factory-startup --background --python-exit-code 1 --python tests/blender/blender_paquete_zip.py

lint:
	uv run ruff check .

db-up:
	$(PYTHON) scripts/BaseLocal.py up

db-down:
	$(PYTHON) scripts/BaseLocal.py down

db-estado:
	$(PYTHON) scripts/BaseLocal.py estado

db-respaldo:
	$(PYTHON) scripts/BaseLocal.py respaldo

db-reset:
	$(PYTHON) scripts/BaseLocal.py reset
