# clear_mutex (Operator)

## Name

`clear_mutex` — Clear the mutex synchronization object.

## Signature

`clear_mutex( : : MutexHandle : )`

## Description

`clear_mutex` destroys the mutex object given by *`MutexHandle`*.
The mutex must be unlocked. After calling
`clear_mutex`, the mutex can no longer be used. The
handle *`MutexHandle`* becomes invalid.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- MutexHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`MutexHandle`** (input_control, state is modified)  mutex `→`  (handle)

Mutex synchronization object.

## Result

If the mutex handle is valid, the operator `clear_mutex`
returns 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`create_mutex`

## See also

`create_mutex`

## Module

Foundation
