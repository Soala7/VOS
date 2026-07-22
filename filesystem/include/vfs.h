/*
 * File: VOS/filesystem/include/vfs.h
 *
 * Virtual File System interface.
 */

#ifndef VFS_H
#define VFS_H


/*
 * Initialize the virtual filesystem.
 */
void vfs_init(void);


/*
 * Check if a path exists.
 */
int vfs_exists(const char *path);


/*
 * Check if a path is a directory.
 */
int vfs_is_directory(const char *path);


/*
 * List contents of a directory.
 */
void vfs_list(const char *path);


#endif