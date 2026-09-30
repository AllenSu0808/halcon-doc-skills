# wait_seconds (Operator)

## Name

`wait_seconds` — Delaying the execution of the program.

## Signature

`wait_seconds( : : Seconds : )`

## Description

The operator `wait_seconds` delays the execution by the number
of seconds indicated in *`Seconds`*.

`wait_seconds` uses the *'performance_counter'* for the
measurement of time intervals. The *'performance_counter'* is
explained in the description of the parameter *'clock_mode'* of
the operator [`set_system`](set_system.md).

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Seconds`** (input_control)  real `→`  (real)

Number of seconds by which the execution of the program
will be delayed.

Default:
10

Restriction:
`Seconds >= 0`

## Result

The operator `wait_seconds` always returns the value 2 (
H_MSG_TRUE)
.

## Possible Successors

`system_call`

## See also

`system_call`,
`count_seconds`

## Module

Foundation
