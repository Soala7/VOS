/*
 * File: VOS/apps/terminal/shell/src/command_loader.c
 *
 * Registers built-in commands.
 */

#include <stdio.h>

#include "../include/command_loader.h"

#include "../include/command_registry.h"

#include "../include/command.h"


/*
 * Command defined in help.c
 */
extern Command help_command;
extern Command echo_command;
extern Command clear_command;
extern Command version_command;
extern Command about_command;
extern Command exit_command;
extern Command date_command;
extern Command time_command;
extern Command pwd_command;
extern Command ls_command;
extern Command cd_command;
extern Command mkdir_command;
extern Command touch_command;

void load_commands(void)
{
    registry_register(&help_command);
    registry_register(&echo_command);
    registry_register(&clear_command);
    registry_register(&version_command);
    registry_register(&about_command);
    registry_register(&exit_command);
    registry_register(&date_command);
    registry_register(&time_command);
    registry_register(&pwd_command);
    registry_register(&ls_command);
    registry_register(&cd_command);
    registry_register(&mkdir_command);
    registry_register(&touch_command);

    printf("REGISTERED COMMANDS:\n");

    for(int i = 0; i < registry_count(); i++)
    {
        printf("%s\n", registry_get(i)->name);
    }

    printf("cd execute address: %p\n", cd_command.execute);
    printf("mkdir execute address: %p\n", mkdir_command.execute);

    printf("cd command address: %p\n", &cd_command);
    printf("mkdir command address: %p\n", &mkdir_command);
}