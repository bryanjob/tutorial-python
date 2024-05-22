.PHONY: lint

LINT_CMD = pylint
VC_CMD = git

PY_FILE_LIST ?= $(if $(LINT_ALL), \
	$(shell find * -type f -iname '*.py'), \
	$(shell $(VC_CMD) diff --name-only --diff-filter=d HEAD^ | grep -E '*.py'))

lint:
#	@echo "${PY_FILE_LIST}"
	$(LINT_CMD) $(PY_FILE_LIST)
