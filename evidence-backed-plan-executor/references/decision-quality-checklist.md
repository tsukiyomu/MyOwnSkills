# Decision Quality Checklist

Read this checklist for material architecture, concurrency, consistency, persistence, security, dependency, or CI-gate decisions. Apply only relevant questions; do not add complexity solely to satisfy the checklist.

## Problem evidence

- What user-visible or system risk is being controlled?
- Which repository evidence proves the risk or gap exists?
- What are the business and technical invariants?
- What scale, latency, durability, and availability requirements are confirmed?
- Which requirements are assumptions rather than measured facts?
- What is explicitly outside this work unit?

## Existing architecture

- Where does the workflow enter and terminate?
- Which component owns the state being changed?
- What is the authoritative source of truth?
- Where are transaction, retry, timeout, and cancellation boundaries?
- What existing mechanism can solve the problem before introducing a new component?
- Which operational constraints already exist in deployment and CI?

## Alternatives

- What is the smallest viable solution?
- What are at least two realistic alternatives for a material decision?
- What does each option optimize: correctness, latency, throughput, simplicity, cost, or operability?
- Which new failure modes and operational responsibilities does each option introduce?
- Under what conditions would each option be the better choice?

## Distributed state and concurrency

- What happens under duplicate, reordered, delayed, or lost requests or messages?
- Is the operation atomic at the required boundary?
- Is idempotency required, and where is its key stored?
- Can retries repeat a successful side effect?
- What happens during partial success between two systems?
- How are reconciliation and compensation performed?
- What does fail-open or fail-closed mean for this operation?
- Are consistency guarantees stated precisely rather than described as simply "safe"?

For Redis or Lua proposals, additionally check:

- Why is a database conditional update, lock, or queue insufficient?
- Does the Lua script touch keys that share a Redis Cluster hash slot?
- Is Redis authoritative, a cache, or a reservation layer?
- What happens after Redis success and database failure?
- How are script timeout, failover, and ambiguous client results handled?
- How are durability, expiry, reconciliation, and capacity limits verified?

## Implementation mapping

- Which exact files, symbols, interfaces, schemas, or workflow steps change?
- Which behavior remains unchanged?
- Does every material invariant map to an assertion or other evidence?
- Are mocks or stubs placed at an intentional dependency boundary?
- Does the implementation introduce configuration, migration, rollback, or observability work?

## Verification

- What is the lowest-cost deterministic proof?
- What integration boundary requires a more authentic dependency?
- Has success, expected failure, retry, and recovery behavior been considered?
- Can a failed run preserve enough evidence to diagnose the failure?
- What does the test result not prove?
- Is a CI check diagnostic, blocking, scheduled, or manual, and who owns that decision?

## Learning transfer

- Can the user explain the invariant before naming the technology?
- Can the user compare the selected solution with a simpler alternative?
- Can the user identify the most dangerous failure mode?
- Can the user point from a requirement to production code, test assertion, and execution evidence?
- Can the user state a condition that would invalidate the design?

Treat an implementation as delivered when its acceptance evidence passes. Treat knowledge as mastered only when the user can explain or apply the method independently.
