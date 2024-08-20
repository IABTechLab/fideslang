FROM python:3.9-slim-bullseye as base

# Update pip in the base image since we'll use it everywhere
RUN pip install -U pip

#######################
## Tool Installation ##
#######################

FROM base as builder

RUN : \
    && apt-get update \
    && apt-get install \
    -y --no-install-recommends \
    curl \
    git \
    make \
    vim \
    g++ \
    gnupg \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

#########################
## Python Dependencies ##
#########################

COPY dev-requirements.txt dev-requirements.txt
RUN pip install -r dev-requirements.txt

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

###############################
## General Application Setup ##
###############################

COPY . /fideslang
WORKDIR /fideslang

# Immediately flush to stdout, globally
ENV PYTHONUNBUFFERED=TRUE

# Enable detection of running within Docker
ENV RUNNING_IN_DOCKER=TRUE

###################################
## Application Development Setup ##
###################################

FROM builder as dev

# Install fideslang as a symlink
RUN pip install -e ".[all]"

##################################
## Production Application Setup ##
##################################

FROM builder as prod

# Install without a symlink
RUN python -m pip install build
RUN python -m build
RUN pip install dist/fideslang-*.tar.gz
