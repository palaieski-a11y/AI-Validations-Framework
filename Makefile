# Makefile for AI-Validations-Framework

.PHONY: help install install-dev test lint format clean build docs

help:
	@echo "AI-Validations-Framework - Available targets:"
	@echo "  make install       - Install package"
	@echo "  make install-dev   - Install with dev dependencies"
	@echo "  make test          - Run tests"
	@echo "  make lint          - Run linting checks"
	@echo "  make format        - Format code with black"
	@echo "  make clean         - Clean build artifacts"
	@echo "  make build         - Build distribution"
	@echo "  make docs          - Generate documentation"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"
	pip install playwright
	playwright install

test:
	pytest tests/ -v --cov=ai_validations --cov-report=html

test-unit:
	pytest tests/ -v -m "not integration"

test-integration:
	pytest tests/ -v -m "integration"

lint:
	ruff check ai_validations tests
	black --check ai_validations tests
	mypy ai_validations --ignore-missing-imports

format:
	black ai_validations tests
	isort ai_validations tests

clean:
	rm -rf build dist *.egg-info
	rm -rf .pytest_cache .mypy_cache .ruff_cache
	rm -rf htmlcov .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean
	python -m build

docs:
	@echo "Building documentation..."
	mkdir -p docs/_build
	@echo "Documentation ready in docs/GUIDE.md"

run-cli:
	python -m ai_validations.cli --help
