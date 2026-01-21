# Stop on error
$ErrorActionPreference = "Stop"

Write-Host "Initializing repository structure..."

# Helper functions
function Ensure-Dir {
    param (
        [Parameter(Mandatory)]
        [string]$Path
    )

    if (-not (Test-Path $Path)) {
        New-Item -ItemType Directory -Path $Path | Out-Null
        Write-Host "Created directory: $Path"
    }
}

function Ensure-File {
    param (
        [Parameter(Mandatory)]
        [string]$Path,
        [string]$Content = ""
    )

    if (-not (Test-Path $Path)) {
        $Content | Out-File -FilePath $Path -Encoding utf8
        Write-Host "Created file: $Path"
    }
}

# Root-level files (no README)
Ensure-File "CONTRIBUTING.md"
Ensure-File ".editorconfig"
Ensure-File ".gitignore"
Ensure-File "Makefile"

# GitHub workflows
Ensure-Dir ".github/workflows"
Ensure-File ".github/workflows/go.yml"
Ensure-File ".github/workflows/python.yml"
Ensure-File ".github/workflows/lint.yml"

# Problems root
Ensure-Dir "problems"

# Python structure
Ensure-Dir "python"
Ensure-Dir "python/src"
Ensure-Dir "python/src/common"
Ensure-File "python/requirements.txt"
Ensure-File "python/pyproject.toml"
Ensure-File "python/src/common/test_helpers.py"

# Go structure
Ensure-Dir "go"
Ensure-Dir "go/internal"
Ensure-Dir "go/internal/common"
Ensure-Dir "go/internal/common/testhelpers"
Ensure-File "go/go.mod"
Ensure-File "go/go.sum"
Ensure-File "go/internal/common/testhelpers/helpers.go"

# Backend structure
Ensure-Dir "backend"
Ensure-Dir "backend/python"
Ensure-Dir "backend/python/fastapi"
Ensure-Dir "backend/go"
Ensure-Dir "backend/go/nethttp"

Write-Host "Repository structure initialized successfully."
