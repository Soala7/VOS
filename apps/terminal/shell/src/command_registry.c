/*
 * File: VOS/apps/terminal/shell/src/command_registry.c
 *
 * Implements the command registry.
 */

#include "../include/command_registry.h"

#include <string.h>


#define MAX_COMMANDS 256


/*
 * Stores registered commands.
 */
static Command *commands[MAX_COMMANDS];


/*
 * Number of commands currently registered.
 */
static int command_count = 0;



void registry_init(void)
{
    /*
     * Reset registry.
     */
    command_count = 0;


    /*
     * Clear command storage.
     */
    for (int i = 0; i < MAX_COMMANDS; i++)
    {
        commands[i] = NULL;
    }
}



int registry_register(Command *command)
{
    if (command == NULL)
    {
        return 0;
    }


    if (command_count >= MAX_COMMANDS)
    {
        return 0;
    }


    commands[command_count] = command;

    command_count++;


    return 1;
}



Command *registry_find(const char *name)
{
    if (name == NULL)
    {
        return NULL;
    }


    for (int i = 0; i < command_count; i++)
    {
        if (strcmp(commands[i]->name, name) == 0)
        {
            return commands[i];
        }
    }


    return NULL;
}

int registry_count(void)
{
    return command_count;
}



Command *registry_get(int index)
{
    if (index < 0 || index >= command_count)
    {
        return NULL;
    }


    return commands[index];
}