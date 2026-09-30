# TryLockMutex (Operator)

## Name

`TryLockMutex` — Lock a mutex synchronization object.

## Signature

`static void HOperatorSet.TryLockMutex(HTuple mutexHandle, out HTuple busy)`

`int HMutex.TryLockMutex()`

## Description

`TryLockMutex` behaves identically to [`LockMutex`](lock_mutex.md), except
that it does not block the calling thread if the mutex is already locked by
another thread but returns immediately. The state of the mutex before trying
to lock it is returned in *`busy`*. *1* indicates that the mutex
was already locked before calling `TryLockMutex`, *0* that
the mutex was unlocked (signaled).

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`mutexHandle`** (input_control)  mutex `→` [HMutex](HMutex.md), [HTuple](HTuple.md) (*IntPtr*)

Mutex synchronization object.

**`busy`** (output_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Mutex already locked?

## Result

If the mutex handle is valid, the operator `TryLockMutex`
returns 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMutex`

## Possible Successors

`UnlockMutex`

## See also

`LockMutex`

## Module

Foundation
