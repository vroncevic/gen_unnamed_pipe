/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * unp_close.c
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
 *     Close a file descriptor.
 *
 * Arguments:
 *     file_descriptor - file descriptor
 *
 * Return value:
 *     status  - returns zero on success | UNP_ERROR and error number is set to
 *               indicate error:
 *                   EBADF (not valid file descriptor)
 *                   EINTR (interrupted by a signal)
 *                   EIO (I/O error occurred)
 *                   ENOSPC, EDQUOT (on NFS, these errors are not normally
 *                                   reported against first write which
 *                                   exceeds available storage space, but
 *                                   instead against a subsequent)
 *
 * Standards:
 *     POSIX.1-2001, POSIX.1-2008
 */
int unp_close(int file_descriptor) {
    int status;
    if (file_descriptor >= 0) {
        status = close(file_descriptor);
    } else {
        status = UNP_ERROR;
    }
    return status;
}

