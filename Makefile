OS := $(shell uname -s)

ifeq ($(OS),Linux)
    DEPS_CMD := python3 -m pip install -r analysis/api/requirements.txt
else
    DEPS_CMD := python -m pip install -r analysis/api/requirements.txt
endif

deps:
	$(DEPS_CMD)
run :
	python3 analysis/api/main.py
website:
	open analysis/app/index.html