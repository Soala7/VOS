/*
 * File: VOS/apps/terminal/shell/test_shell.c
 *
 * Small test program for the Gorgon OS shell backend.
 */

#include "include/shell.h"
#include "include/command_registry.h"
#include "include/command_loader.h"
#include "include/command_result.h"
#include "include/cwd.h"

#include <stdio.h>


int main(void)
{
    /* Prepare command storage. */
    registry_init();
    cwd_init();


    /* Add built-in commands. */
    load_commands();


    char input[] = "pwd";


    CommandResult result = shell_execute(input);


    if (result.success)
    {
        printf("%s\n", result.output);
    }
    else
    {
        printf("Error: %s\n", result.error);
    }

    command_result_destroy(&result);
    return 0;
}