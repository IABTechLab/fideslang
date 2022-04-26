.DEFAULT_GOAL := help

####################
# CONSTANTS
####################
REGISTRY := ethyca
IMAGE_TAG := $(shell git fetch --force --tags && git describe --tags --dirty --always)

# Image Names & Tags
IMAGE_NAME := fideslang
IMAGE := $(REGISTRY)/$(IMAGE_NAME):$(IMAGE_TAG)
IMAGE_LOCAL := $(REGISTRY)/$(IMAGE_NAME):local
IMAGE_LATEST := $(REGISTRY)/$(IMAGE_NAME):latest

# Disable TTY to perserve output within Github Actions logs
# CI env variable is always set to true in Github Actions
ifeq "$(CI)" "true"
    CI_ARGS:=--no-TTY
endif

# Run in Compose
RUN = docker compose run --rm $(ANALYTICS_ID_OVERRIDE) $(CI_ARGS) $(IMAGE_NAME)
RUN_NO_DEPS = docker compose run --no-deps --rm $(ANALYTICS_ID_OVERRIDE) $(CI_ARGS) $(IMAGE_NAME)
START_APP = docker compose up -d $(IMAGE_NAME)

.PHONY: help
help:
	@echo --------------------
	@echo Development Targets:
	@echo ----
	@echo api - Spins up the database and API, reachable on localhost:8080.
	@echo ----
	@echo build - Builds the fidesctl Docker image.
	@echo ----
	@echo check-all - Run all CI checks except for externally dependent ones.
	@echo ----
	@echo clean - Runs Docker commands to clean up the docker local environment.
	@echo ----
	@echo cli - Spins up the database, API, and starts a shell within the API container to run CLI commands.
	@echo ----
	@echo cli-integration - Spins up the CLI with additional containers needed for integration testing.
	@echo ----
	@echo db - Spins up the database, reachable on localhost:5432
	@echo ----
	@echo docs-serve - Spins up the docs server on localhost:8000
	@echo ----
	@echo reset-db - Resets the database back to its freshly initialized state.
	@echo --------------------

####################
# Dev
####################

.PHONY: cli
cli: build-local
	@echo "Setting up a local development shell... (press CTRL-D to exit)"
	@$(START_APP)
	@$(RUN) /bin/bash
	@make teardown

####################
# Docker
####################

build:
	docker build --target=prod --tag $(IMAGE) .

build-local:
	docker build --target=dev --tag $(IMAGE_LOCAL) .

# The production image is used for running tests in CI
build-local-prod:
	docker build --target=prod --tag $(IMAGE_LOCAL) .

push: build
	docker tag $(IMAGE) $(IMAGE_LATEST)
	docker push $(IMAGE)
	docker push $(IMAGE_LATEST)

####################
# CI
####################

black:
	@$(RUN_NO_DEPS) black --check src/

# The order of dependent targets here is intentional
check-all: teardown build-local-prod check-install fidesctl fidesctl-db-scan black \
			pylint mypy xenon pytest-unit pytest-integration
	@echo "Running formatter, linter, typechecker and tests..."

check-install:
	@echo "Checking that fidesctl is installed..."
	@$(RUN_NO_DEPS) fidesctl ${WITH_TEST_CONFIG} --version

.PHONY: fidesctl
fidesctl:
	@$(RUN_NO_DEPS) fidesctl --local ${WITH_TEST_CONFIG} evaluate

fidesctl-db-scan:
	@$(START_APP)
	@$(RUN) fidesctl ${WITH_TEST_CONFIG} scan dataset db \
	"postgresql+psycopg2://postgres:fidesctl@fidesctl-db:5432/fidesctl_test"

mypy:
	@$(RUN_NO_DEPS) mypy

pylint:
	@$(RUN_NO_DEPS) pylint src/

pytest-unit:
	@$(START_APP)
	@$(RUN_NO_DEPS) pytest -x -m unit

pytest-integration:
	@$(START_APP)
	@docker compose run --rm $(CI_ARGS) $(IMAGE_NAME) \
	pytest -x -m integration
	@make teardown

pytest-external:
	@docker compose -f docker-compose.yml -f docker-compose.integration-tests.yml up -d $(IMAGE_NAME)
	@docker compose run \
	-e SNOWFLAKE_FIDESCTL_PASSWORD \
	-e REDSHIFT_FIDESCTL_PASSWORD \
	-e AWS_ACCESS_KEY_ID \
	-e AWS_SECRET_ACCESS_KEY \
	-e AWS_DEFAULT_REGION \
	-e OKTA_CLIENT_TOKEN \
	--rm $(CI_ARGS) $(IMAGE_NAME) \
	pytest -x -m external
	@make teardown

xenon:
	@$(RUN_NO_DEPS) xenon src \
	--max-absolute B \
	--max-modules B \
	--max-average A \
	--ignore "data, tests, docs" \
	--exclude "src/fidesctl/_version.py"

####################
# Utils
####################

.PHONY: clean
clean:
	@echo "Doing docker cleanup for this project..."
	@docker compose -f docker-compose.yml -f docker-compose.integration-tests.yml down --remove-orphans --volumes --rmi all
	@docker system prune --force
	@echo "Clean complete!"

.PHONY: teardown
teardown:
	@echo "Tearing down the dev environment..."
	@docker compose -f docker-compose.yml -f docker-compose.integration-tests.yml down --remove-orphans
	@echo "Teardown complete"

.PHONY: docs-build
docs-build: build-local
	@docker compose run --rm $(CI_ARGS) $(IMAGE_NAME) \
	python generate_docs.py docs/fides/docs/

.PHONY: docs-serve
docs-serve: docs-build
	@docker compose build docs
	@docker compose run --rm --service-ports $(CI_ARGS) docs \
	/bin/bash -c "pip install -e /fides && mkdocs serve --dev-addr=0.0.0.0:8000"
