# try_lock_mutex (Operator)

## Name

`try_lock_mutex` — Lock a mutex synchronization object.

## Signature

`def try_lock_mutex(mutex_handle: HHandle) -> int`

## Description

`try_lock_mutex` behaves identically to [`lock_mutex`](lock_mutex.md), except
that it does not block the calling thread if the mutex is already locked by
another thread but returns immediately. The state of the mutex before trying
to lock it is returned in *`busy`*. *1* indicates that the mutex
was already locked before calling `try_lock_mutex`, *0* that
the mutex was unlocked (signaled).

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`mutex_handle`** (input_control)  mutex `→` HHandle

Mutex synchronization object.

**`busy`** (output_control)  number `→` int

Mutex already locked?

## Result

If the mutex handle is valid, the operator `try_lock_mutex`
returns 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_mutex`

## Possible Successors

`unlock_mutex`

## See also

`lock_mutex`

## Module

Foundation
