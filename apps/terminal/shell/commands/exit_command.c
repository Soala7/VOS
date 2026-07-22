/*
 * File: VOS/apps/terminal/shell/commands/exit_command.c
 *
 * Implements the exit command.
 */

#include "../include/command.h"
#include "../include/command_result_builder.h"

#include <stdio.h>

static CommandResult exit_execute(int argc, char **argv)
{
    (void)argc;
    (void)argv;


    char *output = result_alloc(64);

    if (output == NULL)
    {
        return result_error("Memory allocation failed.");
    }


    snprintf(
        output,
        64,
        "__VOS_EXIT__"
    );


    return result_success(output);
}



Command exit_command =
{
    .name = "exit",
    .description = "Close the terminal",
    .execute = exit_execute
};