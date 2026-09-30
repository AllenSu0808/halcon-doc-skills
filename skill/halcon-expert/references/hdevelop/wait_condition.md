# wait_condition (Operator)

## Name

`wait_condition` — wait on the signal of a condition synchronization object.

## Signature

`wait_condition( : : ConditionHandle, MutexHandle : )`

## Description

`wait_condition` atomically unlocks the *`MutexHandle`* (as per
[`unlock_mutex`](unlock_mutex.md)) and waits for the condition variable
*`ConditionHandle`* to be signaled. The thread execution is suspended
and does not consume any CPU time until the condition variable is signaled.
The mutex must be locked by the calling thread on entrance to
`wait_condition`. Before returning to the calling thread,
`wait_condition` re-acquires *`MutexHandle`*
(as per [`lock_mutex`](lock_mutex.md)).

Unlocking the mutex and suspending on the condition variable is done
atomically. Thus, if all threads always acquire the mutex before signaling
the condition, this guarantees that the condition cannot be signaled
(and thus ignored) between the time a thread locks the mutex and
the time it waits on the condition variable.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ConditionHandle`** (input_control)  condition `→`  (handle)

Condition synchronization object.

**`MutexHandle`** (input_control)  mutex `→`  (handle)

Mutex synchronization object.

## Result

`wait_condition` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Possible Successors

`signal_condition`,
`clear_condition`

## Module

Foundation
