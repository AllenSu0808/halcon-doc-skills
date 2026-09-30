# ClearMutex (Operator)

## Name

`ClearMutex` — Clear the mutex synchronization object.

## Signature

`static void HOperatorSet.ClearMutex(HTuple mutexHandle)`

`void HMutex.ClearMutex()`

## Description

`ClearMutex` destroys the mutex object given by *`mutexHandle`*.
The mutex must be unlocked. After calling
`ClearMutex`, the mutex can no longer be used. The
handle *`mutexHandle`* becomes invalid.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- mutexHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`mutexHandle`** (input_control, state is modified)  mutex `→` [HMutex](HMutex.md), [HTuple](HTuple.md) (*IntPtr*)

Mutex synchronization object.

## Result

If the mutex handle is valid, the operator `ClearMutex`
returns 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`CreateMutex`

## See also

`CreateMutex`

## Module

Foundation
