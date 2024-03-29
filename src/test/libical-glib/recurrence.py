#!/usr/bin/env python3
# GI_TYPELIB_PATH=$PREFIX/lib/girepository-1.0/ ./recurrence-type.py

###############################################################################
#
# SPDX-FileCopyrightText: 2015 William Yu <williamyu@gnome.org>
#
# SPDX-License-Identifier: LGPL-2.1-only OR MPL-2.0
#
###############################################################################

''' Test Python bindings for libical recurrence '''

import gi
gi.require_version('ICalGLib', '3.0')
from gi.repository import ICalGLib  # nopep8 # pylint: disable=wrong-import-position

weekday = ICalGLib.Recurrence.day_day_of_week(0)
assert weekday == ICalGLib.RecurrenceWeekday.NO_WEEKDAY
weekday = ICalGLib.Recurrence.day_day_of_week(1)
assert weekday == ICalGLib.RecurrenceWeekday.SUNDAY_WEEKDAY

assert ICalGLib.Recurrence.day_position(15) == 1
assert ICalGLib.Recurrence.day_position(16) == 2
assert ICalGLib.Recurrence.day_position(25) == 3

encoded = ICalGLib.Recurrence.encode_day(ICalGLib.RecurrenceWeekday.MONDAY_WEEKDAY, 0)
assert ICalGLib.Recurrence.day_day_of_week(encoded) == ICalGLib.RecurrenceWeekday.MONDAY_WEEKDAY
assert ICalGLib.Recurrence.day_position(encoded) == 0

encoded = ICalGLib.Recurrence.encode_day(ICalGLib.RecurrenceWeekday.THURSDAY_WEEKDAY, -3)
assert ICalGLib.Recurrence.day_day_of_week(encoded) == ICalGLib.RecurrenceWeekday.THURSDAY_WEEKDAY
assert ICalGLib.Recurrence.day_position(encoded) == -3

encoded = ICalGLib.Recurrence.encode_day(ICalGLib.RecurrenceWeekday.FRIDAY_WEEKDAY, 2)
assert ICalGLib.Recurrence.day_day_of_week(encoded) == ICalGLib.RecurrenceWeekday.FRIDAY_WEEKDAY
assert ICalGLib.Recurrence.day_position(encoded) == 2

encoded = ICalGLib.Recurrence.encode_month(3, 0)
assert ICalGLib.Recurrence.month_month(encoded) == 3
assert not ICalGLib.Recurrence.month_is_leap(encoded)

encoded = ICalGLib.Recurrence.encode_month(12, 1)
assert ICalGLib.Recurrence.month_month(encoded) == 12
assert ICalGLib.Recurrence.month_is_leap(encoded)

string = "COUNT=10;FREQ=DAILY"
recurrence = ICalGLib.Recurrence.new_from_string(string)
assert recurrence.to_string() == "FREQ=DAILY;COUNT=10"

recurrence.set_by_second(0, 1)
recurrence.set_by_second(1, ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX)
assert recurrence.get_by_second(0) == 1
assert recurrence.get_by_second(1) == ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX
array = recurrence.get_by_second_array()
assert array[0] == 1
assert len(array) == 1
array = [100, 101]
assert len(array) == 2
recurrence.set_by_second_array(array)
assert recurrence.get_by_second(0) == 100
assert recurrence.get_by_second(1) == 101
assert recurrence.get_by_second(2) == ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX
array = recurrence.get_by_second_array()
assert array[0] == 100
assert array[1] == 101
assert len(array) == 2

recurrence.set_by_minute(0, 2)
recurrence.set_by_minute(1, ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX)
assert recurrence.get_by_minute(0) == 2
assert recurrence.get_by_minute(1) == ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX
array = recurrence.get_by_minute_array()
assert array[0] == 2
assert len(array) == 1
array = [200, 201]
assert len(array) == 2
recurrence.set_by_minute_array(array)
assert recurrence.get_by_minute(0) == 200
assert recurrence.get_by_minute(1) == 201
assert recurrence.get_by_minute(2) == ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX
array = recurrence.get_by_minute_array()
assert array[0] == 200
assert array[1] == 201
assert len(array) == 2

recurrence.set_by_hour(0, 3)
recurrence.set_by_hour(1, ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX)
assert recurrence.get_by_hour(0) == 3
assert recurrence.get_by_hour(1) == ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX
array = recurrence.get_by_hour_array()
assert array[0] == 3
assert len(array) == 1
array = [300, 301]
assert len(array) == 2
recurrence.set_by_hour_array(array)
assert recurrence.get_by_hour(0) == 300
assert recurrence.get_by_hour(1) == 301
assert recurrence.get_by_hour(2) == ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX
array = recurrence.get_by_hour_array()
assert array[0] == 300
assert array[1] == 301
assert len(array) == 2

recurrence.set_by_day(0, 4)
recurrence.set_by_day(1, ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX)
assert recurrence.get_by_day(0) == 4
assert recurrence.get_by_day(1) == ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX
array = recurrence.get_by_day_array()
assert array[0] == 4
assert len(array) == 1
array = [400, 401]
assert len(array) == 2
recurrence.set_by_day_array(array)
assert recurrence.get_by_day(0) == 400
assert recurrence.get_by_day(1) == 401
assert recurrence.get_by_day(2) == ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX
array = recurrence.get_by_day_array()
assert array[0] == 400
assert array[1] == 401
assert len(array) == 2

recurrence.set_by_month_day(0, 5)
recurrence.set_by_month_day(1, ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX)
assert recurrence.get_by_month_day(0) == 5
assert recurrence.get_by_month_day(1) == ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX
array = recurrence.get_by_month_day_array()
assert array[0] == 5
assert len(array) == 1
array = [500, 501]
assert len(array) == 2
recurrence.set_by_month_day_array(array)
assert recurrence.get_by_month_day(0) == 500
assert recurrence.get_by_month_day(1) == 501
assert recurrence.get_by_month_day(2) == ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX
array = recurrence.get_by_month_day_array()
assert array[0] == 500
assert array[1] == 501
assert len(array) == 2

recurrence.set_by_year_day(0, 6)
recurrence.set_by_year_day(1, ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX)
assert recurrence.get_by_year_day(0) == 6
assert recurrence.get_by_year_day(1) == ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX
array = recurrence.get_by_year_day_array()
assert array[0] == 6
assert len(array) == 1
array = [600, 601]
assert len(array) == 2
recurrence.set_by_year_day_array(array)
assert recurrence.get_by_year_day(0) == 600
assert recurrence.get_by_year_day(1) == 601
assert recurrence.get_by_year_day(2) == ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX
array = recurrence.get_by_year_day_array()
assert array[0] == 600
assert array[1] == 601
assert len(array) == 2

recurrence.set_by_week_no(0, 7)
recurrence.set_by_week_no(1, ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX)
assert recurrence.get_by_week_no(0) == 7
assert recurrence.get_by_week_no(1) == ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX
array = recurrence.get_by_week_no_array()
assert array[0] == 7
assert len(array) == 1
array = [700, 701]
assert len(array) == 2
recurrence.set_by_week_no_array(array)
assert recurrence.get_by_week_no(0) == 700
assert recurrence.get_by_week_no(1) == 701
assert recurrence.get_by_week_no(2) == ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX
array = recurrence.get_by_week_no_array()
assert array[0] == 700
assert array[1] == 701
assert len(array) == 2

recurrence.set_by_month(0, 8)
recurrence.set_by_month(1, ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX)
assert recurrence.get_by_month(0) == 8
assert recurrence.get_by_month(1) == ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX
array = recurrence.get_by_month_array()
assert array[0] == 8
assert len(array) == 1
array = [800, 801]
assert len(array) == 2
recurrence.set_by_month_array(array)
assert recurrence.get_by_month(0) == 800
assert recurrence.get_by_month(1) == 801
assert recurrence.get_by_month(2) == ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX
array = recurrence.get_by_month_array()
assert array[0] == 800
assert array[1] == 801
assert len(array) == 2

recurrence.set_by_set_pos(0, 9)
recurrence.set_by_set_pos(1, ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX)
assert recurrence.get_by_set_pos(0) == 9
assert recurrence.get_by_set_pos(1) == ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX
array = recurrence.get_by_set_pos_array()
assert array[0] == 9
assert len(array) == 1
array = [900, 901]
assert len(array) == 2
recurrence.set_by_set_pos_array(array)
assert recurrence.get_by_set_pos(0) == 900
assert recurrence.get_by_set_pos(1) == 901
assert recurrence.get_by_set_pos(2) == ICalGLib.RecurrenceArrayMaxValues.RECURRENCE_ARRAY_MAX
array = recurrence.get_by_set_pos_array()
assert array[0] == 900
assert array[1] == 901
assert len(array) == 2

recurrence.set_by_second(0, 13)
by_second = recurrence.get_by_second_array()
assert by_second[0] == 13

recurrence = ICalGLib.Recurrence.new_from_string(string)

assert ICalGLib.Recurrence.weekday_from_string("MO") == ICalGLib.RecurrenceWeekday.MONDAY_WEEKDAY

start = 100000
result = ICalGLib.recur_expand_recurrence(string, start, 10)
secsPerDay = 24*60*60
for i in range(0, 9):
    assert result[i] == start + i*secsPerDay

string = "19970101T183248Z/19970102T071625Z"

period = ICalGLib.Period.new_from_string(string)
start = period.get_start()

iterator = ICalGLib.RecurIterator.new(recurrence, start)
timetype = iterator.next()
day = timetype.get_day()
ref = 1
while day != 0:
    assert day == ref
    ref += 1
    timetype = iterator.next()
    day = timetype.get_day()

recurrence = ICalGLib.Recurrence.new_from_string("FREQ=YEARLY;COUNT=10")
start = ICalGLib.Time.new_from_string("20161224T000000Z")

iterator = ICalGLib.RecurIterator.new(recurrence, start)

start = ICalGLib.Time.new_from_string("20181224T000000Z")

assert ICalGLib.RecurIterator.set_start(iterator, start) == 0

recurrence = ICalGLib.Recurrence.new_from_string("FREQ=YEARLY")
start = ICalGLib.Time.new_from_string("20161224T000000Z")

iterator = ICalGLib.RecurIterator.new(recurrence, start)

start = ICalGLib.Time.new_from_string("20181224T000000Z")

assert ICalGLib.RecurIterator.set_start(iterator, start) == 1
timetype = iterator.next()

assert timetype.get_year() == 2018

timetype = iterator.next()
assert timetype.get_year() == 2019
