# timed_wait_condition (Operator)

## Name

`timed_wait_condition` — Bounded wait on the signal of a condition synchronization object.

## Signature

`def timed_wait_condition(condition_handle: HHandle, mutex_handle: HHandle, timeout: int) -> None`

## Description

`timed_wait_condition` atomically unlocks *`mutex_handle`* and
waits on
*`condition_handle`*, as [`wait_condition`](wait_condition.md) does, but it also bounds
the duration of the wait. If *`condition_handle`* has not been signaled
within the amount of time specified by *`timeout`* in micro seconds,
the mutex *`mutex_handle`* is re-acquired and
`timed_wait_condition` returns the error H_ERR_TIMEOUT.

Using negative values for *`timeout`* means an infinite waiting time.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`condition_handle`** (input_control)  condition `→` HHandle

Condition synchronization object.

**`mutex_handle`** (input_control)  mutex `→` HHandle

Mutex synchronization object.

**`timeout`** (input_control)  number `→` int

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
