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
RUN = docker compose run --rm  $(CI_ARGS) $(IMAGE_NAME)

.PHONY: help
help:
	@echo --------------------
	@echo Development Targets:
	@echo ----
	@echo build - Builds the fideslang Docker image.
	@echo ----
	@echo check-all - Run all CI checks
	@echo ----
	@echo clean - Runs Docker commands to clean up the docker local environment.
	@echo ----
	@echo shell - Starts a shell within the container to run CLI commands.
	@echo ----
	@echo docs-serve - Spins up the docs server on localhost:8000
	@echo --------------------

####################
# Dev
####################

.PHONY: shell
shell: build-local
	@echo "Setting up a local development shell... (press CTRL-D to exit)"
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
	@$(RUN) nox -s black

# The order of dependent targets here is intentional
check-all: teardown build-local-prod check-install check-static pytest
	@echo "Running formatter, linter, typechecker and tests..."

check-static:
	@$(RUN) nox -s check_static

check-install:
	@echo "Checking that fideslang is installed..."
	@$(RUN) python -c "import fideslang"

mypy:
	@$(RUN) nox -s mypy

pylint:
	@$(RUN) nox -s pylint

pytest: build-local
	@$(RUN) nox -s tests

xenon:
	@$(RUN) nox -s xenon

####################
# Utils
####################

.PHONY: clean
clean:
	@echo "Doing docker cleanup for this project..."
	@docker compose down --remove-orphans --volumes --rmi all
	@docker system prune --force
	@echo "Clean complete!"

.PHONY: teardown
teardown:
	@echo "Tearing down the dev environment..."
	@docker compose down --remove-orphans
	@echo "Teardown complete"

.PHONY: docs-serve
docs-serve:
	@docker compose build docs
	@docker compose run --rm --service-ports $(CI_ARGS) docs \
	/bin/bash -c "mkdocs serve --dev-addr=0.0.0.0:8000"
