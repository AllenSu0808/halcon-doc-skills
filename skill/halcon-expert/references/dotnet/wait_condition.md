# WaitCondition (Operator)

## Name

`WaitCondition` — wait on the signal of a condition synchronization object.

## Signature

`static void HOperatorSet.WaitCondition(HTuple conditionHandle, HTuple mutexHandle)`

`void HCondition.WaitCondition(HMutex mutexHandle)`

## Description

`WaitCondition` atomically unlocks the *`mutexHandle`* (as per
[`UnlockMutex`](unlock_mutex.md)) and waits for the condition variable
*`conditionHandle`* to be signaled. The thread execution is suspended
and does not consume any CPU time until the condition variable is signaled.
The mutex must be locked by the calling thread on entrance to
`WaitCondition`. Before returning to the calling thread,
`WaitCondition` re-acquires *`mutexHandle`*
(as per [`LockMutex`](lock_mutex.md)).

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

**`conditionHandle`** (input_control)  condition `→` [HCondition](HCondition.md), [HTuple](HTuple.md) (*IntPtr*)

Condition synchronization object.

**`mutexHandle`** (input_control)  mutex `→` [HMutex](HMutex.md), [HTuple](HTuple.md) (*IntPtr*)

Mutex synchronization object.

## Result

`WaitCondition` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Possible Successors

`SignalCondition`,
`ClearCondition`

## Module

Foundation
