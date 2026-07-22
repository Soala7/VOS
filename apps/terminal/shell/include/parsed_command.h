/*
 * File: VOS/apps/terminal/shell/include/parsed_command.h
 *
 * Defines the structure used to store parsed user input.
 */

#ifndef PARSED_COMMAND_H
#define PARSED_COMMAND_H


/*
 * Stores a command after parsing.
 *
 * Example:
 *
 * Input:
 *     echo hello
 *
 * Result:
 *
 * name:
 *     echo
 *
 * argv:
 *     ["echo", "hello"]
 */
typedef struct
{
    char *name;

    int argc;

    char **argv;

} ParsedCommand;


/* Creates an empty parsed command. */
ParsedCommand *parsed_command_create(void);


/* Releases memory used by a parsed command. */
void parsed_command_destroy(ParsedCommand *command);


#endif