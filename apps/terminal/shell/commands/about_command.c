/*
 * File: VOS/apps/terminal/shell/commands/about_command.c
 *
 * Implements the about command.
 */

#include "../include/command.h"
#include "../include/command_result_builder.h"
#include "../include/version.h"

#include <stdio.h>


static CommandResult about_execute(int argc, char **argv)
{
    (void)argc;
    (void)argv;


    char *output = result_alloc(512);

    if (output == NULL)
    {
        return result_error("Memory allocation failed.");
    }


    snprintf(
        output,
        512,

        "Gorgon OS(VOS)\n"
        "\n"
        "Version : %s\n"
        "Build   : %s\n"
        "\n"
        "Developer : Soala7\n"
        "\n"
        "Languages\n"
        "  - Python (The best)\n"
        "  - C (Speed) \n"
        "  - Rust (Security)\n"
        "\n"
        "A virtual operating system designed\n"
        "to evolve into a real operating system.\n"
        "Maybe",

        vos_version(),
        vos_build()
    );

    return result_success(output);
}


Command about_command =
{
    .name = "about",
    .description = "Display information about Gorgon OS",
    .execute = about_execute
};