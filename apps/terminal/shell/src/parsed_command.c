/*
 * File: VOS/apps/terminal/shell/src/parsed_command.c
 *
 * Handles creation and cleanup of parsed commands.
 */

#include "../include/parsed_command.h"

#include <stdlib.h>


ParsedCommand *parsed_command_create(void)
{
    ParsedCommand *command = malloc(sizeof(ParsedCommand));


    if (command == NULL)
    {
        return NULL;
    }


    command->name = NULL;
    command->argc = 0;
    command->argv = NULL;


    return command;
}



void parsed_command_destroy(ParsedCommand *command)
{
    if (command == NULL)
    {
        return;
    }


    /*
     * Free each argument string.
     */
    for (int i = 0; i < command->argc; i++)
    {
        free(command->argv[i]);
    }


    /*
     * Free the argument array.
     */
    free(command->argv);


    /*
     * Free command name.
     */
    free(command->name);


    /*
     * Free the structure.
     */
    free(command);
}