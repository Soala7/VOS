# Service Manager Design

## Purpose

The Service Manager is responsible for registering, storing, and providing access to all major VOS system services.

Instead of the Kernel creating and managing every subsystem directly, it delegates that responsibility to the Service Manager. This keeps the Kernel small, modular, and easier to maintain.

## Why it exists ?

Without a Service Manager, the Kernel would have to keep references to every subsystem.

Like the ;

* FileSystem
* MemoryManager
* ProcessManager
* DriverManager
* NetworkManager
* Logger

As VOS grows, the Kernel would become difficult to maintain.

The Service Manager solves this by acting as a central registry.

## Responsibilities

The Service Manager is responsible for:

* Registering system services.
* Providing access to registered services.
* Checking whether a service exists.
* Removing services when necessary.

The Service Manager does **not** create or initialize services. That responsibility belongs to the BootLoader or Kernel.

## Public Methods

register(name, service)
Registers a new service.

get(name)
Returns a registered service.

exists(name)
Checks whether a service has been registered.

unregister(name)
Removes a registered service.

list_services()
Returns a list of all registered services.

## Services managed by VOS

Initially, the Service Manager will manage:

* Logger
* Configuration Manager
* File System
* Memory Manager
* Process Manager

Future versions may also include:

* Driver Manager
* Network Manager
* Security Manager
* Package Manager
* Desktop Manager
* AI Assistant

## Relationship with the Kernel

BootLoader
↓
Kernel
↓
Service Manager
↓
All system services

The Kernel coordinates the operating system but does not own every subsystem directly.

## Future Improvements

Future versions of the Service Manager may support:

* Automatic dependency resolution
* Service priorities
* Plugin registration
* Lazy loading of services
* Runtime service replacement

## Version

Designed for VOS v0.1.0
Contributions by Soala7
