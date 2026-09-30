# unlock_mutex (Operator)

## Name

`unlock_mutex` — Unlock a mutex synchronization object.

## Signature

`def unlock_mutex(mutex_handle: HHandle) -> None`

## Description

`unlock_mutex` unlocks the mutex object given by *`mutex_handle`*.
The mutex must have been locked by the calling thread. Attempting to unlock
a mutex that is not locked by the calling thread is undefined behavior.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`mutex_handle`** (input_control)  mutex `→` HHandle

Mutex synchronization object.

## Result

If the mutex handle is valid, the operator `unlock_mutex` returns
2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`lock_mutex`,
`try_lock_mutex`

## Possible Successors

`lock_mutex`,
`try_lock_mutex`,
`clear_mutex`

## Module

Foundation
