# clear_condition (Operator)

## Name

`clear_condition` — Destroy a condition synchronization object.

## Signature

`clear_condition( : : ConditionHandle : )`

## Description

`clear_condition` destroys the condition object given in
*`ConditionHandle`*. No threads should be waiting on the condition at
the time `clear_condition` is called. After calling
`clear_condition`, the condition can no longer be used.
The handle *`ConditionHandle`* becomes invalid.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- ConditionHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`ConditionHandle`** (input_control, state is modified)  condition `→`  (handle)

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
