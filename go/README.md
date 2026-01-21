High-level purpose

The go/ subtree exists to answer this question:

“How do we keep Go code module-safe, testable, and production-shaped while solving daily problems?”

Unlike Python, Go already enforces discipline — but only within a module boundary. The subtree creates and protects that boundary.

go/ — the Go module root

This directory is the module root, not just an organizational folder.

Why this matters:

go.mod applies recursively

Imports are resolved relative to the module path

Tooling (go test, go vet, gofmt) assumes module context

Putting Go code at repo root would:

Pollute imports

Collide with Python tooling

Make future backend work harder

Analogy:
This is the service root — like a microservice repo inside a mono-repo.

go.mod

What it is:
The authoritative declaration of:

Module path

Go version

External dependencies

Example:

module github.com/your-org/leetcode-dual-lang/go

go 1.22


Why it exists even early:

Locks compiler behavior

Makes builds reproducible

Enables CI and dependency caching

Unlike Python, Go cannot function sanely without this.

Analogy:
This is your Terraform provider block + module source combined.

go.sum

What it is:
A cryptographic lockfile.

What it guarantees:

Dependency integrity

Reproducible builds

Supply-chain safety

You never edit this manually.

Analogy:
This is your checksum-verified artifact store.

cmd/

This is one of Go’s most important conventions.

Rule of thumb:

Anything under cmd/ is executable.

Why this matters:

Clean separation between libraries and binaries

Multiple entrypoints can coexist

Scales naturally into services and CLIs

Example later:

cmd/
 ├── day01/
 │   └── main.go
 └── api/
     └── main.go


Analogy:
These are your service entrypoints — like ECS tasks or Kubernetes Deployments.

cmd/dayXX/main.go

Purpose:
A runnable implementation of that day’s problem.

Why not put logic directly in main.go?
Because:

It becomes untestable

It encourages monolithic functions

It doesn’t scale to backend work

Instead:

main.go wires inputs → outputs

Logic lives elsewhere

Analogy:
This is your HTTP handler / Lambda entrypoint, not your business logic.

internal/

This is a Go-specific superpower.

Anything under internal/:

Cannot be imported outside this module

Enforces architectural boundaries at compile time

That means:

No accidental reuse

No tight coupling

No “just import it” shortcuts

Analogy:
This is network-level isolation, enforced by the compiler.

internal/solutions/

This is where the actual problem logic lives.

Structure:

internal/solutions/day01.go
internal/solutions/day02.go


Why this is correct:

Logic is testable

Logic is reusable

Logic is independent of I/O

Analogy:
This is your core service logic, behind a private API.

internal/solutions/dayXX.go

Example:

package solutions

func TwoSum(nums []int, target int) []int {
    ...
}


Why this matters:

Pure functions

Deterministic

Easy to benchmark

Easy to reuse later in APIs

This mirrors how backend handlers call service layers.

internal/solutions/dayXX_test.go

Go’s testing model shines here.

Benefits:

Tests live next to code

go test ./... just works

Table-driven tests are natural

Example:

func TestTwoSum(t *testing.T) {
    tests := []struct {
        nums   []int
        target int
        want   []int
    }{...}
}


Analogy:
These are contract tests, not ad-hoc scripts.

pkg/ (optional, later)

This folder is intentionally empty or absent early.

Rule:

If something goes in pkg/, you are promising it’s reusable outside this module.

You do not want this early.
Most logic belongs in internal/.

Analogy:
This is a public API surface — dangerous to expose too soon.

README.md (inside go/)

Purpose:

Go version expectations

How to run tests

How to build binaries

Not redundant — scoped documentation again.

Why this layout is “production-shaped”

This exact structure maps cleanly to:

REST APIs (Fiber / Gin / net/http)

gRPC services

CLIs

Lambda-style handlers

When you pivot to backend work:

cmd/api/main.go becomes the server

internal/handlers/ appears naturally

internal/services/ holds business logic

Your daily problem patterns still apply

Nothing is thrown away.