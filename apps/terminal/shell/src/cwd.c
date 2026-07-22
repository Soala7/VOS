/*
 * File: VOS/apps/terminal/shell/src/cwd.c
 *
 * Stores the shell's current working directory.
 */

#include "../include/cwd.h"

#include <string.h>


static char current_directory[256] = "/";


void cwd_init(void)
{
    strcpy(current_directory, "/");
}


const char *cwd_get(void)
{
    return current_directory;
}


void cwd_set(const char *path)
{
    strncpy(
        current_directory,
        path,
        sizeof(current_directory) - 1
    );

    current_directory[sizeof(current_directory) - 1] = '\0';
}