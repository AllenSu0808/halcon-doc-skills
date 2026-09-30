# timed_wait_condition (Operator)

## Name

`timed_wait_condition` — Bounded wait on the signal of a condition synchronization object.

## Signature

`timed_wait_condition( : : ConditionHandle, MutexHandle, Timeout : )`

## Description

`timed_wait_condition` atomically unlocks *`MutexHandle`* and
waits on
*`ConditionHandle`*, as [`wait_condition`](wait_condition.md) does, but it also bounds
the duration of the wait. If *`ConditionHandle`* has not been signaled
within the amount of time specified by *`Timeout`* in micro seconds,
the mutex *`MutexHandle`* is re-acquired and
`timed_wait_condition` returns the error H_ERR_TIMEOUT.

Using negative values for *`Timeout`* means an infinite waiting time.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ConditionHandle`** (input_control)  condition `→`  (handle)

Condition synchronization object.

**`MutexHandle`** (input_control)  mutex `→`  (handle)

Mutex synchronization object.

**`Timeout`** (input_control)  number `→`  (integer)

Timeout in micro seconds.

## Result

`timed_wait_condition` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised. If a timeout occurs, the error
H_ERR_TIMEOUT is raised.

## Possible Successors

`signal_condition`,
`clear_condition`

## Module

Foundation
