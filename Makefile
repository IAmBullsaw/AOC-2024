# Makefile for creating daily Python script and running tests

# Declare targets as phony to prevent conflicts with potential file names
.PHONY: day test

# Helper function to pad single-digit numbers with zero
pad_day = $(shell printf "%02d" $(1))

# Rule to create a daily Python script
day:
	$(eval DAY := $(if $(word 2,$(MAKECMDGOALS)),$(word 2,$(MAKECMDGOALS)),$(shell date +%d)))
	$(eval DAY_PADDED := $(call pad_day,$(DAY)))
	@if [ ! -f $(DAY_PADDED).py ]; then \
		cp template.py $(DAY_PADDED).py && \
		echo "Created $(DAY_PADDED).py"; \
	else \
		echo "Error: $(DAY_PADDED).py already exists. Not overwriting."; \
		exit 1; \
	fi

# Rule to run tests for a specific day
test:
	$(eval DAY := $(if $(word 2,$(MAKECMDGOALS)),$(word 2,$(MAKECMDGOALS)),$(shell date +%d)))
	$(eval DAY_PADDED := $(call pad_day,$(DAY)))
	$(eval TEST_NUM := $(word 3,$(MAKECMDGOALS)))
	@if [ -z "$(TEST_NUM)" ]; then \
		python3 $(DAY_PADDED).py --tests; \
	else \
		python3 $(DAY_PADDED).py --test$(TEST_NUM); \
	fi

# Dummy targets to prevent make from complaining about arguments
%:
	@:

