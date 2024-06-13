/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * unp_write.c
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
 *     Write to a file descriptor.
 *
 * Arguments:
 *     file_descriptor - file descriptor
 *     buffer - socket address structure
 *     count - size of peer address
 *
 * Return value:
 *     number_of_bytes - on success, number of bytes written is returned |
 *                       UNP_ERROR and error number is set to indicate error.
 *
 *     Note that a successful write() may transfer fewer than count
 *     bytes.  Such partial writes can occur for various reasons; for
 *     example, because there was insufficient space on disk device
 *     to write all of requested bytes, or because a blocked write()
 *     to a socket, pipe, or similar was interrupted by a signal handler
 *     after it had transferred some, but before it had transferred all
 *     of requested bytes.  In event of a partial write, the
 *     caller can make another write() call to transfer remaining
 *     bytes.  subsequent call will either transfer further bytes or
 *     may result in an error (e.g., if disk is now full).
 *     If count is zero and descriptor refers to a regular file, then write()
 *     may return a failure status if one of errors below is
 *     detected.  If no errors are detected, or error detection is not
 *     performed, 0 is returned without causing any other effect.  If
 *     count is zero and descriptor refers to a file other than a regular
 *     file, results are not specified.
 *
 *     EAGAIN (file descriptor descriptor refers to a file other than a
 *             socket and has been marked nonblocking (O_NONBLOCK), and
 *             write would block.  See open(2) for further details on
 *             O_NONBLOCK flag)
 *     EAGAIN or EWOULDBLOCK
 *            (file descriptor descriptor refers to a socket and has been
 *             marked nonblocking (O_NONBLOCK), and write would
 *             block.  POSIX.1-2001 allows either error to be returned
 *             for this case, and does not require these constants to
 *             have same value, so a portable application should
 *             check for both possibilities)
 *     EBADF (descriptor is not a valid file descriptor or is not open for
 *            writing)
 *     EDESTADDRREQ
 *            (descriptor refers to a datagram socket for which a peer address
 *             has not been set using connect(2))
 *     EDQUOT (user's quota of disk blocks on filesystem containing file
 *             referred to by descriptor has been exhausted)
 *     EFAULT (buf is outside your accessible address space)
 *     EFBIG (An attempt was made to write a file that exceeds the
 *            implementation-defined maximum file size or process's
 *            file size limit, or to write at a position past the
 *            maximum allowed offset)
 *     EINTR (call was interrupted by a signal before any data was
 *            written; see signal(7))
 *     EINVAL (descriptor is attached to an object which is unsuitable for
 *             writing; or file was opened with O_DIRECT flag,
 *             and either address specified in buf, value
 *             specified in count, or file offset is not suitably
 *             aligned)
 *     EIO (low-level I/O error occurred while modifying inode.
 *          This error may relate to write-back of data written by
 *          an earlier write(), which may have been issued to a
 *          different file descriptor on same file.  Since Linux
 *          4.13, errors from write-back come with a promise that they
 *          may be reported by subsequent.  write() requests, and will
 *          be reported by a subsequent fsync(2) (whether or not they
 *          were also reported by write()).  An alternate cause of EIO
 *          on networked filesystems is when an advisory lock had been
 *          taken out on file descriptor and this lock has been
 *          lost.  See Lost locks section of fcntl(2) for further
 *          details)
 *     ENOSPC (device containing file referred to by descriptor has no
 *             room for data)
 *     EPERM (operation was prevented by a file seal; see fcntl(2))
 *     EPIPE (descriptor is connected to a pipe or socket whose reading end is
 *            closed.  When this happens writing process will also
 *            receive a SIGPIPE signal.  (Thus, write return value
 *            is seen only if program catches, blocks or ignores
 *            this signal.))
 *     Other errors may occur, depending on object connected to descriptor.
 *
 * Standards:
 *     POSIX.1-2001, POSIX.1-2008
 */
ssize_t unp_write(int file_descriptor, const void * buffer, size_t count) {
    ssize_t number_of_bytes;
    if (file_descriptor >= 0 && buffer != NULL) {
        number_of_bytes = write(file_descriptor, buffer, count);
    } else {
        number_of_bytes = UNP_ERROR;
    }
    return number_of_bytes;
}

