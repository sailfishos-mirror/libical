#!/usr/bin/env python
#======================================================================
# FILE: Duration.py
# CREATOR: eric
#
# SPDX-FileCopyrightText: 2001, Eric Busboom <eric@civicknowledge.com>
# SPDX-FileCopyrightText: 2001, Patrick Lewis <plewis@inetarena.com>
#
# SPDX-License-Identifier: LGPL-2.1-only OR MPL-2.0
#
#
#
#===============================================================

from LibicalWrap import *
from Property import Property
from types import DictType, StringType, IntType

class Duration(Property):
    """
    Represent a length of time, like 3 minutes, or 6 days, 20 seconds.


    """

    def __init__(self, arg, name="DURATION"):
        """
        Create a new duration from an RFC2445 string or number of seconds.
        Construct the duration from an iCalendar string or a number of seconds.

        Duration("P3DT2H34M45S")   Construct from an iCalendar string
        Duration(3660)             Construct from seconds
        """

        self.dur = None

        e=icalerror_supress("MALFORMEDDATA")

        if isinstance(arg, DictType):

            self.dur = icaldurationtype_from_string(arg['value'])
            Property.__init__(self,ref=arg['ref'])
        else:
            if isinstance(arg, StringType):
                self.dur = icaldurationtype_from_string(arg)
            elif isinstance(arg, IntType):
                self.dur = icaldurationtype_from_int(arg)
            elif isinstance(arg,Duration):
                self.dur = arg.dur
            else:
                self.dur = icaldurationtype_null_duration()

            Property.__init__(self,type=name)

        icalerror_restore("MALFORMEDDATA",e)

        if self.dur == None or icaldurationtype_is_null_duration(self.dur):
            raise Property.ConstructorFailedError("Failed to construct Duration from " +str(arg))

        try:
            self._update_value()
        except Property.UpdateFailedError:
            raise Property.ConstructorFailedError("Failed to construct Duration from  " + str(arg))

    def _update_value(self):

        self.value(icaldurationtype_as_ical_string(self.dur),"DURATION")

    def valid(self):
        "Returns true if this is a valid duration"

        return not icaldurationtype_is_null_duration(self.dur)

    def seconds(self,v=None):
        """Return or set duration in seconds"""
        if(v != None):
            self.dur = icaldurationtype_from_int(v);
            self.dict['value'] = icaltimedurationtype_as_ical_string(self.dur)
        return icaldurationtype_as_int(self.dur)
