/*
 * File: VOS/apps/terminal/shell/src/host.c
 *
 * Interface between shell commands and host callbacks.
 */


#include "../include/host.h"
#include "../include/host_manager.h"
#include <stdio.h>


void host_init(void)
{
}



void host_shutdown(void)
{
}




void host_pwd(
    char *buffer,
    int size
)
{
    host_manager_pwd(
        buffer,
        size
    );
}




void host_ls(
    const char *path,
    char *buffer,
    int size
)
{
    if (path == NULL)
    {
        path = "";
    }


    host_manager_ls(
        path,
        buffer,
        size
    );
}




int host_cd(
    const char *path
)
{
    return host_manager_cd(
        path
    );
}




int host_mkdir(
    const char *path
)
{
    return host_manager_mkdir(
        path
    );
}




int host_touch(
    const char *path
)
{
    return host_manager_touch(
        path
    );
}