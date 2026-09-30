# LockMutex (Operator)

## Name

`LockMutex` — Lock a mutex synchronization object.

## Signature

`static void HOperatorSet.LockMutex(HTuple mutexHandle)`

`void HMutex.LockMutex()`

## Description

`LockMutex` locks the mutex given by *`mutexHandle`*. If the
mutex is currently unlocked, it becomes locked and owned by the calling
thread, and `LockMutex` returns immediately. If the mutex is
already locked by another thread, the calling thread waits until the mutex
is unlocked. The kind of wait is defined by the mutex' attributes set during
creation in [`CreateMutex`](create_mutex.md).

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`mutexHandle`** (input_control)  mutex `→` [HMutex](HMutex.md), [HTuple](HTuple.md) (*IntPtr*)

Mutex synchronization object.

## Result

If the mutex handle is valid, the operator `LockMutex` returns 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`CreateMutex`

## Possible Successors

`UnlockMutex`

## See also

`TryLockMutex`

## Module

Foundation
