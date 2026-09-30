# TimedWaitCondition (Operator)

## Name

`TimedWaitCondition` — Bounded wait on the signal of a condition synchronization object.

## Signature

`static void HOperatorSet.TimedWaitCondition(HTuple conditionHandle, HTuple mutexHandle, HTuple timeout)`

`void HCondition.TimedWaitCondition(HMutex mutexHandle, int timeout)`

## Description

`TimedWaitCondition` atomically unlocks *`mutexHandle`* and
waits on
*`conditionHandle`*, as [`WaitCondition`](wait_condition.md) does, but it also bounds
the duration of the wait. If *`conditionHandle`* has not been signaled
within the amount of time specified by *`timeout`* in micro seconds,
the mutex *`mutexHandle`* is re-acquired and
`TimedWaitCondition` returns the error H_ERR_TIMEOUT.

Using negative values for *`timeout`* means an infinite waiting time.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`conditionHandle`** (input_control)  condition `→` [HCondition](HCondition.md), [HTuple](HTuple.md) (*IntPtr*)

Condition synchronization object.

**`mutexHandle`** (input_control)  mutex `→` [HMutex](HMutex.md), [HTuple](HTuple.md) (*IntPtr*)

Mutex synchronization object.

**`timeout`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Timeout in micro seconds.

## Result

`TimedWaitCondition` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised. If a timeout occurs, the error
H_ERR_TIMEOUT is raised.

## Possible Successors

`SignalCondition`,
`ClearCondition`

## Module

Foundation
