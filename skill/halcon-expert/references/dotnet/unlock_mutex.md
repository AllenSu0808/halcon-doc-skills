# UnlockMutex (Operator)

## Name

`UnlockMutex` — Unlock a mutex synchronization object.

## Signature

`static void HOperatorSet.UnlockMutex(HTuple mutexHandle)`

`void HMutex.UnlockMutex()`

## Description

`UnlockMutex` unlocks the mutex object given by *`mutexHandle`*.
The mutex must have been locked by the calling thread. Attempting to unlock
a mutex that is not locked by the calling thread is undefined behavior.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`mutexHandle`** (input_control)  mutex `→` [HMutex](HMutex.md), [HTuple](HTuple.md) (*IntPtr*)

Mutex synchronization object.

## Result

If the mutex handle is valid, the operator `UnlockMutex` returns
2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`LockMutex`,
`TryLockMutex`

## Possible Successors

`LockMutex`,
`TryLockMutex`,
`ClearMutex`

## Module

Foundation
