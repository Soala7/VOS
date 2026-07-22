/*
 * File: VOS/apps/terminal/shell/commands/version_command.c
 *
 * Implements the version command.
 */

#include "../include/command.h"
#include "../include/command_result_builder.h"
#include "../include/version.h"

#include <stdio.h>


static CommandResult version_execute(int argc, char **argv)
{
    (void)argc;
    (void)argv;


    char *output = result_alloc(256);

    if (output == NULL)
    {
        return result_error("Memory allocation failed.");
    }


    snprintf(
        output,
        256,
        "%s %s (%s)",
        vos_name(),
        vos_version(),
        vos_build()
    );


    return result_success(output);
}


Command version_command =
{
    .name = "version",
    .description = "Display the Gorgon OS version",
    .execute = version_execute
};