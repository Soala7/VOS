/*
 * File: ls_command.c
 *
 * Implements the ls command.
 */

#include "../include/command.h"
#include "../include/command_result_builder.h"
#include "../include/host.h"

#include <string.h>


static CommandResult ls_execute(
    int argc,
    char **argv
)
{
    const char *path = NULL;


    if (argc > 1)
    {
        path = argv[1];
    }


    char result[4096];


    host_ls(
        path,
        result,
        sizeof(result)
    );


    char *output = result_alloc(
        strlen(result) + 1
    );


    if (output == NULL)
    {
        return result_error(
            "Memory allocation failed."
        );
    }


    strcpy(
        output,
        result
    );


    return result_success(output);
}



Command ls_command =
{
    .name = "ls",
    .description = "List directory contents",
    .execute = ls_execute
};