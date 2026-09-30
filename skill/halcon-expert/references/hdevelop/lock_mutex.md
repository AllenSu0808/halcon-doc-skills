# lock_mutex (Operator)

## Name

`lock_mutex` — Lock a mutex synchronization object.

## Signature

`lock_mutex( : : MutexHandle : )`

## Description

`lock_mutex` locks the mutex given by *`MutexHandle`*. If the
mutex is currently unlocked, it becomes locked and owned by the calling
thread, and `lock_mutex` returns immediately. If the mutex is
already locked by another thread, the calling thread waits until the mutex
is unlocked. The kind of wait is defined by the mutex' attributes set during
creation in [`create_mutex`](create_mutex.md).

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MutexHandle`** (input_control)  mutex `→`  (handle)

Mutex synchronization object.

## Result

If the mutex handle is valid, the operator `lock_mutex` returns 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`create_mutex`

## Possible Successors

`unlock_mutex`

## See also

`try_lock_mutex`

## Module

Foundation
