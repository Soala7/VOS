/*
 * File: VOS/apps/terminal/shell/include/shell.h
 *
 * Defines the main shell interface.
 */

#ifndef SHELL_H
#define SHELL_H

#include "command_registry.h"


/* Executes a command line entered by the user. */
CommandResult shell_execute(char *input);


#endif