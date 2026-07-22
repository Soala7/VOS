/*
 * File: VOS/apps/terminal/shell/include/host.h
 *
 * Host interface between the shell and VOS.
 */

#ifndef HOST_H
#define HOST_H

#ifdef __cplusplus
extern "C" {
#endif



/*
 * Initialization
 */

void host_init(void);

void host_shutdown(void);




/*
 * Filesystem operations
 */


void host_pwd(
    char *buffer,
    int size
);



void host_ls(
    const char *path,
    char *buffer,
    int size
);



int host_cd(
    const char *path
);



int host_mkdir(
    const char *path
);



int host_touch(
    const char *path
);



#ifdef __cplusplus
}
#endif

#endif