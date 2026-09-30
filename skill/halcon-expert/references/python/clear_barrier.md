# clear_barrier (Operator)

## Name

`clear_barrier` — Destroy a barrier synchronization object.

## Signature

`def clear_barrier(barrier_handle: HHandle) -> None`

## Description

`clear_barrier` destroys the barrier object given in
*`barrier_handle`*. No threads should be waiting on the barrier at the
time `clear_barrier` is called. After calling `clear_barrier`,
the barrier can no longer be used.
The handle *`barrier_handle`* becomes invalid.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- barrier_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`barrier_handle`** (input_control, state is modified)  barrier `→` HHandle

Barrier synchronization object.

## Result

If the barrier handle is valid, the operator `clear_barrier` returns
2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_barrier`

## See also

`create_barrier`

## Module

Foundation
