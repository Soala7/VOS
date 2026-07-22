/*
 * File: VOS/apps/terminal/shell/commands/time_command.c
 *
 * Implements the time command.
 */

#include "../include/command.h"
#include "../include/command_result_builder.h"

#include <stdio.h>
#include <stdlib.h>
#include <time.h>



static CommandResult time_execute(int argc, char **argv)
{
    (void)argc;
    (void)argv;


    char *output = result_alloc(128);

    if (output == NULL)
    {
        return result_error("Memory allocation failed.");
    }


    time_t current_time = time(NULL);

    struct tm *local_time = localtime(&current_time);


    if (local_time == NULL)
    {
        free(output);

        return result_error("Unable to get system time.");
    }


    snprintf(
        output,
        128,
        "%02d:%02d:%02d",
        local_time->tm_hour,
        local_time->tm_min,
        local_time->tm_sec
    );


    return result_success(output);
}



Command time_command =
{
    .name = "time",
    .description = "Display the current time",
    .execute = time_execute
};