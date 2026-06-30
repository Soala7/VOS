# ADR-0001: Use a Service Manager

- Status: Accepted
- Date: 2026-06-30

## Context

VOS is being designed as a modular operating-system-inspired project. The kernel and higher-level components need a reliable way to access shared infrastructure such as logging, configuration, the event bus, filesystem services, and process management.

If these services are managed directly by the kernel, the kernel becomes tightly coupled to many subsystems and becomes harder to maintain as the system grows.

## Decision

VOS will use a Service Manager as a central registry for system services.

The Service Manager will:

- register services by name
- provide access to registered services
- check whether a service exists
- allow services to be removed or replaced when needed

The kernel will coordinate the system, but it will delegate service lookup and registration to the Service Manager rather than owning every subsystem directly.

## Rationale

This approach improves modularity and keeps the kernel focused on orchestration instead of direct implementation details. It also makes the system easier to test, extend, and evolve as new services are introduced.

## Alternatives Considered

1. Kernel-managed services
   - Simpler at first, but creates strong coupling and makes the kernel harder to scale.

2. Global singleton access
   - Easy to implement, but leads to hidden dependencies and poor testability.

3. Dependency injection only
   - Flexible, but more cumbersome for a system that needs a shared service registry.

## Consequences

### Positive

- reduced coupling between kernel and subsystems
- cleaner separation of responsibilities
- easier service discovery and extension
- better foundation for future runtime and plugin-style features

### Trade-offs

- introduces an additional layer of indirection
- requires explicit registration of services during initialization

## Related Documents

- [docs/architecture/ServiceManager.md](../architecture/ServiceManager.md)
- [core/services_manager.py](../../core/services_manager.py)
