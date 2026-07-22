/*
 * File: VOS/apps/terminal/shell/include/cwd.h
 *
 * Manages the shell's current working directory.
 */

#ifndef CWD_H
#define CWD_H


/*
 * Initializes the current working directory.
 */
void cwd_init(void);


/*
 * Returns the current working directory.
 */
const char *cwd_get(void);


/*
 * Changes the current working directory.
 */
void cwd_set(const char *path);


#endif