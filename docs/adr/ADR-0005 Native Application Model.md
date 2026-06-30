# ADR-0005: Native Application Model

## Status

Accepted

---

## Context

VOS requires a consistent application model that defines how software runs inside the system.

Applications must be independent of the host operating system while still being able to interact with VOS services.

---

## Decision

We define three application types:

### 1. Native VOS Applications

Applications written specifically for VOS that run inside VOS Processes and use VOS APIs.

Examples:

* Browser
* Terminal
* Explorer
* Calculator
* Games

---

### 2. Wrapped Host Applications

Applications executed from the host operating system but managed within the VOS Desktop environment.

---

### 3. Packaged VOS Applications (Future)

Installable applications distributed through a VOS package system.

---

## Application Rules

* Applications must run inside VOS Processes.
* Applications must not access Kernel internals directly.
* Applications must communicate through Runtime services.
* Applications must use Event Bus for communication.

---

## Consequences

### Positive

* Consistent application lifecycle
* Extensible ecosystem
* Clear separation of concerns
* Future package management support

### Negative

* Increased abstraction complexity
* Requires application wrapper layer

---

## Alternatives Considered

### 1. Direct host application execution

Rejected due to lack of control and inconsistency.

### 2. No formal application model

Rejected due to architectural inconsistency.

---

## Summary

The Native Application Model defines how applications operate inside VOS, ensuring consistency, modularity, and long-term scalability.
