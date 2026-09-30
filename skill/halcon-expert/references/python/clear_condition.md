# clear_condition (Operator)

## Name

`clear_condition` — Destroy a condition synchronization object.

## Signature

`def clear_condition(condition_handle: HHandle) -> None`

## Description

`clear_condition` destroys the condition object given in
*`condition_handle`*. No threads should be waiting on the condition at
the time `clear_condition` is called. After calling
`clear_condition`, the condition can no longer be used.
The handle *`condition_handle`* becomes invalid.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- condition_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`condition_handle`** (input_control, state is modified)  condition `→` HHandle

Condition synchronization object.

## Result

If the condition handle is valid, the operator `clear_condition`
returns 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_condition`

## See also

`create_condition`

## Module

Foundation
