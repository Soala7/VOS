/*
 * File: mkdir_command.c
 *
 * Implements mkdir command.
 */

#include "../include/command.h"
#include "../include/command_result_builder.h"
#include "../include/host.h"


static CommandResult mkdir_execute(
    int argc,
    char **argv
)
{
    if (argc < 2)
    {
        return result_error(
            "Usage: mkdir <directory>"
        );
    }


    int success = host_mkdir(
        argv[1]
    );


    if (success)
    {
        return result_success(
            "Directory created."
        );
    }


    return result_error(
        "Failed to create directory."
    );
}



Command mkdir_command =
{
    .name = "mkdir",
    .description = "Create a directory",
    .execute = mkdir_execute
};