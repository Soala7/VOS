/*
 * File: VOS/apps/terminal/shell/commands/touch_command.c
 *
 * Implements touch command.
 */


#include "../include/command.h"
#include "../include/command_result_builder.h"
#include "../include/host.h"



static CommandResult touch_execute(
    int argc,
    char **argv
)
{
    if (argc < 2)
    {
        return result_error(
            "Usage: touch <file>"
        );
    }



    int success = host_touch(
        argv[1]
    );



    if (success)
    {
        return result_success(
            "File created."
        );
    }



    return result_error(
        "Failed to create file."
    );
}




Command touch_command =
{
    .name = "touch",
    .description = "Create a file",
    .execute = touch_execute
};