# =========================
# Repo-wide Makefile
# =========================

.PHONY: help test test-go test-python lint fmt clean check

# Default target
help:
	@echo ""
	@echo "Available targets:"
	@echo "  make test         Run all tests (Go + Python)"
	@echo "  make test-go      Run Go tests"
	@echo "  make test-python  Run Python tests"
	@echo "  make lint         Run linters (if installed)"
	@echo "  make fmt          Format code"
	@echo "  make clean        Remove temporary files"
	@echo "  make check        fmt + lint + test"
	@echo ""

# =========================
# Testing
# =========================

test: test-go test-python

test-go:
	@echo "Running Go tests..."
	go test ./...

test-python:
	@echo "Running Python tests..."
	pytest

# =========================
# Formatting
# =========================

fmt:
	@echo "Formatting Go code..."
	gofmt -w .

	@echo "Formatting Python code..."
	black .

# =========================
# Linting
# =========================

lint:
	@echo "Linting Go code..."
	golangci-lint run || echo "golangci-lint not installed, skipping"

	@echo "Linting Python code..."
	flake8 . || echo "flake8 not installed, skipping"

# =========================
# Hygiene
# =========================

clean:
	@echo "Cleaning up..."
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf coverage.out

check: fmt lint test