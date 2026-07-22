/*
 * File: VOS/apps/terminal/shell/src/command_result_builder.c
 *
 * Implements helper functions for building CommandResult objects.
 */

#include "../include/command_result_builder.h"

#include <stdlib.h>
#include <string.h>



char *result_alloc(size_t size)
{
    return malloc(size);
}



CommandResult result_success(char *output)
{
    CommandResult result;

    result.success = 1;
    result.exit_code = 0;

    result.output = output;
    result.error = NULL;

    return result;
}



CommandResult result_error(const char *error)
{
    CommandResult result;

    result.success = 0;
    result.exit_code = 1;

    result.output = NULL;


    if (error != NULL)
    {
        result.error = malloc(
            strlen(error) + 1
        );


        if (result.error != NULL)
        {
            strcpy(
                result.error,
                error
            );
        }
    }
    else
    {
        result.error = NULL;
    }


    return result;
}