/*
 * File: VOS/apps/terminal/shell/include/command_result.h
 *
 * Defines the result returned after a command executes.
 */

#ifndef COMMAND_RESULT_H
#define COMMAND_RESULT_H


typedef struct
{
    int success;

    int exit_code;

    char *output;

    char *error;

} CommandResult;


/*
 * Frees memory allocated by a command result.
 */
void command_result_destroy(CommandResult *result);


#endif