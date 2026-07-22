/*
 * File: VOS/apps/terminal/shell/include/host_manager.h
 *
 * Manages callbacks between the C shell and VOS host.
 */

#ifndef HOST_MANAGER_H
#define HOST_MANAGER_H

#ifdef __cplusplus
extern "C" {
#endif



typedef void (*PWD_CALLBACK)(
    char *buffer,
    int size
);



typedef void (*LS_CALLBACK)(
    const char *path,
    char *buffer,
    int size
);



typedef int (*CD_CALLBACK)(
    const char *path
);



typedef int (*MKDIR_CALLBACK)(
    const char *path
);



typedef int (*TOUCH_CALLBACK)(
    const char *path
);




void host_manager_set_pwd(
    PWD_CALLBACK callback
);



void host_manager_set_ls(
    LS_CALLBACK callback
);



void host_manager_set_cd(
    CD_CALLBACK callback
);



void host_manager_set_mkdir(
    MKDIR_CALLBACK callback
);



void host_manager_set_touch(
    TOUCH_CALLBACK callback
);




void host_manager_pwd(
    char *buffer,
    int size
);



void host_manager_ls(
    const char *path,
    char *buffer,
    int size
);



int host_manager_cd(
    const char *path
);



int host_manager_mkdir(
    const char *path
);



int host_manager_touch(
    const char *path
);



#ifdef __cplusplus
}
#endif

#endif