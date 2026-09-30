# get_system_time (Operator)

## Name

`get_system_time` — Read out the system time.

## Signature

`def get_system_time() -> Tuple[int, int, int, int, int, int, int, int]`

## Description

The operator `get_system_time` reads out the current system time.
The system time is read according to the local time zone or as UTC,
see *"system_time_base"* in [`get_system`](get_system.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`msecond`** (output_control)  integer `→` int

Milliseconds (0..999).

**`second`** (output_control)  integer `→` int

Seconds (0..59).

**`minute`** (output_control)  integer `→` int

Minutes (0..59).

**`hour`** (output_control)  integer `→` int

Hours (0..23).

**`day`** (output_control)  integer `→` int

Day of the month (1..31).

**`yday`** (output_control)  integer `→` int

Day of the year (1..366).

**`month`** (output_control)  integer `→` int

Month (1..12).

**`year`** (output_control)  integer `→` int

Year (xxxx).

## Result

`get_system_time` always returns the value 2 (
H_MSG_TRUE)
.

## See also

`get_image_time`

## Module

Foundation
