# Coding Standards

## General Principles

- Keep code modular and easy to understand.
- Prefer clear names over clever implementations.
- Separate core logic, UI components, and runtime behavior into distinct modules.
- Write tests for new functionality whenever practical.

## Python Conventions

- Use descriptive function and class names.
- Keep functions focused on a single responsibility.
- Follow PEP 8 formatting where possible.
- Use docstrings for public classes and functions.
- Avoid unnecessary dependencies.

## Project Structure

- Keep kernel-related code under the kernel package.
- Keep shared infrastructure under the core package.
- Keep application entry points under the apps package.
- Keep desktop UI modules under the desktop package.

## Documentation

- Update documentation when architecture, behavior, or interfaces change.
- Keep ADRs and design docs aligned with the codebase.
