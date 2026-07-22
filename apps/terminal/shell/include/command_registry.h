/*
 * File: VOS/apps/terminal/shell/include/command_registry.h
 *
 * Defines the command registry interface.
 */

#ifndef COMMAND_REGISTRY_H
#define COMMAND_REGISTRY_H

#include "command.h"


/*
 * Initializes the command registry.
 */
void registry_init(void);


/*
 * Registers a command.
 */
int registry_register(Command *command);


/*
 * Finds a command by name.
 */
Command *registry_find(const char *name);


/*
 * Returns the number of registered commands.
 */
int registry_count(void);


/*
 * Returns a command by index.
 */
Command *registry_get(int index);


#endif