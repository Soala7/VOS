/*
 * File: VOS/apps/terminal/shell/src/parser.c
 *
 * Implements command line parsing.
 */

#include "../include/parser.h"

#include <stdlib.h>
#include <string.h>


#define MAX_ARGUMENTS 64



ParsedCommand *parser_parse(char *input)
{
    /*
     * Create the command container.
     */
    ParsedCommand *command = parsed_command_create();


    if (command == NULL)
    {
        return NULL;
    }


    /*
     * Temporary storage for splitting input.
     */
    char *token;


    int capacity = MAX_ARGUMENTS;


    command->argv = malloc(sizeof(char *) * capacity);


    if (command->argv == NULL)
    {
        parsed_command_destroy(command);
        return NULL;
    }



    /*
     * Split input using spaces.
     *
     * Example:
     *
     * "echo hello"
     *
     * becomes:
     *
     * "echo"
     * "hello"
     */
    token = strtok(input, " ");



    while (token != NULL)
    {
        command->argv[command->argc] = strdup(token);

        command->argc++;

        token = strtok(NULL, " ");
    }



    /*
     * First argument is always the command name.
     */
    if (command->argc > 0)
    {
        command->name = strdup(command->argv[0]);
    }


    return command;
}