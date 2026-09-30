# GetSystemTime (Operator)

## Name

`GetSystemTime` — Read out the system time.

## Signature

`static void HOperatorSet.GetSystemTime(out HTuple MSecond, out HTuple second, out HTuple minute, out HTuple hour, out HTuple day, out HTuple YDay, out HTuple month, out HTuple year)`

## Description

The operator `GetSystemTime` reads out the current system time.
The system time is read according to the local time zone or as UTC,
see *"system_time_base"* in [`GetSystem`](get_system.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MSecond`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Milliseconds (0..999).

**`second`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Seconds (0..59).

**`minute`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Minutes (0..59).

**`hour`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Hours (0..23).

**`day`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Day of the month (1..31).

**`YDay`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Day of the year (1..366).

**`month`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Month (1..12).

**`year`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Year (xxxx).

## Result

`GetSystemTime` always returns the value 2 (
H_MSG_TRUE)
.

## See also

`GetImageTime`

## Module

Foundation
