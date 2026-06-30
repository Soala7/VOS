# VOS Event Bus

## Overview

The Event Bus is the internal communication system of VOS.  
It allows different components of the system to communicate without direct dependencies.

Instead of systems calling each other directly, they emit and listen to events.

## Core Concept

VOS uses a **Publish–Subscribe (Pub/Sub)** model:

- Publishers emit events
- Subscribers listen for events
- The Event Bus connects both

## Why It Exists

Without the Event Bus:
- Systems become tightly coupled
- Kernel becomes complex
- Hard to scale or modify subsystems

With the Event Bus:
- Systems remain independent
- Communication is centralized
- Architecture becomes modular and scalable

## Event Flow

1. A system emits an event
2. Event Bus receives it
3. Event Bus finds listeners
4. Listeners are executed

## Example Events

- `boot_complete`
- `file_created`
- `file_deleted`
- `process_started`
- `process_terminated`
- `user_login`

## Event Structure

All events follow this format:
{
    "name": "event_name",
    "data": {},
    "source": "system_name"
}

## Subscription Model

Systems register listeners like:
event_bus.subscribe("file_created", handler_function)

## Emitting Events

Systems emit events like:
event_bus.emit("file_created", {
    "path": "/home/user/file.txt"
})

## System Integration

* Kernel registers Event Bus during boot
* Core services use Event Bus for communication
* Desktop listens for system-level events
* Applications emit events instead of direct calls

## Design Rules

* No direct system-to-system communication
* All communication goes through Event Bus
* Events must be lightweight and structured
* Event Bus must not depend on high-level systems

## Role in VOS Architecture

The Event Bus is part of the `core/` layer:

core/
├── service_manager.py
├── logger.py
├── event_bus.py

It is a foundational system service used by all other components.



