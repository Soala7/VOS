/*
 * File: VOS/apps/terminal/shell/commands/clear.c
 *
 * Implements the clear command.
 */

#include "../include/command.h"

#include <stdlib.h>
#include <string.h>


static CommandResult clear_execute(int argc, char **argv)
{
    (void)argc;
    (void)argv;


    CommandResult result;

    result.success = 1;
    result.exit_code = 0;
    result.error = NULL;

    /*
     * Special token understood by the future VOS terminal UI.
     * The C shell itself does not clear the host terminal.
     */
    result.output = strdup("__VOS_CLEAR__");


    return result;
}

Command clear_command =
{
    .name = "clear",
    .description = "Clear the terminal screen",
    .execute = clear_execute
};