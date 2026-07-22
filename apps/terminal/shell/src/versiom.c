/*
 * File: VOS/apps/terminal/shell/src/version.c
 *
 * Provides version information.
 */

#include "../include/version.h"


const char *vos_name(void)
{
    return "Gorgon OS";
}


const char *vos_version(void)
{
    return "0.1.0";
}


const char *vos_build(void)
{
    return "Development";
}