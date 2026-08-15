# Libical v4.0.5

## Overview

This is a patch release and is fully source and binary compatible with version 4.0.0.

## ReleaseNotes

- Fix 32-bit time_t upper bound off by two days.
- Buildsystem: fix libical_deprecated_option() writing the wrong cache value
- Bogus TZIDs no longer cause an error.
- DTEND, DURATION, DUE property types and values are now validated per RFC 5545 Sections 3.8.2.2 - 3.8.2.5.
- Built-in timezones updated to tzdata2026c.

Please see the [CHANGELOG](https://github.com/libical/libical/blob/4.0/CHANGELOG.md) for more.
