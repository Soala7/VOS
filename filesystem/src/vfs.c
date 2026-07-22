/*
 * File: VOS/filesystem/src/vfs.c
 *
 * Virtual filesystem implementation.
 */

#include "../include/vfs.h"

#include <stdio.h>
#include <string.h>


typedef struct
{
    char name[64];
    int directory;

} VFSNode;



static VFSNode nodes[] =
{
    {"system", 1},
    {"users", 1},
    {"apps", 1},
    {"README.txt", 0}
};


static int node_count = 4;



void vfs_init(void)
{
    printf("[VFS] Initialized\n");
}



int vfs_exists(const char *path)
{
    for (int i = 0; i < node_count; i++)
    {
        if (strcmp(nodes[i].name, path) == 0)
        {
            return 1;
        }
    }


    return 0;
}



int vfs_is_directory(const char *path)
{
    for (int i = 0; i < node_count; i++)
    {
        if (strcmp(nodes[i].name, path) == 0)
        {
            return nodes[i].directory;
        }
    }


    return 0;
}



void vfs_list(const char *path)
{
    (void)path;


    for (int i = 0; i < node_count; i++)
    {
        printf("%s\n", nodes[i].name);
    }
}