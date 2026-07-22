/*
 * File: VOS/apps/terminal/shell/include/command_result_builder.h
 *
 * Creates CommandResult objects.
 */

#ifndef COMMAND_RESULT_BUILDER_H
#define COMMAND_RESULT_BUILDER_H

#include "command_result.h"

#include <stddef.h>


/*
 * Allocates memory for command output.
 */
char *result_alloc(size_t size);


/*
 * Creates a successful command result.
 */
CommandResult result_success(char *output);


/*
 * Creates an error command result.
 */
CommandResult result_error(const char *error);


#endif