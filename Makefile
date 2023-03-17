# inspired by https://github.com/idealo/shalmaneser-parquet-file-merge/blob/main/Makefile
# and https://github.com/idealo/die-monte-carlo-dq/blob/main/Makefile

PYTHON = python3
PYENV_VERSION = 3.9.13
VENV = .venv
APP_NAME = "example-app"

.PHONY: all
DEFAULT_GOAL: setup

setup: get_pyenv venv

venv: $(VENV)/touchfile # wrapper for the one below

get_pyenv:
	@echo "installing pyenv via homebrew and python$(PYENV_VERSION)"
	brew install pyenv
	pyenv install -v $(PYENV_VERSION) || true # to avoid cancelling the recipe if existing

# only when requirements change: https://stackoverflow.com/questions/24736146/how-to-use-virtualenv-in-makefile
.ONESHELL:
$(VENV)/touchfile: requirements.txt requirements-dev.txt
	@pyenv local $(PYENV_VERSION) || { echo "!!! no python $(PYENV_VERSION) found run 'make get_pyenv' to install it"; exit 1; }
	@echo "Creating virtual environment and installing dependencies in $(VENV) using python $(PYENV_VERSION)"
	$(PYTHON) -m venv $(VENV)
	. $(VENV)/bin/activate && pip install --upgrade pip \
	&& pip install -r requirements.txt && pip install -r requirements-dev.txt
	@touch $(VENV)/touchfile
	rm -rf .python-version


update: # to force the upper
	. $(VENV)/bin/activate && pip install --upgrade pip \
	&& pip install -r requirements.txt && pip install -r requirements_dev.txt

cleanup:
	@echo "Cleaning up the envs / temps."
	@rm -rf $(VENV)/
	# TODO more to be deleted?

open_history_server:
	open "http://localhost:4040/"

# # docker part
# d_init:
# 	brew install --cask docker && \
# 	docker run hello-world && \
# 	echo "we are set :)"

# d_start:
# 	open -a docker
# 	echo "we are set :)"

# d_build:
# 	docker build . -t $(APP_NAME)

# d_run: d_build
# 	docker run -d -p 5000:5000 $(APP_NAME)

# d_list:
# 	docker ps

# d_kill:
# 	docker kill $$(docker ps | grep $(APP_NAME) | cut -d" " -f 1)

# d_ssh:
# 	docker exec -it $$(docker ps | grep $(APP_NAME) | cut -d" " -f 1) bash

# d_ssh_root:
# 	docker exec -it -u root $$(docker ps | grep $(APP_NAME) | cut -d" " -f 1) bash

# d_clean_all: d_clean_images d_clean_containers d_clean_volumes

# d_clean_images:
# 	docker image prune -a

# d_clean_containers:
# 	docker container prune

# d_clean_volumes:
# 	docker system prune --volumes
