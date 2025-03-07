/*
 * This work is based on work from Hiram Clawson and has been modified to the
 * needs of the libical project. The original copyright notice is as follows:
 */
/*
 *      Copyright (c) 1986-2000, Hiram Clawson
 *      All rights reserved.
 *
 *      Redistribution and use in source and binary forms, with or
 *      without modification, are permitted provided that the following
 *      conditions are met:
 *
 *              Redistributions of source code must retain the above
 *              copyright notice, this list of conditions and the
 *              following disclaimer.
 *
 *              Redistributions in binary form must reproduce the
 *              above copyright notice, this list of conditions and
 *              the following disclaimer in the documentation and/or
 *              other materials provided with the distribution.
 *
 *              Neither name of The Museum of Hiram nor the names of
 *              its contributors may be used to endorse or promote products
 *              derived from this software without specific prior
 *              written permission.
 *
 *      THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
 *      CONTRIBUTORS ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES,
 *      INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 *      MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
 *      IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
 *      INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 *      (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 *      OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 *      HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
 *      STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
 *      IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
 *      THE POSSIBILITY OF SUCH DAMAGE.
 */
/*
 * The modifications made are licensed as follows (to distinguish between
 * the original code and the modifications made, refer to the source code
 * history):
 */
 /*======================================================================

  SPDX-FileCopyrightText: 2018, Markus Minichmayr
      https://tapkey.com

  SPDX-License-Identifier: LGPL-2.1-only OR MPL-2.0
 ========================================================================*/

/**
 *      @file astime.h
 *      @brief contains definitions of structures used for time calculations.
 */

#ifndef ICAL_ASTIME_H
#define ICAL_ASTIME_H

#include "libical_ical_export.h"

/*      Functions in caldate.c  */

typedef struct ut_instant_int
{
    long j_date0;      /**< julian decimal date, 0 = 01 Jan 4713 BC */
    long year;          /**< year, valid range [-4,713, +32,767] */
    int month;          /**<    [1-12]  */
    int day;            /**<    [1-31]  */
    int weekday;                /**<    [0-6]   */
    int day_of_year;            /**<    [1-366] */
} UTinstantInt, *UTinstantIntPtr;

/*      Functions in caldate.c  */

/**
 *	Computes the day of the week, the day of the year from
 *	the Gregorian (or julian) calendar date
 *	from the julian decimal date.
 *	for astronomical purposes, The Gregorian calendar reform occurred
 *	on 15 Oct. 1582.  This is 05 Oct 1582 by the julian calendar.

 *	Input:	a ut_instant structure pointer, where the j_date element
 *		has been set. ( = 0 for 01 Jan 4713 B.C.)
 *
 *	output:  will set all the other elements of the structure.
 *		As a convenience, the function will also return the year.
 *
 *	Reference: Astronomical formulae for calculators, meeus, p 23
 *	from fortran program by F. Espenak - April 1982 Page 277,
 *	50 Year canon of solar eclipses: 1986-2035
 *
 */
LIBICAL_ICAL_EXPORT void caldat_int(UTinstantIntPtr);

/**
 *	Computes the julian decimal date (j_date) from
 *	the Gregorian (or Julian) calendar date.
 *	for astronomical purposes, The Gregorian calendar reform occurred
 *	on 15 Oct. 1582.  This is 05 Oct 1582 by the julian calendar.
 *	Input:  a ut_instant structure pointer where Day, Month, Year
 *      have been set for the date in question.
 *
 *	Output: the j_date and weekday elements of the structure will be set.
 *		Also, the return value of the function will be the j_date too.
 *
 *	Reference: Astronomical formulae for calculators, meeus, p 23
 *	from fortran program by F. Espenak - April 1982 Page 276,
 *	50 Year canon of solar eclipses: 1986-2035
 */
LIBICAL_ICAL_EXPORT void juldat_int(UTinstantIntPtr);

#endif
