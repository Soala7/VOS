/*
 * File: VOS/apps/terminal/shell/include/command.h
 *
 * Defines a shell command.
 */

#ifndef COMMAND_H
#define COMMAND_H

#include "command_result.h"


typedef CommandResult (*CommandFunction)(int argc, char **argv);


typedef struct
{
    char *name;

    char *description;

    CommandFunction execute;

} Command;

#endif