# WaitSeconds (Operator)

## Name

`WaitSeconds` — Delaying the execution of the program.

## Signature

`static void HOperatorSet.WaitSeconds(HTuple seconds)`

`static void HSystem.WaitSeconds(double seconds)`

## Description

The operator `WaitSeconds` delays the execution by the number
of seconds indicated in *`seconds`*.

`WaitSeconds` uses the *"performance_counter"* for the
measurement of time intervals. The *"performance_counter"* is
explained in the description of the parameter *"clock_mode"* of
the operator [`SetSystem`](set_system.md).

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`seconds`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Number of seconds by which the execution of the program
will be delayed.

Default:
10

Restriction:
`Seconds >= 0`

## Result

The operator `WaitSeconds` always returns the value 2 (
H_MSG_TRUE)
.

## Possible Successors

`SystemCall`

## See also

`SystemCall`,
`CountSeconds`

## Module

Foundation
