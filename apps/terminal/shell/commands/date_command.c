/*
 * File: VOS/apps/terminal/shell/commands/date_command.c
 *
 * Implements the date command.
 */

#include "../include/command.h"
#include "../include/command_result_builder.h"

#include <stdio.h>
#include <time.h>
#include <stdlib.h>


static CommandResult date_execute(int argc, char **argv)
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
        "%02d-%02d-%04d",
        local_time->tm_mday,
        local_time->tm_mon + 1,
        local_time->tm_year + 1900
    );


    return result_success(output);
}



Command date_command =
{
    .name = "date",
    .description = "Display the current date",
    .execute = date_execute
};