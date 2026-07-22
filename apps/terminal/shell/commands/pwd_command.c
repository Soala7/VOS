/*
 * File: VOS/apps/terminal/shell/commands/pwd_command.c
 *
 * Implements the pwd command.
 */

#include "../include/command.h"
#include "../include/command_result_builder.h"
#include "../include/cwd.h"
#include "../include/host.h"
#include <stdio.h>


static CommandResult pwd_execute(int argc, char **argv)
{
    (void)argc;
    (void)argv;


    char *output = result_alloc(256);

    if (output == NULL)
    {
        return result_error("Memory allocation failed.");
    }


    char path[256];

    host_pwd(
        path,
        sizeof(path)
    );


    snprintf(
        output,
        256,
        "%s",
        path
    );


        return result_success(output);
    }



Command pwd_command =
{
    .name = "pwd",
    .description = "Display the current working directory",
    .execute = pwd_execute
};