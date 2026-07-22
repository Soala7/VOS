/*
 * File: VOS/apps/terminal/shell/src/host_manager.c
 *
 * Stores and forwards host callbacks.
 */


#include "../include/host_manager.h"

#include <string.h>




static PWD_CALLBACK pwd_callback = 0;

static LS_CALLBACK ls_callback = 0;

static CD_CALLBACK cd_callback = 0;

static MKDIR_CALLBACK mkdir_callback = 0;

static TOUCH_CALLBACK touch_callback = 0;





void host_manager_set_pwd(
    PWD_CALLBACK callback
)
{
    pwd_callback = callback;
}




void host_manager_set_ls(
    LS_CALLBACK callback
)
{
    ls_callback = callback;
}




void host_manager_set_cd(
    CD_CALLBACK callback
)
{
    cd_callback = callback;
}




void host_manager_set_mkdir(
    MKDIR_CALLBACK callback
)
{
    mkdir_callback = callback;
}




void host_manager_set_touch(
    TOUCH_CALLBACK callback
)
{
    touch_callback = callback;
}







void host_manager_pwd(
    char *buffer,
    int size
)
{
    if (pwd_callback)
    {
        pwd_callback(
            buffer,
            size
        );

        return;
    }



    strncpy(
        buffer,
        "/",
        size - 1
    );

    buffer[size - 1] = '\0';
}






void host_manager_ls(
    const char *path,
    char *buffer,
    int size
)
{
    if (ls_callback)
    {
        ls_callback(
            path,
            buffer,
            size
        );

        return;
    }



    buffer[0] = '\0';
}







int host_manager_cd(
    const char *path
)
{
    if (cd_callback)
    {
        return cd_callback(path);
    }


    return 0;
}







int host_manager_mkdir(
    const char *path
)
{
    if (mkdir_callback)
    {
        return mkdir_callback(path);
    }


    return 0;
}


int host_manager_touch(
    const char *path
)
{
    if (touch_callback)
    {
        return touch_callback(path);
    }


    return 0;
}