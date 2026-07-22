/*
 * File: VOS/apps/terminal/shell/src/command_result.c
 *
 * Handles cleanup of command results.
 */

#include "../include/command_result.h"
#include <stdio.h>
#include <stdlib.h>



void command_result_destroy(CommandResult *result)
{
    if (result == NULL)
    {
        return;
    }

    printf(
        "DESTROY output=%p error=%p\n",
        result->output,
        result->error
    );

    free(result->output);
    free(result->error);

    result->output = NULL;
    result->error = NULL;
}