# get_system_time (Operator)

## Name

`get_system_time` — Read out the system time.

## Signature

`get_system_time( : : : MSecond, Second, Minute, Hour, Day, YDay, Month, Year)`

## Description

The operator `get_system_time` reads out the current system time.
The system time is read according to the local time zone or as UTC,
see *'system_time_base'* in [`get_system`](get_system.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MSecond`** (output_control)  integer `→`  (integer)

Milliseconds (0..999).

**`Second`** (output_control)  integer `→`  (integer)

Seconds (0..59).

**`Minute`** (output_control)  integer `→`  (integer)

Minutes (0..59).

**`Hour`** (output_control)  integer `→`  (integer)

Hours (0..23).

**`Day`** (output_control)  integer `→`  (integer)

Day of the month (1..31).

**`YDay`** (output_control)  integer `→`  (integer)

Day of the year (1..366).

**`Month`** (output_control)  integer `→`  (integer)

Month (1..12).

**`Year`** (output_control)  integer `→`  (integer)

Year (xxxx).

## Result

`get_system_time` always returns the value 2 (
H_MSG_TRUE)
.

## See also

`get_image_time`

## Module

Foundation
