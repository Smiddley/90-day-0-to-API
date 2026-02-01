
## This repository is a structured, side-by-side Go and Python learning track designed to take a learner from algorithmic fundamentals to production-ready backend engineering in 90 days.

The core constraints are intentional:
- One problem per day
- Every problem is solved in both Go and Python
- No language-specific shortcuts
- Concepts must transfer cleanly to backend systems

This repository is designed for pair learning, review, and CI-driven discipline.

## Who This Is For

- Engineers with a Cloud / Networking background
- Learners transitioning into backend engineering
- Mentors guiding a structured 90-day program
- Anyone who wants algorithmic fluency without “grind culture”

## Learning Philosophy

This project prioritizes systems thinking over syntax.
Algorithms are framed as state management problems.
Data structures map to network control planes.
Performance is treated as a capacity and latency problem.
Backend services are a natural extension, not a new discipline.
If you understand routing tables, NAT, queues, retries, and health checks, you already have most of the intuition needed.

## Daily Workflow

Each day follows the same loop:

- Read the problem description and constraints
- Implement the solution in Python
- Implement the equivalent solution in Go
- Add or update tests
- Commit and open a pull request

## Guidelines:

- One problem per day
- One PR per day
- Small, reviewable changes
- Clarity > cleverness

# Curriculum Overview
## Phase 1 — Foundations (Days 1–14)

### Goal: Align Python and Go mental models.

Topics:

- Program execution and state
- Control flow
- Core data structures
- Functions and contracts

### Cloud / networking intuition:
- Local state vs shared state
- Control plane validation
- Deterministic input → output behavior
## Phase 2 — Algorithmic Patterns (Days 15–45)

### Goal: Learn patterns, not memorization.

Topics:

- Two pointers and sliding windows
- Hash maps as state tables
- Stacks and queues
- Linked lists
- Trees
- Recursion and backtracking

### Cloud / networking intuition:

- TCP flow control
- Packet buffering
- DNS and policy evaluation trees
- Route selection under constraints

## Phase 3 — Performance & Scale Thinking (Days 46–60)

### Goal: Design with constraints and tradeoffs.

Topics:

- Searching and sorting
- Heaps and priority queues
- Graph traversal and cycle detection
- Cloud / networking intuition:
- Prefix matching
- QoS and priority scheduling
- Network topology and dependency graphs

## Phase 4 — Transition to Backend Engineering (Days 61–75)

### Goal: Algorithms become services.

Topics:
- Project structure and tooling
- Error handling, timeouts, and retries
- Data modeling and serialization
- HTTP and REST fundamentals
###Cloud / networking intuition:
- Stateless load balancing
- Idempotent operations
- Control-plane payloads

## Phase 5 — Production Readiness (Days 76–90)

### Goal: Build something that could ship.

Topics:
- FastAPI (Python) and net/http (Go)
- Swagger / OpenAPI contracts
- Persistence and transactions
- Security fundamentals
- Observability and health checks
###Cloud / networking intuition:
- mTLS and identity
- Backpressure
- Readiness vs liveness
- Problem Design

## Each problem is intentionally:
- Language-agnostic
- Solvable without dynamic typing tricks
- Comparable between Go and Python
- Structured like a production system component

## Each problem includes:
- Clear constraints
- A recommended approach
- Time and space complexity
- A cloud or networking analogy

## Testing and CI
- Every solution includes tests
- Go and Python tests run on every push and pull request
- CI enforces correctness and basic hygiene
- The goal is to normalize production discipline early.

## Backend Phase

After Day 60, problems evolve into:

- Converting algorithms into HTTP endpoints
- Validating and serializing input/output
- Mapping errors to status codes
- Introducing persistence and schema design

By the end, algorithms stop feeling academic and start feeling like service internals.

## End State

By Day 90, contributors should be able to:

- Solve most Easy and many Medium algorithm problems
- Translate solutions cleanly between Go and Python
- Design and implement RESTful APIs
- Reason about performance, state, and failure
- Move confidently into cloud-native backend work

## Expectations

This repository values:
- Consistency over speed
- Understanding over memorization
- Reviewable code over clever hacks
- Systems thinking over syntax tricks

## Next Steps

Possible extensions:

- Benchmarking Go vs Python implementations
- Expanding the backend into a full service
- Integrating CI/CD and infrastructure
- Deploying to a cloud environment
<<<<<<< HEAD
=======
# 90-day-0-to-API
Goal: Solve 90 days worth of coding puzzles to learn Python (and Go)
>>>>>>> 118da01 (Initial commit)
=======
>>>>>>> a5759c2 (Update README.md)
