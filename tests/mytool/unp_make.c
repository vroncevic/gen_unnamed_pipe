/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * unp_make.c
 * Copyright (C) 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
 *
 * mytool is free software: you can redistribute it and/or modify it
 * under terms of GNU General Public License as published by the
 * Free Software Foundation, either version 3 of License, or
 * (at your option) any later version.
 *
 * mytool is distributed in hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See GNU General Public License for more details.
 *
 * You should have received a copy of GNU General Public License along
 * with this program. If not, see <http://www.gnu.org/licenses/>.
 */

#include "np.h"

/**
 * Description:
 *     Make a FIFO special file (a named pipe).
 *
 * Arguments:
 *     path_name - FIFO special file path name
 *     mode - specifies FIFO's permissions
 *
 * Return value:
 *     status - on success return 0 | UNP_ERROR and error number is set to
 *              indicate error:
 *                  EACCES (one of directories in pathname did not allow
 *                          search (execute) permission)
 *                  EDQUOT (user's quota of disk blocks or inodes on the
 *                          filesystem has been exhausted)
 *                  EEXIST (pathname already exists, this includes case
 *                          where pathname is a symbolic link, dangling or not)
 *                  ENAMETOOLONG (either total length of pathname is greater
 *                                than PATH_MAX, or an individual filename
 *                                component has a length greater than NAME_MAX
 *                                in GNU system, there is no imposed limit
 *                                on overall filename length, but some
 *                                filesystems may place limits on length of a
 *                                component)
 *                  ENOENT (directory component in pathname does not exist or
 *                          is a dangling symbolic link)
 *                  ENOSPC (directory or filesystem has no room for new file)
 *                  ENOTDIR (component used as a directory in pathname is not,
 *                           in fact, a directory)
 *                  EROFS (pathname refers to a read-only filesystem)
 *                  EBADF (dirfd is not a valid file descriptor)
 *                  ENOTDIR (pathname is a relative path and dirfd is a file
 *                           descriptor referring to a file other than a
 *                           directory)
 *
 * Standards:
 *     POSIX.1-2001, POSIX.1-2008
 */
int unp_make(const char * path_name, mode_t mode) {
    int status;
    if (path_name != NULL && mode >= 0) {
        status = mkfifo(path_name, mode);
    } else {
        status = UNP_ERROR;
    }
    return status;
}

