High-level purpose

That python/ subtree exists to answer one question:

“How do we keep Python code organized, testable, and production-shaped as the repo grows?”

Even though daily problems live under problems/, Python still needs:

A dependency boundary

A shared utilities location

A place CI can reason about “the Python project”

This mirrors how Go has go.mod at the repo root.

Breakdown, line by line
python/

This is the Python project root.

Why this matters:

CI needs a stable place to install dependencies from

Tools like pytest, black, and mypy expect a project boundary

Prevents Python tooling from crawling the entire repo indiscriminately

Think of this as the Python control plane.

pyproject.toml

What it is:
The modern, canonical configuration file for Python projects.

What it replaces (over time):

setup.py

Tool-specific config files (setup.cfg, .flake8, etc.)

Why you want it even early:

Central place for tool configuration (formatter, linter, test runner)

Future-proof (PEP 517 / 518)

Required if you ever package or publish anything

Analogy (Cloud):
This is your service manifest — like a Helm chart or Terraform module metadata.

Even if it’s mostly empty at first, it establishes structure and intent.

requirements.txt

What it is:
A flat list of runtime and dev dependencies.

Why it still exists alongside pyproject.toml:

Simple

Universally understood

Works cleanly with GitHub Actions

Easy for beginners

Example contents later:

pytest
fastapi
uvicorn


Analogy:
This is your AMI / container dependency list — explicit, reproducible, boring (in a good way).

src/

This is a deliberate best practice, not cosmetic.

Why not put code directly under python/?
Because Python will otherwise:

Accidentally import from the repo root

Mask dependency issues

Behave differently locally vs CI

Using src/ forces:

Explicit imports

Realistic module resolution

Fewer “works on my machine” bugs

Analogy:
This is like separating runtime containers from infra code.

src/common/

This is for shared Python utilities, not problem solutions.

What goes here:

Test helpers

Shared fixtures

Common validation helpers

Later: auth helpers, serialization helpers

What does not go here:

Daily problem solutions

One-off logic

Why this matters:
Without this, you’ll start copy-pasting helper code across problems.
That’s technical debt by Day ~12.

Analogy:
This is your shared library, like a VPC module or IAM policy bundle.

src/common/__init__.py

What it does:
Marks common as a Python package.

Why it still exists in 2025:

Explicit is better than implicit

Makes imports predictable

Avoids edge cases with tooling

Even if it’s empty, it’s a contract.

src/common/test_helpers.py

Purpose:
A single place for:

Assertion helpers

Shared test data builders

Reusable test utilities

Example later:

def assert_lists_equal(a, b):
    assert sorted(a) == sorted(b)


This prevents:

Repeating the same test logic in 90 folders

Tests diverging in style and rigor

Analogy:
This is your test harness, like synthetic traffic generators in networking.

README.md (inside python/)

Purpose:
Human-facing documentation for:

How Python tests are run

How dependencies are installed

Any Python-specific conventions

This is not redundant with the repo README.
It’s scoped documentation.

Analogy:
This is a service-specific runbook, not the architecture doc.

Why this exists even though problems live elsewhere

You might be thinking:

“But all the real code is under problems/ — why do this now?”

Because:

Tooling needs a stable anchor

CI needs predictable paths

You’re teaching production habits, not scripts

This layout prevents:

Import hell

Dependency sprawl

CI flakiness

Bad habits forming early