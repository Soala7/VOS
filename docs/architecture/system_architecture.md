# System Architecture

## Overview

VOS (Virtual Operating System) is a user-space operating system built in Python that runs on top of a host operating system. It provides a full virtual operating environment including a Kernel, Runtime, File System, Desktop Environment, and Applications.

The system is designed to behave like a real operating system while remaining cross-platform and portable.

---

# High-Level Architecture

```text id="sysarch1"
Host Operating System
        │
        ▼
Python Runtime
        │
        ▼
VOS Core Layer
        │
├── Kernel
├── Runtime
├── Services
├── Event Bus
├── Logger
├── File System
│
└── Desktop Environment
        │
        ▼
Applications
```

---

# System Layers

## 1. Host Layer

The host operating system provides:

* CPU scheduling
* Memory allocation
* File I/O
* Networking
* Device access
* Process execution

VOS does not replace these functions. It uses them as the execution base.

---

## 2. Core Layer

The Core Layer includes:

* Kernel
* Service Manager
* Event Bus
* Logger
* Configuration Manager

This layer forms the foundation of VOS and initializes all system services.

---

## 3. Runtime Layer

The Runtime Layer is responsible for:

* Managing application lifecycle
* Managing processes
* Managing user sessions
* Coordinating system startup
* Launching the Desktop

---

## 4. Desktop Layer

The Desktop Layer provides:

* Window management
* Taskbar
* Start menu
* Icons
* User interface rendering

This layer is fully decoupled from the Kernel.

---

## 5. Application Layer

Applications run inside VOS Processes and include:

* Native VOS applications
* System tools
* Games
* Future packaged applications

---

# Data Flow

1. User interacts with Desktop.
2. Desktop sends events to Runtime.
3. Runtime manages processes and applications.
4. Kernel provides system services.
5. File System handles data storage.
6. Event Bus coordinates communication.

---

# Design Principles

* Separation of concerns
* Modular architecture
* Event-driven communication
* Platform independence
* Extensibility
* Maintainability

---

# Future Expansion

* Plugin system
* Package manager
* Multi-user support
* Virtual networking layer
* Sandboxed execution environments

---

# Summary

The System Architecture defines the full structure of VOS as a layered virtual operating system running on top of a host OS. It separates responsibilities into Core, Runtime, Desktop, and Application layers to ensure scalability and maintainability.
