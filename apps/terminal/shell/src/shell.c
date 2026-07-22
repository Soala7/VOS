/*
 * File: VOS/apps/terminal/shell/src/shell.c
 *
 * Controls the shell execution flow.
 */

#include "../include/shell.h"

#include "../include/parser.h"
#include "../include/command_registry.h"
#include "../include/parsed_command.h"

#include <stdlib.h>



CommandResult shell_execute(char *input)
{
    CommandResult result;


    result.success = 0;
    result.exit_code = 1;
    result.output = NULL;
    result.error = NULL;



    /*
     * Convert text input into a ParsedCommand.
     */
    ParsedCommand *parsed = parser_parse(input);


    if (parsed == NULL)
    {
        result.error = "Failed to parse command.";

        return result;
    }



    /*
     * Find the command in the registry.
     */
    Command *command = registry_find(parsed->name);


    if (command == NULL)
    {
        result.error = "Command not found.";

        parsed_command_destroy(parsed);

        return result;
    }



    /*
     * Execute the command.
     */
    result = command->execute(
        parsed->argc,
        parsed->argv
    );



    /*
     * Free parser memory.
     */
    parsed_command_destroy(parsed);


    return result;
}