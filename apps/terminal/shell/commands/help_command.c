#include "../include/command.h"
#include "../include/command_registry.h"

#include <stdlib.h>
#include <string.h>
#include <stdio.h>



static CommandResult help_execute(int argc, char **argv)
{
    (void)argc;
    (void)argv;


    CommandResult result;

    result.success = 1;
    result.exit_code = 0;
    result.error = NULL;



    char *output = malloc(1024);


    if (output == NULL)
    {
        result.success = 0;
        result.error = "Memory allocation failed.";

        return result;
    }



    strcpy(output, "Available commands:\n");



    for (int i = 0; i < registry_count(); i++)
    {
        Command *command = registry_get(i);


        strcat(output, "  ");
        strcat(output, command->name);
        strcat(output, " - ");
        strcat(output, command->description);
        strcat(output, "\n");
    }



    result.output = output;


    return result;
}



Command help_command =
{
    .name = "help",
    .description = "Display available commands",
    .execute = help_execute
};