/***************************************************************************
SPDX-FileCopyrightText: 1996 Apple Computer, Inc., AT&T Corp., International
Business Machines Corporation and Siemens Rolm Communications Inc.

SPDX-License-Identifier: LicenseRef-APPLEMIT

The software is provided with RESTRICTED RIGHTS.  Use, duplication, or
disclosure by the government are subject to restrictions set forth in
DFARS 252.227-7013 or 48 CFR 52.227-19, as applicable.

***************************************************************************/

#ifndef VCC_H
#define VCC_H

#include "libical_vcal_export.h"
#include "vobject.h"

#if defined(__CPLUSPLUS__) || defined(__cplusplus)
extern "C"
{
#endif

    typedef void (*MimeErrorHandler) (const char *);

    LIBICAL_VCAL_EXPORT void registerMimeErrorHandler(MimeErrorHandler);

    LIBICAL_VCAL_EXPORT VObject *Parse_MIME(const char *input, unsigned long len);

    LIBICAL_VCAL_EXPORT VObject *Parse_MIME_FromFileName(const char *fname);

/* NOTE regarding Parse_MIME_FromFile
The function above, Parse_MIME_FromFile, comes in two flavors,
neither of which is exported from the DLL. Each version takes
a CFile or FILE* as a parameter, neither of which can be
passed across a DLL interface (at least that is my experience).
If you are linking this code into your build directly then
you may find them a more convenient API that the other flavors
that take a file name. If you use them with the DLL LIB you
will get a link error.
*/

#ifdef INCLUDEMFC
    LIBICAL_VCAL_EXPORT VObject *Parse_MIME_FromFile(CFile * file);
#else
    LIBICAL_VCAL_EXPORT VObject *Parse_MIME_FromFile(FILE * file);
#endif

#if defined(__CPLUSPLUS__) || defined(__cplusplus)
}

#endif

#endif /* VCC_H */
