/*
 * File: cd_command.c
 *
 * Implements the cd command.
 */

#include "../include/command.h"
#include "../include/command_result_builder.h"
#include "../include/host.h"

#include <string.h>


static CommandResult cd_execute(
    int argc,
    char **argv
)
{
    if (argc < 2)
    {
        return result_error(
            "Usage: cd <directory>"
        );
    }


    int success = host_cd(
        argv[1]
    );


    if (success)
    {
        return result_success("");
    }


    return result_error(
        "Directory not found."
    );
}



Command cd_command =
{
    .name = "cd",
    .description = "Change current directory",
    .execute = cd_execute
};