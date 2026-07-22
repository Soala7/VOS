/*
 * File: VOS/apps/terminal/shell/commands/echo.c
 *
 * Implements the echo command.
 */

#include "../include/command.h"

#include <stdlib.h>
#include <string.h>


static CommandResult echo_execute(int argc, char **argv)
{
    CommandResult result;


    result.success = 1;
    result.exit_code = 0;
    result.error = NULL;


    /*
     * Temporary output buffer.
     */
    char *output = malloc(512);


    if (output == NULL)
    {
        result.success = 0;
        result.error = "Memory allocation failed.";

        return result;
    }


    output[0] = '\0';


    /*
     * Skip argv[0] because that is the command name.
     */
    for (int i = 1; i < argc; i++)
    {
        strcat(output, argv[i]);


        if (i < argc - 1)
        {
            strcat(output, " ");
        }
    }


    result.output = output;


    return result;
}



Command echo_command =
{
    .name = "echo",
    .description = "Print text to the terminal",
    .execute = echo_execute
};