/*
 * File: VOS/apps/terminal/shell/include/parser.h
 *
 * Defines the shell input parser.
 */

#ifndef PARSER_H
#define PARSER_H

#include "parsed_command.h"


/* Converts raw user input into a ParsedCommand. */
ParsedCommand *parser_parse(char *input);


#endif