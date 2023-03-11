# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


# --------- Development commands ---------

format: # Format code and sort imports
	poetry run black docker_compose_diagram tests
	poetry run isort docker_compose_diagram tests

lint: # Run code quality tools
	# Check pep8 style
	poetry run flake8 docker_compose_diagram tests
	# Check imports order
	poetry run isort docker_compose_diagram tests --check-only
	# Check code security issues
	poetry run bandit -r docker_compose_diagram

safety:
	# Check security issues with installed packages
	poetry run safety check

# Prevent running a file with same name
.PHONY: test
test: # Run tests
	poetry run pytest tests


# --------- GitHub Actions CI ---------

# Prevent running a file with same name
ci.test: # Run ci tests
	poetry run pytest tests


ci.lint: # Run code quality tools inside ci
	# Check pep8 style
	poetry run flake8 docker_compose_diagram
	# Check imports order
	poetry run isort docker_compose_diagram --check-only
	# Check code security issues
	poetry run bandit -r docker_compose_diagram


